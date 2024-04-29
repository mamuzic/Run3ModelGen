#!/bin/bash

# Initialize variables to hold the values
source_dir=""
build_dir=""

# Parse command-line options
while getopts 's:b:' flag; do
    case "${flag}" in
        s) source_dir="${OPTARG}" ;;
        b) build_dir="${OPTARG}" ;;
        *) echo "Usage: $0 -s <source_dir> -b <build_dir>" >&2
           exit 1 ;;
    esac
done

# Ensure both values are provided
if [[ -z "$source_dir" || -z "$build_dir" ]]; then
    echo "Both source and build dir need to be provided."
    exit 1
fi

# Define a function to ignore errors
handle_error() {
    echo "WARNING: some files in $build_dir already existed. Is this intended?"
    # Additional error handling code here
    # exit 1
}

# Move setup script to build dir
cp $source_dir/setup.sh $build_dir

# Activate custom error handling
trap 'handle_error' ERR

# Create build dir
mkdir $build_dir/Run3ModelGen 2>/dev/null

# Link python modules in build
ln -s $source_dir/Run3ModelGen/python/* $build_dir/Run3ModelGen/ 2>/dev/null

# Deactivate custom error handling
trap - ERR

# Manipulating env vars: PATH, PYTHONPATH and DATAPATH
echo 'export PATH="'${build_dir}'/Run3ModelGen:$PATH"' >> $build_dir/setup.sh
echo 'export PATH="'${source_dir}'/Run3ModelGen/scripts:$PATH"' >> $build_dir/setup.sh
echo 'export PYTHONPATH="'${build_dir}':$PYTHONPATH"' >> $build_dir/setup.sh
echo 'export DATAPATH="'${source_dir}/data':$DATAPATH"' >> $build_dir/setup.sh