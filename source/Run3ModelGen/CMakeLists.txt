# CMakeLists.txt for the Run3ModelGen code
atlas_subdir( Run3ModelGen )

# Execute pip install command
execute_process(
    COMMAND pip install pyslha
    RESULT_VARIABLE PIP_INSTALL_RESULT
)

if(PIP_INSTALL_RESULT)
    message(FATAL_ERROR "Failed to install pyslha Python package using pip")
endif()

atlas_add_executable( testworld testworld.cxx )
atlas_install_python_modules( python/*.py ) 
atlas_install_scripts( scripts/*.py )

# Add data directory with loose text files
atlas_install_generic( data/*
   DESTINATION data
)

add_dependencies( testworld SPheno )