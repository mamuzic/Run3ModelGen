# CMakeLists.txt for the softsusy directory

# Add a custom target to configure softsusy
add_custom_target(softsusy_configure
    COMMENT "Configuring softsusy"
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/configure
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

# Add a custom target to call make
add_custom_target(softsusy
    COMMENT "Building softsusy"
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}" ${CMAKE_MAKE_PROGRAM} -j1
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS softsusy_configure
)