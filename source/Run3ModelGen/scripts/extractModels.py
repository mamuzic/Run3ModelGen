#!/usr/bin/env python

import click
from Run3ModelGen.extractor import ModelExtractor

@click.command()
@click.option('--scan_dir', type=str, help='Scan directory to extract models from. Can also be a .tar ball.', required=True)
@click.option('--root_file', type=str, help='Root NTuple with scan info', required=True)
@click.option('--selection', type=str, default="akarr['SS_m_h']!=-1", help='Selection to apply.')
def main(scan_dir, root_file, selection):
    '''Main script for submitting condor jobs for model generation.'''

    # Initialise ModelExtractor
    ModExt = ModelExtractor(scan_dir=scan_dir, root_file=root_file, selection=selection)
    
    # Select interesting models
    ModExt.select_models()
    
    # Move interesting models to EOS
    ModExt.move_models()
    
if __name__ == "__main__":
    main()
