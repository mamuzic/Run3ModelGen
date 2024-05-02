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

Please not that since pixi edits your `.bash_profile` automatically, it should be set up correctly on your next login.

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

This repo is still very much under development! So far, one script has been added, which generates random models using `SPheno`. If you set everything up correctly, the script can be exectued with:

```bash
genModels.py
```

# FAQ

Will follow soon. In the meantime, if you have any questions at all, please contact jonas.wuerzinger@cern.ch.