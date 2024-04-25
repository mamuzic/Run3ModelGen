# CMakeLists.txt for the Run3ModelGen code
atlas_subdir( Run3ModelGen )

atlas_add_executable( testworld testworld.cxx )
atlas_install_python_modules( python/*.py ) 
atlas_install_scripts( scripts/*.py )

# Add data directory with loose text files
atlas_install_generic( data/*
   DESTINATION data
)

add_dependencies( testworld SPheno )