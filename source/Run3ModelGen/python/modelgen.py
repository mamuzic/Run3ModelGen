'''Module for ModelGenerator class'''

import yaml
import numpy as np
import os
datadir = os.environ['DATAPATH'].split(':')[0]

import pyslha

from Run3ModelGen.ntupling import mkntuple
from Run3ModelGen.microextract import microextract

import structlog
log = structlog.get_logger()
structlog.stdlib.recreate_defaults()  # so we have logger names

class ModelGenerator:
    '''Class for Model Generation.'''
    def __init__(self, config_file: str = None, seed: int = 123) -> None:
        '''Initialise scan.'''
        
        print(structlog.get_config()["processors"])
        
        # Print logo. Note: ASCII art generated with https://patorjk.com/software/taag/ (Small, Fitted)
        with open(f"{datadir}/logo.txt", 'r') as file:
            logo = "\n"+file.read()+"\n"
        print(logo)
        
        self.config_file = config_file
        self.seed = seed
        self.points = {}
        
        # Add all keys in config_file as attributes. Replace attribute by default if not provided
        default_config = f"{datadir}/default_config.yaml"
        config_dict = self.read_yaml_file(self.config_file) if self.config_file is not None else {}
        
        for key, defaultval in self.read_yaml_file(default_config).items():
            if key in config_dict:
                setattr(self, key, config_dict[key])
            # If num_models is not supplied and the prior is 'fixed', read number of models from parameters
            elif key == 'num_models' and config_dict.get('prior', None) == 'fixed':
                setattr(self, key, len(config_dict['parameters']['tanb']))
            else:                
                setattr(self, key, defaultval)
        
        # Set numpy seed:
        np.random.seed(self.seed)
        
        # Print information on initialised generator
        log.info(f"Initialised ModelGenerator with:")
        for var, varval in vars(self).items():
            if var == 'parameters':
                log.info(f"\t{var} = ")
                for param, paramval in varval.items(): log.info(f"\t\t{param}: {paramval}")
            elif var == 'steps':
                log.info(f"\t{var} = ")
                for step in varval: log.info(f"\t\t{step}")
            else:
                log.info(f"\t{var} = {varval}")

        return None
    
    def read_yaml_file(self, file_path: str) -> dict:
        '''Function for reading yaml file. Returns dict.'''
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        return data
    
    def sample_flat(self) -> None:
        '''Function for sampling parameters defined in config_dict ranges.'''
        
        for key, scanrange in self.parameters.items():
            
            # Check if the provided range is interrupted
            if type(scanrange[0]) == list:
                weights = []
                dist = 0
                
                # Loop over ranges to get weights for numbers of models
                for subrange in scanrange:
                    if type(subrange) != list: raise ValueError(f"Provided scanrange for parameter {key} is not supported!")
                    weights.append((subrange[1]-subrange[0]))
                    dist += subrange[1]-subrange[0]

                weights = [weight/dist for weight in weights]
                
                # Generate random points according to weights and append result in one np array
                # Making sure that overall number of models matches
                points_left = self.num_models
                points = np.array([])
                list_numpoints = []
                for i in range(len(scanrange)):
                    numpoints = int(self.num_models*weights[i])
                    if i == len(scanrange)-1: numpoints = points_left
                    list_numpoints += [numpoints]
                    
                    points = np.append(points, np.random.uniform(scanrange[i][0], scanrange[i][1], numpoints))
                    points_left -= numpoints
                    
                self.points[key] = points
                
                log.info(f"Found gap in scanning ranges for parameter {key}. Generated random numbers for subranges with weights:", weights=weights)
                log.info("Resulting in these numbers of points:", list_numpoints=list_numpoints)
                
            else:
                self.points[key] = np.random.uniform(scanrange[0], scanrange[1], self.num_models)
            
        return None
    
    def sample_fixed(self) -> None:
        '''Function for generating fixed points given by input config file.'''
        
        for key, pointlist in self.parameters.items():
            self.points[key] = np.array(pointlist)
            
        return None
            
    def run_step(self, modelnum: int, **kwargs) -> None:
        '''Function decorator for exectuting run_* function.'''
        step_name = kwargs['name']
        
        # Select run_ function based on step name
        if hasattr(self, f"run_{step_name}") and callable(func := getattr(self, f"run_{step_name}")):
            func(modelnum, **kwargs)
        else:
            raise KeyError(f"step {step_name} not supported!")
    
    def run_prep_input(self, modelnum: int, **kwargs) -> str:
        '''Prep input. Returns the filename of the prepped file.'''
        
        rawfile = pyslha.read(f"{datadir}/raw.slha", ignorenomass = True)
        
        rawfile.blocks['EXTPAR'][1] = self.points['M_1'][modelnum]
        rawfile.blocks['EXTPAR'][2] = self.points['M_2'][modelnum]
        rawfile.blocks['EXTPAR'][3] = self.points['M_3'][modelnum]
        rawfile.blocks['EXTPAR'][11] = self.points['AT'][modelnum]
        rawfile.blocks['EXTPAR'][12] = self.points['Ab'][modelnum]
        rawfile.blocks['EXTPAR'][13] = self.points['Atau'][modelnum]
        rawfile.blocks['EXTPAR'][23] = self.points['mu'][modelnum]
        rawfile.blocks['EXTPAR'][25] = self.points['tanb'][modelnum]
        rawfile.blocks['EXTPAR'][26] = self.points['mA'][modelnum]
        rawfile.blocks['EXTPAR'][31] = self.points['meL'][modelnum]
        rawfile.blocks['EXTPAR'][32] = self.points['meL'][modelnum] # mmuL := meL
        rawfile.blocks['EXTPAR'][33] = self.points['mtauL'][modelnum]
        rawfile.blocks['EXTPAR'][34] = self.points['meR'][modelnum]
        rawfile.blocks['EXTPAR'][35] = self.points['meR'][modelnum] # mmuR := meR
        rawfile.blocks['EXTPAR'][36] = self.points['mtauR'][modelnum]
        rawfile.blocks['EXTPAR'][41] = self.points['mqL1'][modelnum]
        rawfile.blocks['EXTPAR'][42] = self.points['mqL1'][modelnum] # mqL2 := mqL1
        rawfile.blocks['EXTPAR'][43] = self.points['mqL3'][modelnum]
        rawfile.blocks['EXTPAR'][44] = self.points['muR'][modelnum]
        rawfile.blocks['EXTPAR'][45] = self.points['muR'][modelnum] # mcR := muR
        rawfile.blocks['EXTPAR'][46] = self.points['mtR'][modelnum]
        rawfile.blocks['EXTPAR'][47] = self.points['mdR'][modelnum]
        rawfile.blocks['EXTPAR'][48] = self.points['mdR'][modelnum] # msR := mdR
        rawfile.blocks['EXTPAR'][49] = self.points['mbR'][modelnum]
        
        preppedfile = f"{self.scan_dir}/{kwargs['output_dir']}/{modelnum}.slha" 
        pyslha.write(preppedfile, rawfile)
        
        return None
    
    def run_SPheno(self, modelnum: int, **kwargs):
        '''Run SPheno.'''
        
        infile = f"{self.scan_dir}/{kwargs['input_dir']}/{modelnum}.slha"
        outfile = f"{self.scan_dir}/{kwargs['output_dir']}/{modelnum}.slha"
        logfile = f"{self.scan_dir}/{kwargs['log_dir']}/{modelnum}.log"
        
        os.system(f"SPheno {infile} {outfile} &> {logfile}")
        
        return None
    
    def run_softsusy(self, modelnum: int, **kwargs) -> None:
        '''Run softsusy.'''
        
        infile = f"{self.scan_dir}/{kwargs['input_dir']}/{modelnum}.slha"
        outfile = f"{self.scan_dir}/{kwargs['output_dir']}/{modelnum}.slha"
        
        os.system(f"softpoint.x leshouches < {infile} &> {outfile}")
        
        return None
    
    def run_micromegas(self, modelnum: int, **kwargs) -> None:
        '''Run micromegas.'''
        
        infile = f"{self.scan_dir}/{kwargs['input_dir']}/{modelnum}.slha"
        outfile_raw = f"{self.scan_dir}/{kwargs['output_dir']}_raw/{modelnum}.out"
        outfile = f"{self.scan_dir}/{kwargs['output_dir']}/{modelnum}.csv"
        
        # Run micromegas to get the raw, humanly readable output
        os.system(f"main {infile} > {outfile_raw}")
        
        # Extract values into outfile
        microextract(infilen = outfile_raw, outfilen = outfile)
        
        return None
    
    def run_superiso(self, modelnum: int, **kwargs) -> None:
        '''Run superiso.'''
        
        infile = f"{self.scan_dir}/{kwargs['input_dir']}/{modelnum}.slha"
        outfile = f"{self.scan_dir}/{kwargs['output_dir']}/{modelnum}.flha"
        
        # Run superiso and pipe humanly readable output into null
        os.system(f"slha.x {infile} &>/dev/null")
        # Move the auto-generated output file into the right location
        os.system(f"mv output.flha {outfile}")
        
        return None
    
    def generate_models(self) -> None:
        '''Main function to generate models.'''
        
        log.info(f"Starting Model Generation...")
        
        # Set up directories for saving scan
        log.info(f"Setting up output directories for scan")
        os.system(f"rm -r {self.scan_dir}")
        os.mkdir(self.scan_dir)
        
        for step in self.steps:
            dirns = ['output_dir', 'log_dir']
            for dirn in dirns:
                if dirn in step: os.mkdir(f"{self.scan_dir}/{step[dirn]}")
                if dirn in step and "micromegas" in step['name']: os.mkdir(f"{self.scan_dir}/{step[dirn]}_raw")
        
        if self.prior == 'flat':
            self.sample_flat()
        elif self.prior == 'fixed':
            self.sample_fixed()
        else:
            raise ValueError(f"ERROR: prior {self.prior} not supported. Can only be flat.")
        
        for mod in range(self.num_models):
            log.info(f"Generating Model: {mod}.slha ({mod+1}/{self.num_models})")
            
            for step in self.steps:
                log.info(f"\trunning step: {step['name']}")
                self.run_step(modelnum=mod, **step)
         
        # Dump scan config in scan_dir
        with open(f"{self.scan_dir}/scan_config.yaml", "w") as file:
            skipkeys = ['points']
            dumpdict = {key: value for key, value in vars(self).items() if key not in skipkeys}
            yaml.dump(dumpdict, file, default_flow_style=None, encoding=None)
                
        log.info("Finished generating models!")
        
        return None
    
    def mkntuple(self) -> None:
        '''Promote ntuple making to class attribute.'''
        
        return mkntuple(self.scan_dir, self.num_models, self.isGMSB)