#!/usr/bin/env python

import click
from Run3ModelGen.condor_handler import CondorHandler

@click.command()
@click.option('--config', default=None, help='Yaml file containing scan configuration. If no config is provided, will read from the default.')
@click.option('--condor_dir', default="scan_condor", type=str, help='Log dir containing condor info.')
@click.option('--num_jobs', default=2, type=int, help='Number of batch jobs to submit.')
@click.option('--force', is_flag=True, type=bool, help='Force overriding condor_dir.')
def main(config, condor_dir, num_jobs, force):
    '''Main script for submitting condor jobs for model generation.'''

    # Initialise CondorHandler for handling submission
    handler = CondorHandler(config, condor_dir, num_jobs, force)
    
    # Generate submission files
    handler.prep_subfile()
    
    # Submit condor jobs
    handler.submit_jobs()

if __name__ == "__main__":
    main()
