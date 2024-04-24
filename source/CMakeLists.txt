# Mandatory setting for minimal CMake requirement:
cmake_minimum_required( VERSION 3.21 )
# cmake_minimum_required( VERSION 2.8 )

# Create a project:
project( Run3ModelGen VERSION 25.2 )

# Pick up a local version of the AtlasCMake code if it exists:
find_package( AtlasCMake QUIET )

# Find the project that we depend on:
find_package( AnalysisBase 25.2 REQUIRED )

# Set up CTest:
atlas_ctest_setup()

# Set up a work directory project:
# atlas_project( Run3ModelGen ${AnalysisBase_VERSION}
#     USE AnalysisBase ${AnalysisBase_VERSION}
# )
atlas_project( Run3ModelGen 0.1.0 )

# Add subdirectory for SPheno (not necessary with ATLAS!)
# add_subdirectory( SPheno-4.0.5beta )
# # add_subdirectory( SPheno-4.0.5beta ${CMAKE_BINARY_DIR}/SPheno-4.0.5beta)

# Set up the runtime environment setup script(s):
lcg_generate_env( SH_FILE ${CMAKE_BINARY_DIR}/${ATLAS_PLATFORM}/env_setup.sh )
install( FILES ${CMAKE_BINARY_DIR}/${ATLAS_PLATFORM}/env_setup.sh
   DESTINATION . )

# Set up CPack:
atlas_cpack_setup()