#!/usr/bin/env python

from Run3ModelGen.modelgen import ModelGenerator

def main():
    # from argparse import ArgumentParser
    # parser = ArgumentParser()
    # parser.add_argument('--config', default='scan_config.yaml', help='Yaml file containing scan configuration')
    # args = parser.parse_args()

    ModelGen = ModelGenerator()
    
    ModelGen.generate_models()
    
    print("This Test is tested!")

if __name__ == "__main__":
    main()
