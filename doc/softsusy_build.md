# Adding softsusy to the framework

This file collects steps I undertook to build softsusy-4.1.11 with pixi.

## 1. Extract the original .tar ball
```bash
tar -xzf ../../softsusy-4.1.11.tar.gz
```

## 2. Compile sofsusy with
```bash
cd sofsusy-4.1.11
./configure
make
```

## 4. Incorporating in the cmake pipeline

After calling `make clean`, added a CMakeLists.txt file for softsusy, making the in-source build work. Additionally, edit [source/cmake_build_env.sh](../source/cmake_build_env.sh) to append the executeable to `PATH`.

## 5. Out-of-source build

Since softsusy's makefile is nicely set up per default, this is completely solved by setting the `WORKING_DIRECTORY` for the binary dir in [source/softsusy-4.1.11/CMakeLists.txt](../source/softsusy-4.1.11/CMakeLists.txt), e.g.:
```cmake
# Add a custom target to call make
add_custom_target(softsusy
    COMMENT "Building softsusy"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS softsusy_configure
)
```