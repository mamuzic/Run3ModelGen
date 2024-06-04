#!/bin/bash

# Export pixi path
. ~/.bash_profile

export ClusterId=$1
export ProcId=$2
export RUN3MODELGENDIR=$3
export EosDir=$4
export Sel=$5
# export IsGMSBRun=$4 # TODO: Add this option!
shift $#

echo "Running with arguments: $ClusterId, $ProcId, $RUN3MODELGENDIR, $EosDir, $Sel"

cd $RUN3MODELGENDIR
source build/setup.sh

cd run

# run local model extraction
pixi run extractModels.py --scan_dir $EosDir/$ProcId/scan.$ClusterId.$ProcId.tar.gz --root_file $EosDir/$ProcId/ntuple.$ClusterId.$ProcId.root --selection $Sel