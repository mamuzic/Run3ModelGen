# CMakeLists.txt for the Run3ModelGen code
atlas_subdir( Run3ModelGen )

atlas_add_executable( testworld testworld.cxx )
# atlas_install_python_modules( python/*.py ) 
atlas_install_scripts( scripts/*.py )

add_dependencies( testworld SPheno )