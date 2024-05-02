#!/usr/bin/env python

from Run3ModelGen.modelgen import ModelGenerator

def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--config', default=None, help='Yaml file containing scan configuration')
    args = parser.parse_args()

    # If config file is not provided, use default for initiating ModelGenerator
    ModelGen = ModelGenerator(args.config)
    
    # Generate models and save them according to the config yaml
    ModelGen.generate_models()
    
    # Make NTuple
    ModelGen.mkntuple()

if __name__ == "__main__":
    main()
