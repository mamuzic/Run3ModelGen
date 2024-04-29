# Main CMakeLists.txt for the Run3ModelGen project

# Mandatory setting for minimal CMake requirement
cmake_minimum_required( VERSION 3.20 )

# Create a project
project( Run3ModelGen VERSION 25.2 )

# Add subdirectories
add_subdirectory( SPheno-4.0.5beta )

# Add shell script to place all relevant files in build
add_custom_target( Run3ModelGen
    COMMENT "Building Run3ModelGen"
    COMMAND ${CMAKE_SOURCE_DIR}/cmake_build_env.sh -s ${CMAKE_SOURCE_DIR} -b ${CMAKE_BINARY_DIR}
    DEPENDS SPheno
)

# make Run3ModelGen the default target for "make"
add_custom_target(default_target DEPENDS Run3ModelGen)