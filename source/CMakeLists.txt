# Main CMakeLists.txt for the Run3ModelGen project

# Mandatory setting for minimal CMake requirement
cmake_minimum_required( VERSION 3.20 )

# Create a project
project( Run3ModelGen )

include( ExternalProject )

# Add subdirectories
add_subdirectory( SPheno-4.0.5beta )
add_subdirectory( micromegas_5.2.1 )

# Add softsusy as ExternalProject because it builds out-of-the-box
ExternalProject_Add( softsusy
    PREFIX softsusy-4.1.11
    URL http://softsusy.hepforge.org/downloads/softsusy-4.1.11.tar.gz
    CONFIGURE_COMMAND <SOURCE_DIR>/configure
    BUILD_COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}" ${CMAKE_MAKE_PROGRAM}
    INSTALL_COMMAND ""
)

# Add shell script to place all relevant files in build
add_custom_target( Run3ModelGen
    COMMENT "Building Run3ModelGen"
    COMMAND ${CMAKE_SOURCE_DIR}/cmake_build_env.sh -s ${CMAKE_SOURCE_DIR} -b ${CMAKE_BINARY_DIR}
    DEPENDS SPheno softsusy micromegas
)

# make Run3ModelGen the default target for "make"
add_custom_target(default_target DEPENDS Run3ModelGen)