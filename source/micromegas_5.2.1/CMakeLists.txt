# CMakeLists.txt for the micromegas directory

# Add a custom target to call make
add_custom_target(micromegas
    COMMENT "Building micromegas"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}/micromegas_5.2.1" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS micromegas_MSSM
)

# Add custom target for MSSM subdir
add_custom_target(micromegas_MSSM
    COMMENT "Building micromegas/MSSM"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}/micromegas_5.2.1/MSSM" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}"/MSSM"
)