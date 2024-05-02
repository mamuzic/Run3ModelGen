# CMakeLists.txt for the SPheno directory

# Add a custom target to call make
add_custom_target(SPheno
    COMMENT "Building SPheno"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}/SPheno-4.0.5beta" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)