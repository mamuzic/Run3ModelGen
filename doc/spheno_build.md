# Adding SPheno to the framework

This file collects steps I undertook to build SPheno-4.0.5beta with pixi.

## 1. Extract the original .tar ball
```bash
tar -xzf ../SPheno-4.0.5beta.tar.gz
```

## 2. Edits to the original files

1. [Makefile](../source/SPheno-4.0.5beta/Makefile): compile with gfortran
2. [src/Control.F90](../source/SPheno-4.0.5beta/src/Control.F90): Change `ErrCan=6` such that SPheno's errors are written into the default output.
3. [src/InputOutput.F90](../source/SPheno-4.0.5beta/src/InputOutput.F90): Allow for saving into a different output file.
4. [src/SPheno4.f90](../source/SPheno-4.0.5beta/src/SPheno4.f90): Support longer strings for filenames.

## 3. Compile SPheno with:
```bash
cd SPheno-4.0.5beta
make
```

## 4. Incorporating in the cmake pipeline

After calling `make clean`, added a [CMakeLists.txt](../source/SPheno-4.0.5beta/CMakeLists.txt) file for SPheno, which calls SPheno's custom [Makefile](../source/SPheno-4.0.5beta/Makefile):
```cmake
# Add a custom target to call make
add_custom_target(SPheno
    COMMENT "Building SPheno"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}/SPheno-4.0.5beta" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
```

## 5. Out-of-source build

For out-of-source building, I was able to modify the SPheno [Makefile](../source/SPheno-4.0.5beta/Makefile) to build into the cmake binary dir:
```Makefile
BUILD_DIR = $(abspath ${CMAKE_BINARY_DIR})
bin/SPheno:
	mkdir -p ${BUILD_DIR}/bin ${BUILD_DIR}/lib ${BUILD_DIR}/include
	cd ${Model} ; ${MAKE} F90=${F90} version=${version}
```