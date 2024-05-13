# Adding superISO to the framework

This file collects steps I undertook to build superiso_v4.0 with pixi.

## 1. Extract the original .tar ball
```bash
tar -xzf ../superiso_v4.0.tgz
```

## 2. Edits to the original files

Might not be necessary here?

## 3. Compile with:
```bash
cd superiso_v4.0
make
make slha
```

## 4. Incorporating in the cmake pipeline

Since we don't need to edit superiso, we can use CMake's `ExternalProject_Add` for superiso:
```cmake
# Add superiso as ExternalProject
ExternalProject_Add( superiso
    PREFIX superiso_v4.0
    URL "${CMAKE_SOURCE_DIR}/superiso_v4.0.tgz"
    DOWNLOAD_EXTRACT_TIMESTAMP NEW
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${CMAKE_MAKE_PROGRAM} && ${CMAKE_MAKE_PROGRAM} slha
    INSTALL_COMMAND ""
    BUILD_IN_SOURCE 1
)
```

Which technically only does an in-source build, but since the files are extrated into our build directory, that's good enough. Unfortunately, superiso does not allow automatic downloads, so I'm adding the tar ball locally.
Additionally, edit [source/cmake_build_env.sh](../source/cmake_build_env.sh) to append the executeable to `PATH`.
