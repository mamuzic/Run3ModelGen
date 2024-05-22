#!/usr/bin/env python

import click
from Run3ModelGen.modelgen import ModelGenerator

@click.command()
@click.option('--config', default=None, help='Yaml file containing scan configuration. If no config is provided, will read from the default.')
@click.option('--scan_dir', default="scan", type=str, help='Scan output directory.')
@click.option('--seed', default=123, type=int, help='Seed for np random number generation.')
def main(config, scan_dir, seed):
    '''Main script for generating models according to provided config file. Will also generate root NTuple.'''

    # If config file is not provided, use default for initiating ModelGenerator
    ModelGen = ModelGenerator(config, scan_dir, seed)
    
    # Generate models and save them according to the config yaml. Note: This automatically overwrites the scan directory.
    ModelGen.generate_models()
    
    # Make NTuple
    ModelGen.mkntuple()

if __name__ == "__main__":
    main()
