# Mandatory setting for minimal CMake requirement:
cmake_minimum_required( VERSION 3.14 )
# cmake_minimum_required( VERSION 2.8 )

# Create a project:
project( Run3ModelGen )

add_subdirectory( SPheno-4.0.5beta )
# add_subdirectory( SPheno-4.0.5beta ${CMAKE_BINARY_DIR}/SPheno-4.0.5beta)

add_executable( helloworld helloworld.cxx )
add_dependencies( helloworld SPheno )