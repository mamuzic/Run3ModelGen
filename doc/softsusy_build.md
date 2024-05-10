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

Since softsusy is nicely set up by default, we can simply add it as an external project in the main [CMakeLists.txt](../source/CMakeLists.txt):
```cmake
ExternalProject_Add( softsusy
    PREFIX softsusy-4.1.11
    URL http://softsusy.hepforge.org/downloads/softsusy-4.1.11.tar.gz
    CONFIGURE_COMMAND <SOURCE_DIR>/configure
    BUILD_COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}" ${CMAKE_MAKE_PROGRAM}
    INSTALL_COMMAND ""
)
```

Additionally, edit [source/cmake_build_env.sh](../source/cmake_build_env.sh) to append the executeable to `PATH`.