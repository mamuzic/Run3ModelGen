# Run3ModelGen <!-- omit in toc -->

Draft repo for updated shiny pMSSM model generation. Aiming for this repo to be fully independent of HTCondor & lxplus as well as being fully Dockerised.

# Table of Contents <!-- omit in toc -->

- [Targets](#targets)
  - [Software content](#software-content)
  - [Functionalities](#functionalities)
- [Installation](#installation)
  - [pixi](#pixi)
  - [Run3ModelGen](#run3modelgen)
- [On startup](#on-startup)
- [Running](#running)
  - [Changing the scan configuration](#changing-the-scan-configuration)
- [FAQ](#faq)
  - [pixi](#pixi-1)
  - [Gaps in the scan ranges](#gaps-in-the-scan-ranges)
  - [More](#more)

# Targets
- [x] Move from shell scripts to Makefile structure for building
- [x] migrate to alma9
- [x] Dockerise
- [x] Add CI
- [ ] Update software content
- [ ] Add missing functionalities
- [ ] Make compatible with GAMBIT scanners
- [ ] Improve overall readability & Useability
- [x] Make venv to not clutter the user's local AB python -> solved with pixi!

## Software content

| Software | Run 2 Version | Implemented | Latest Version | Implemented |
| - | - | - | - | - |
| SPheno | 4.0.5beta | &#x2705; | 4.0.5 | &#x274c; |
| Softsusy | 4.1.11 | &#x274c; | 4.1.13 | &#x274c; |
| FeynHiggs | 2.19.0 | &#x274c; | 2.19.0 | &#x274c; |
| SuperIso | 4.0 | &#x274c; | 4.1 7 | &#x274c; |
| GM2Calc | 2.0.0 | &#x274c; | 2.2.0 | &#x274c; |
| micrOMEGAs | 5.2.1 | &#x274c; | 6.0 | &#x274c; |
| EVADE | 0.2.0 | &#x274c; | 0.2.0 | &#x274c; |

## Functionalities

- [x] Script to run flat scan & save output models
- [x] Docker images of framework
- [x] Ntuple making
- [ ] Model selection for factory
- [ ] HTCondor support for larger parallel scans (using Docker?!)
- [ ] Support for non-alma9 machines (e.g. MacOS)

# Installation

## pixi

This repo uses [pixi](https://pixi.sh/latest/) to manage packages, compilers, etc. Hopefully this will only make things easier for you as a user, but it does require installing pixi locally before we can compile the Run3ModelGen code. To install pixi, do:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
. ~/.bash_profile 
```

Please note that since pixi edits your `.bash_profile` automatically, it should be set up correctly on your next login.

## Run3ModelGen

Having installed pixi, we can use the `pixi.toml` and `pixi.lock` files to start a shell with the correct environment and install the Run3ModelGen:

```bash
pixi shell
mkdir build; cd build
cmake -S source -B build
cmake --build build
source build/setup.sh
```

# On startup

As perviously mentioned, pixi should be ready to use as per your `.bash_profile`, so there is no need to do anything here. 
For settup up the Run3ModelGen, please simply execute:

```bash
pixi shell
source build/setup.sh
```
And you're good to go!

# Running

The main script for generating models is [genModels.py](https://gitlab.cern.ch/jwuerzin/Run3ModelGen/-/blob/main/source/Run3ModelGen/scripts/genModels.py?ref_type=heads). If you set everything up correctly, this can simply be executed with:

```bash
genModels.py
```

The script will save the created model files and the corresponding root ntuple.

## Changing the scan configuration

If you would like to change the scan configuration or seed, simply run

```bash
genModels.py --config myconfig.yaml --seed 42 
```

where `myconfig.yaml` is your config file containing the scan configuration. If no config file is supplied, the [default config file](source/Run3ModelGen/data/default_config.yaml) will be read. All values that are missing from `myconfig.yaml` are read from the default as well.

Here the contents of this default configuration:

```yaml
scan_dir: scan
prior: flat
num_models: 10
isGMSB: False
parameters:
  tanb: [1, 60]
  M_1: [-2000, 2000]
  M_2: [-2000, 2000]
  M_3: [4000, 4000]
  AT: [-8000, 8000]
  Ab: [-2000, 2000]
  Atau: [-2000, 2000]
  mu: [-2000, 2000]
  mA: [2000, 2000]
  meL: [0, 2000]
  mtauL: [2000, 2000]
  meR: [0, 2000]
  mtauR: [2000, 2000]
  mqL1: [4000, 4000]
  mqL3: [4000, 4000]
  muR: [4000, 4000]
  mtR: [4000, 4000]
  mdR: [4000, 4000]
  mbR: [4000, 4000]
steps:
  - name: prep_input
    output_dir: input
  - name: SPheno
    input_dir: input
    output_dir: SPheno
    log_dir: SPheno_log
```

# FAQ

## pixi

If you wish to edit the pixi package content, you can either edit the `pixi.toml` file directly, or use (some of) these handy commands which I used to initiate the repo:

```bash
# Install pixi & initialise
curl -fsSL https://pixi.sh/install.sh | bash
. ~/.bash_profile 
pixi init .

# general dependencies
time pixi add 'python=3.11'
time pixi add gfortran
time pixi add cc
time pixi add gcc
time pixi add cxx-compiler
time pixi add cmake
time pixi add make
time pixi add which

# python packages on conda
time pixi add numpy
time pixi add pyyaml
time pixi add pyslha

# start shell
pixi shell
```

Please refrain from editing the `pixi.lock` file directly!

## Gaps in the scan ranges

If you'd like to run with gaps in the scan ranges, this is fully supported. Simply provide the scan ranges as a list containing the subranges, e.g.:
```yaml
...
parameters:
  tanb: [1, 60]
  M_1: [-2000, 2000]
  M_2: [[-3000, -1000], [-1000, 800], [1000, 3000]]
...
```

## More

More will follow soon. In the meantime, if you have any questions at all, please contact jonas.wuerzinger@cern.ch.