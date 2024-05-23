#!/bin/bash

# Export pixi path
. ~/.bash_profile

export ClusterId=$1
export ProcId=$2
export EosDir=$3
export Sel=$4
# export IsGMSBRun=$4 # TODO: Add this option!
shift $#

echo "Running with arguments: $ClusterId, $ProcId, $EosDir, $Sel"

cd /afs/cern.ch/user/j/jwuerzin/work/pMSSMTaskforce/Run3ModelGen/
source build/setup.sh

cd run

# run local model extraction
pixi run extractModels.py --scan_dir $EosDir/$ProcId/scan.$ClusterId.$ProcId.tar.gz --root_file $EosDir/$ProcId/ntuple.$ClusterId.$ProcId.root --selection $Sel