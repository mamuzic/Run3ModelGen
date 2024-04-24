# CMakeLists.txt for the Run3ModelGen code
atlas_subdir( Run3ModelGen )

atlas_add_executable( testworld testworld.cxx )
add_dependencies( testworld SPheno )