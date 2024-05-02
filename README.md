# Run3ModelGen

Draft repo for updated shiny pMSSM model generation. Aiming for this repo to be fully independent of HTCondor & lxplus as well as being fully Dockerised.

## Targets
- [x] Move from shell scripts to Makefile structure for building
- [x] migrate to alma9
- [x] Dockerise
- [x] Add CI
- [ ] Update software content
- [ ] Make compatible with GAMBIT scanners
- [ ] Improve overall readability & Useability
- [x] Make venv to not clutter the user's local AB python -> solved with pixi!

### Software content

| Software | Run 2 Version | Implemented | Latest Version | Implemented |
| - | - | - | - | - |
| SPheno | 4.0.5beta | &#x2705; | 4.0.5 | &#x274c; |
| Softsusy | 4.1.11 | &#x274c; | 4.1.13 | &#x274c; |
| FeynHiggs | 2.19.0 | &#x274c; | 2.19.0 | &#x274c; |
| SuperIso | 4.0 | &#x274c; | 4.1 7 | &#x274c; |
| GM2Calc | 2.0.0 | &#x274c; | 2.2.0 | &#x274c; |
| micrOMEGAs | 5.2.1 | &#x274c; | 6.0 | &#x274c; |

### Functionalities

- [x] Script to run flat scan & save output models
- [x] Docker images of framework
- [ ] Ntuple making
- [ ] Model selection for factory
- [ ] HTCondor support for larger parallel scans (using Docker?!)
- [ ] Support for non-alma9 machines (e.g. MacOS)

## Installation

### pixi

This repo uses [pixi](https://pixi.sh/latest/) to manage packages, compilers, etc. Hopefully this will only make things easier for you as a user, but it does require installing pixi locally before we can compile the Run3ModelGen code. To install pixi, do:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
. ~/.bash_profile 
```

Please note that since pixi edits your `.bash_profile` automatically, it should be set up correctly on your next login.

### Run3ModelGen

Having installed pixi, we can use the `pixi.toml` and `pixi.lock` files to start a shell with the correct environment and install the Run3ModelGen:

```bash
pixi shell
mkdir build; cd build
cmake ../source
make
source setup.sh
```

## On startup

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

# FAQ

## pixi

If you wish to edit the pixi package content, you can either edit the `pixi.toml` file directly, or use (some of) these handy commands which I used to initiate the repo:

```bash
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

## More

More will follow soon. In the meantime, if you have any questions at all, please contact jonas.wuerzinger@cern.ch.