#!/bin/bash

# Export pixi path
. ~/.bash_profile

export ClusterId=$1
export ProcId=$2
export RUN3MODELGENDIR=$3
export config=$4
# export IsGMSBRun=$4 # TODO: Add this option!
shift $#

echo "Running with arguments: $ClusterId, $ProcId, $RUN3MODELGENDIR, $config"

cd $RUN3MODELGENDIR
source build/setup.sh

cd run

# run local model generation with config file if supplied
if [ $config == "None" ]; then
    pixi run genModels.py --scan_dir $_CONDOR_SCRATCH_DIR/scan.$ClusterId.$ProcId --seed $ClusterId$ProcId
else
    pixi run genModels.py --scan_dir $_CONDOR_SCRATCH_DIR/scan.$ClusterId.$ProcId --seed $ClusterId$ProcId --config $config
fi

# move back to condor dir
cd $_CONDOR_SCRATCH_DIR

# setup output dirs
mkdir -p $EOSPATH/$ClusterId/$ProcId

# make tar ball of scan dir
tar -czf scan.$ClusterId.$ProcId.tar.gz scan.$ClusterId.$ProcId

# copy tar ball, config file and ntuple to EOS
echo "Saving results in $EOSPATH/$ClusterId/$ProcId"
cp scan.$ClusterId.$ProcId.tar.gz $EOSPATH/$ClusterId/$ProcId
cp scan.$ClusterId.$ProcId/*.yaml $EOSPATH/$ClusterId/
cp scan.$ClusterId.$ProcId/ntuple.$ClusterId.$ProcId.root $EOSPATH/$ClusterId/$ProcId/