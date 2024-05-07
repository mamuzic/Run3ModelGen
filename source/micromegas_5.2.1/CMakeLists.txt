# CMakeLists.txt for the micromegas directory

# Copy files from source directory to build directory
message("Setting up micromegas build directory")
file(COPY ${CMAKE_CURRENT_SOURCE_DIR} DESTINATION ${CMAKE_BINARY_DIR}/micromegas_5.2.1 FILES_MATCHING PATTERN "*")

# Add custom target for micomegas
add_custom_target(micromegas_base
    COMMENT "Building micromegas"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1
)

# Add a custom target for micomegas/MSSM
add_custom_target(micromegas
    COMMENT "Building micromegas/MSSM"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM
    DEPENDS micromegas_base
)