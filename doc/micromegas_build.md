# Adding micromegas to the framework

This file collects steps I undertook to build micromegas_5.2.1 with pixi.

## 1. Extract the original .tar ball
```bash
tar -xzf ../micromegas_5.2.1.tgz
```

## 2. Edit the relevant files to support building. These are:
1. [source/micromegas_5.2.1/CalcHEP_src/getFlags](../source/micromegas_5.2.1/CalcHEP_src/getFlags): Set correct compiler flags for `cc`:
```bash
CFLAGS="-g -std=gnu99 -fPIC -fcommon -L../../.pixi/envs/default/lib -lgfortran -lquadmath"` 
```

2. [source/micromegas_5.2.1/MSSM/main.c](../source/micromegas_5.2.1/MSSM/main.c): Removing unneccessary routines. Small changes to printouts for further processing.

## 3. Compile micromegas with:
```bash
cd micromegas_5.2.1
make
cd MSSM
make
```

## 4. Incorporating in the cmake pipeline

After calling `make clean`, added a CMakeLists.txt file for micromegas, making the in-source build work. Additionally, edit [source/cmake_build_env.sh](../source/cmake_build_env.sh) to append the executeable to `PATH`.

## 5. Out-of-source build

To move to out-of-source building, I modified micromega's [CMakeLists.txt](../source/micromegas_5.2.1/CMakeLists.txt) to copy the entire source directory into the build dir and compile there. While this is pretty unclean, micromegas uses a large number of Makefiles, which otherwise would all need to be modified.

## 6. Changes for fresh pulls

Since empty directories are not included in git, I needed to modify the micromegas [CMakeLists.txt](../source/micromegas_5.2.1/CMakeLists.txt) to create them:
```cmake
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM/work/tmp)
...
```