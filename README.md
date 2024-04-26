# Run3ModelGen

Draft repo for updated shiny pMSSM model generation.

## Targets:
- [ ] Move from shell scripts to Makefile structure for building
- [ ] migrate to alma9
- [ ] Dockerise
- [ ] Add CI
- [ ] Update software content
- [ ] Make compatible with GAMBIT scanners
- [ ] Improve overall readability & Useability
- [ ] Make venv to not clutter the user's local AB python

## Installation:

Usual ATLAS stuff:

```bash
mkdir build; cd build
setupATLAS
asetup AnalysisBase,25.2.5
cmake ../source
make
source x86_64-el9-gcc13-opt/setup.sh
```