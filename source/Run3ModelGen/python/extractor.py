'''Module for extracting interesting models from scan.'''

import os
datadir = os.environ['DATAPATH'].split(':')[0]

import re
import uproot
import awkward
import yaml
import tarfile

import structlog
import logging
log = structlog.get_logger()
structlog.stdlib.recreate_defaults(log_level=logging.INFO)  # so we have logger names

class ModelExtractor:
    '''Class for extracting interesting models from scan.'''
    def __init__(self, scan_dir: str, root_file: str, selection: str) -> None:
        
        # Print logo. Note: ASCII art generated with https://patorjk.com/software/taag/ (Small, Fitted)
        with open(f"{datadir}/logo.txt", 'r') as file:
            logo = "\n"+file.read()+"\n"
        print(logo)
        
        self.scan_dir = scan_dir
        self.root_file = root_file
        self.selection = selection
        
        log.info("Initialised ModelExtractor with:")
        for var, varval in vars(self).items():
            log.info(f"\t{var} = {varval}")
        
        return None
    
    def select_models(self) -> None:
        '''Select models passing selections using root_file. Returns array with model ids.'''
        
        # Get list of keys to read from NTuple to reduce comp load
        pattern = r"\['(.*?)'\]"
        keys = list(set(re.findall(pattern, self.selection))) + ['model']
        
        log.info("Selecting models passing selection...")
        with uproot.open(f"{self.root_file}:susy") as tree:
        
            # Get akarrray using keys defined above
            akarr = tree.arrays(keys, library="ak")
            
        # Create & apply mask from selections
        mask = eval(self.selection)
        num_models = len(akarr)
        akarr = akarr[mask]
        
        # Set array with model IDs as class attribute
        self.modarr = akarr['model']
        log.info(f"Found {len(self.modarr)}/{num_models} models passing selection.")
        
        return None
    
    def move_models(self) -> None:
        '''Move selected models to EOS.'''
        
        # Use ProcId as subdirectory name
        ProcId = self.root_file.split('.')[-2]
        
        # Determine if scan_dir is tarfile
        try: istar = tarfile.is_tarfile(self.scan_dir)
        except: istar = False
        
        # Set up extraction for tarfile/regular directory
        if istar:
            log.info(f"Scan dir {self.scan_dir} is .tar ball! Will extract files from it...")
        
            # Open tar file 
            tar = tarfile.open(self.scan_dir, "r:gz")
        
            # Get list of subdirs to check, as well as list of file extentions
            subdirlist = []
            suffixlist = []
            
            subdir = "dummystr"
            for member in tar.getmembers():
                if '/' in member.name and member.isdir():
                    subdir = member.name.split("/")[1]
                    subdirlist += [subdir,]
                elif member.isdir():
                    tarbase = member.name
                elif subdir in member.name and not member.isdir():
                    suffix = member.name.split('.')[-1]
                    suffixlist += [suffix,]
                    subdir = "dummystr"
            
            # Get output directory name   
            scanoutdir = self.scan_dir.split('/')[-1].split('.')[1]
        
        else:
            log.info(f"Scan dir {self.scan_dir} is regular directory! Wil extract files from it...")
            
            # Get list of subdirs to check, as well as list of file extentions
            subdirlist = [subdir for subdir in os.listdir(self.scan_dir) if os.path.isdir(f"{self.scan_dir}/{subdir}")]
            suffixlist = [os.listdir(f"{self.scan_dir}/{subdir}")[0].split('.')[-1] for subdir in subdirlist]
            
            # Get output directory name
            scanoutdir = self.scan_dir.split('/')[-1]
        
        # Create output directory
        outdir = f"{os.environ['EOSPATH']}/SelectedModels/{scanoutdir}/Models"
        try: os.makedirs(outdir)
        except: log.warning(f"Output directory {outdir} already exists. Please make sure that this is intended!")
        
        # Dump options in output dir
        with open(f"{os.environ['EOSPATH']}/SelectedModels/{scanoutdir}/extractor_flags.yaml", "w") as file:
            log.info(f"Dumping extractor flags in {os.environ['EOSPATH']}/SelectedModels/{scanoutdir}/extractor_flags.yaml")
            skipkeys = ['modarr']
            dumpdict = {key: value for key, value in vars(self).items() if key not in skipkeys}
            yaml.dump(dumpdict, file, default_flow_style=False)
            
        # Loop over subdirectories
        for i in range(len(subdirlist)):
            subdir = subdirlist[i]
            suffix = suffixlist[i]
                
            destindir = f"{outdir}/{subdir}/{ProcId}"
            
            log.info(f"Filling dir: {destindir}/")
            
            # Create subdir in outdir if it does not yet exist
            try: os.makedirs(f"{destindir}")
            except: pass
            
            # Use modarr to move files to output dir
            for modid in self.modarr:
                modid = int(modid)
                
                # Extract file contents if tar file supplied, copy file otherwise
                if istar:
                    extfile = tar.extractfile(f"{tarbase}/{subdir}/{modid}.{suffix}")
                    with open(f"{destindir}/{modid}.{suffix}", "wb+") as selfile: 
                        for line in extfile: selfile.write(line)
                
                else:
                    os.system(f"cp {self.scan_dir}/{subdir}/{modid}.{suffix} {destindir}")
        
        if istar: tar.close()
        
        return None