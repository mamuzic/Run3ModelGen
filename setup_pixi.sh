# curl -fsSL https://pixi.sh/install.sh | bash
# . ~/.bash_profile 
# pixi init .
time pixi add 'python=3.11'
time pixi add gfortran
time pixi add cc
time pixi add gcc
# time pixi add c++
time pixi add cmake

# python packages on conda
time pixi add numpy
time pixi add pyyaml
# time pixi add pyslha

# start shell
pixi shell