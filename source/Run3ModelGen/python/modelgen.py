'''Module for ModelGenerator class'''

import yaml
import numpy as np
import os
datadir = os.environ['DATAPATH'].split(':')[0]

import pyslha

from Run3ModelGen.ntupling import mkntuple

class ModelGenerator:
    '''Class for Model Generation.'''
    def __init__(self, config_file: str = None) -> None:
        '''Initialise scan.'''
        
        # Print logo. Note: ASCII art generated with https://patorjk.com/software/taag/ (Small, Fitted)
        with open(f"{datadir}/logo.txt", 'r') as file:
            logo = file.read()
        print("\n"+logo+"\n")
        
        self.config_file = config_file
        self.points = {}
        
        # Add all keys in config_file as attributes. Replace attribute by default if not provided
        default_config = f"{datadir}/default_config.yaml"
        config_dict = self.read_yaml_file(self.config_file) if self.config_file is not None else {}
        
        for key, defaultval in self.read_yaml_file(default_config).items():
            if key in config_dict:
                setattr(self, key, config_dict[key])
            else:                
                setattr(self, key, defaultval)
        
        # Set numpy seed:
        np.random.seed(self.seed)
        
        # Print information on initialised generator
        print(f"Initialised ModelGenerator with:")
        for var, varval in vars(self).items():
            if var == 'parameters':
                print(f"\t{var} = ")
                for param, paramval in varval.items(): print(f"\t\t{param}: {paramval}")
            elif var == 'steps':
                print(f"\t{var} = ")
                for step in varval: print(f"\t\t{step}")
            else:
                print(f"\t{var} = {varval}")

        return None
    
    def read_yaml_file(self, file_path: str) -> dict:
        '''Function for reading yaml file. Returns dict.'''
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        return data
    
    def sample_flat(self) -> None:
        '''Function for sampling parameters defined in config_dict ranges.'''
        
        for key, scanrange in self.parameters.items():
            self.points[key] = np.random.uniform(scanrange[0], scanrange[1], self.num_models)
            
        return None
            
    def prep_input(self, modelnum: int, output_dir: str) -> str:
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
        
        preppedfile = f"{self.scan_dir}/{output_dir}/{modelnum}.slha" 
        pyslha.write(preppedfile, rawfile)
        
        return None
    
    def run_SPheno(self, modelnum: int, input_dir: str, output_dir: str, log_dir: str) -> None:
        '''Run SPheno.'''
        
        infile = f"{self.scan_dir}/{input_dir}/{modelnum}.slha"
        outfile = f"{self.scan_dir}/{output_dir}/{modelnum}.slha"
        logfile = f"{self.scan_dir}/{log_dir}/{modelnum}.log"
        
        os.system(f"SPheno {infile} {outfile} &> {logfile}")
        
        return None
    
    def generate_models(self) -> None:
        '''Main function to generate models.'''
        
        print(f"Starting Model Generation...")
        
        # Set up directories for saving scan
        print(f"Setting up output directories for scan\n")
        os.system(f"rm -r {self.scan_dir}")
        os.mkdir(self.scan_dir)
        
        for step in self.steps:
            dirns = ['output_dir', 'log_dir']
            for dirn in dirns:
                if dirn in step: os.mkdir(f"{self.scan_dir}/{step[dirn]}")
        
        if self.prior == 'flat':
            self.sample_flat()
        else:
            raise ValueError(f"ERROR: prior {self.prior} not supported. Can only be flat.")
        
        for mod in range(self.num_models):
            print(f"Generating Model: {mod} out of {self.num_models-1}")
            
            for step in self.steps:
                print(f"\trunning step: {step['name']}")
                if "input" in step['name']:
                    self.prep_input(modelnum=mod, output_dir=step['output_dir'])
                elif "SPheno" in step['name']:
                    self.run_SPheno(modelnum=mod, input_dir=step['input_dir'], output_dir=step['output_dir'], log_dir=step['log_dir'])
                else:
                    raise ValueError(f"ERROR: step name {step['name']} not supported!")
                
        print("\nFinished generating models!")
        
        return None
    
    def mkntuple(self) -> None:
        '''Promote ntuple making to class attribute.'''
        
        return mkntuple(self.scan_dir, self.num_models, self.isGMSB)