'''Module for handling batch jobs.'''

import os
datadir = os.environ['DATAPATH'].split(':')[0]

import structlog
log = structlog.get_logger()
structlog.stdlib.recreate_defaults()  # so we have logger names

class CondorHandler:
    '''Class for batch job handling.'''
    def __init__(self, config_file: str = None, condor_dir: str = f"scan_condor", num_jobs: int = 2, force: bool = False) -> None:
        
        # Print logo. Note: ASCII art generated with https://patorjk.com/software/taag/ (Small, Fitted)
        with open(f"{datadir}/logo.txt", 'r') as file:
            logo = "\n"+file.read()+"\n"
        print(logo)
        
        self.config_file = config_file
        self.condor_dir = condor_dir
        self.num_jobs = num_jobs
        self.force = force
        
        # create log dir if it does not yet exist
        try:
            os.makedirs(f"{self.condor_dir}/outfiles")
        except:
            if not self.force:
                log.exception(f"condor_dir '{self.condor_dir}' already exists! Please either supply a different one or run with '--force' to override it.")
                exit()
            else:
                log.warning(f"condor_dir '{self.condor_dir}' already exists! Running in '--force' mode, so results may be overwritten.")
        
        log.info(f"Initialised CondorHandler with:")
        for var, varval in vars(self).items():
            log.info(f"\t{var} = {varval}")
        
        return None
    
    def prep_subfile(self) -> None:
        '''prepare submission files for condor run.'''
        
        # Save config file in condor_dir if supplied
        if self.config_file is not None:
            os.system(f"cp {self.config_file} {self.condor_dir}/{self.config_file}")
            log.info(f"Saved config file in {self.condor_dir}/{self.config_file}.")
            confstr = f"{os.getcwd()}/{self.condor_dir}/{self.config_file}"
        else:
            confstr = "None"
        
        subfile_text = f"""executable = {self.condor_dir}/genmodels_condor.sh

Requirements = (Machine != "b6100c26e0.cern.ch")
arguments = $(ClusterId) $(ProcId) {confstr}
output = {self.condor_dir}/outfiles/genmodels.$(ClusterId).$(ProcId).out
error = {self.condor_dir}/outfiles/genmodels.$(ClusterId).$(ProcId).err
log = {self.condor_dir}/outfiles/genmodels.$(ClusterId).$(ProcId).log
transfer_output_files = ""
RequestCpus = 4
RequestDisk = 700000
+JobFlavour = "espresso"
+MaxRuntime = 604800
queue {self.num_jobs}"""

        # save subfile text in subfile
        with open(f"{self.condor_dir}/subcondor.sub", 'w') as subfile:
            subfile.write(subfile_text)
        
        log.info(f"Written condor submission file to {self.condor_dir}/subcondor.sub")
        
        # copy executeable to condor_dir
        os.system(f"cp {datadir}/genmodels_condor.sh {self.condor_dir}/genmodels_condor.sh")
        log.info(f"Written condor bash script to {self.condor_dir}/genmodels_condor.sh")
        
        return None
    
    def submit_jobs(self) -> None:
        '''submit prepared condor jobs.'''
        
        log.info(f"Submitting jobs to condor...")
        subcode = os.system(f"condor_submit {self.condor_dir}/subcondor.sub > {self.condor_dir}/submission.log")
        with open(f"{self.condor_dir}/submission.log", 'r') as sublog:
            ClusterId = sublog.read().split()[-1].strip('.')
        
        if subcode == 0: 
            log.info(f"Submission to cluster {ClusterId} successful!")
            substr = f"0-{self.num_jobs-1}" if self.num_jobs > 1 else "0"
            log.info(f"After your models have finished generating, the .tar ball and ntuple will be saved in {os.environ['EOSPATH']}/{ClusterId}/{substr}")
        else: log.error(f"Submission failed!")
        
        
        return None