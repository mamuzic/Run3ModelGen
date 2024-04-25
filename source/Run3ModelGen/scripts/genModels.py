#!/usr/bin/env python

from Run3ModelGen.modelgen import ModelGenerator

def main():
    # from argparse import ArgumentParser
    # parser = ArgumentParser()
    # parser.add_argument('--config', default='scan_config.yaml', help='Yaml file containing scan configuration')
    # args = parser.parse_args()

    # ModelGen = ModelGenerator(args.config, 10)
    ModelGen = ModelGenerator(num_models=10)
    
    ModelGen.sample_flat()
    
    print(ModelGen.points)
    print(ModelGen.points['meR'])
    
    for i in range(ModelGen.num_models):
        infile = ModelGen.prep_input(modelnum=i)
    
        ModelGen.run_SPheno(infile=infile,
                            outfile=f"{ModelGen.SPheno_dir}/{i}.slha",
                            logfile=f"{ModelGen.SPheno_log_dir}/{i}.log"
                            )
    
    print("This Test is tested!")

if __name__ == "__main__":
    main()
