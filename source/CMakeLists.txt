# Main CMakeLists.txt for the Run3ModelGen project

# Mandatory setting for minimal CMake requirement
cmake_minimum_required( VERSION 3.20 )

# Create a project
project( Run3ModelGen )

include( ExternalProject )

# Add subdirectories for tools that need tweaking
add_subdirectory( SPheno-4.0.5beta )
add_subdirectory( micromegas_5.2.1 )

# Add ExternalProjects for tools that run out-of-the-box

# Add softsusy as ExternalProject
ExternalProject_Add( softsusy
    PREFIX softsusy-4.1.11
    URL http://softsusy.hepforge.org/downloads/softsusy-4.1.11.tar.gz
    DOWNLOAD_EXTRACT_TIMESTAMP NEW
    CONFIGURE_COMMAND <SOURCE_DIR>/configure
    BUILD_COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}" ${CMAKE_MAKE_PROGRAM}
    INSTALL_COMMAND ""
)

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

# Add shell script to place all relevant files in build
add_custom_target( Run3ModelGen
    COMMENT "Building Run3ModelGen"
    COMMAND ${CMAKE_SOURCE_DIR}/cmake_build_env.sh -s ${CMAKE_SOURCE_DIR} -b ${CMAKE_BINARY_DIR}
    DEPENDS SPheno softsusy micromegas superiso
)

# make Run3ModelGen the default target for "make"
add_custom_target(default_target DEPENDS Run3ModelGen)