#!/usr/bin/env python

import click
from Run3ModelGen.condor_handler import CondorHandler

@click.command()
@click.option('--eos_dir', help='Full path to directory on EOS containing individual process dirs.', required=True)
@click.option('--condor_dir', default="extractModels_condor_log", type=str, help='Log dir containing condor info.')
@click.option('--selection', type=str, default="akarr['SS_m_h']!=-1", help='Selection to apply.')
@click.option('--num_jobs', default=None, type=int, help='Number of batch jobs to submit. Will extract all subdirs if not supplied.')
@click.option('--flavour', default="tomorrow", type=str, help='JobFlavour for condor jobs. Use "espresso" for testing.')
@click.option('--force', is_flag=True, type=bool, help='Force overriding condor_dir.')
def main(eos_dir, condor_dir, selection, num_jobs, force):
    '''Main script for submitting condor jobs for model generation.'''

    # Initialise CondorHandler for handling submission
    handler = CondorHandler(mode="extractModels", eos_dir=eos_dir, condor_dir=condor_dir, selection=selection, num_jobs=num_jobs, force=force)
    
    # Generate submission files
    handler.prep_subfile()
    
    # Submit condor jobs
    handler.submit_jobs()

if __name__ == "__main__":
    main()
