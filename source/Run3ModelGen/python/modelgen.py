import yaml
import numpy as np
np.random.seed(123)
import os
datadir = os.environ['DATAPATH'].split(':')[0]

import Run3ModelGen.pyslha as pyslha

class ModelGenerator:
    '''Class for Model Generation.'''
    def __init__(self, config_file: str = f"{datadir}/default_config.yaml", num_models: int = 100) -> None:
        '''Initialise scan.'''
        self.config_file = config_file
        self.config_dict = self.read_yaml_file(self.config_file)
        self.num_models = num_models
        self.points = {}
        
        # Set up directories for saving scan:
        os.system('rm -r scan')
        
        self.input_dir = 'scan/inputs'
        self.SPheno_dir = 'scan/SPheno'
        self.SPheno_log_dir = 'scan/SPheno_log'
        
        os.makedirs(self.input_dir)
        os.makedirs(self.SPheno_dir)
        os.makedirs(self.SPheno_log_dir)
        
        print(f"Initialised ModelGenerator with:\n config_file: {self.config_file}\n config_dict: {self.config_dict}\n num_models: {self.num_models}\n")

        return None
    
    def read_yaml_file(self, file_path: str) -> dict:
        '''Function for reading yaml file. Returns dict.'''
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        return data
    
    def sample_flat(self) -> None:
        '''Function for sampling parameters defined in config_dict ranges.'''
        
        for key, scanrange in self.config_dict['parameters'].items():
            print(f"Key: {key}, scanrange: {scanrange}")
            self.points[key] = np.random.uniform(scanrange[0], scanrange[1], self.num_models)
            
        return None
            
    def prep_input(self, modelnum: int) -> str:
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
        
        preppedfile = f"{self.input_dir}/{modelnum}.slha" 
        pyslha.write(preppedfile, rawfile)
        
        return preppedfile
    
    def run_SPheno(self, infile: str, outfile: str, logfile: str) -> None:
        '''Run SPheno.'''
        
        os.system(f"SPheno {infile} {outfile} &> {logfile}")
        
        return None