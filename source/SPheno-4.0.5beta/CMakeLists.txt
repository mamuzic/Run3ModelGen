# CMakeLists.txt for the SPheno directory
atlas_subdir( SPheno-4.0.5beta )

# Add a custom target to call make
add_custom_target(SPheno
    COMMAND ${CMAKE_COMMAND} -E env "CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}/SPheno-4.0.5beta" ${CMAKE_MAKE_PROGRAM}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Building SPheno"
)

atlas_add_alias( SPheno ${CMAKE_BINARY_DIR}/SPheno-4.0.5beta/bin/SPheno )