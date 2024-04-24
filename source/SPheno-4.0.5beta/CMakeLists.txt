# CMakeLists.txt for the SPheno directory

# Add a custom target to call make
add_custom_target(SPheno
    COMMAND ${CMAKE_MAKE_PROGRAM}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Building SPheno"
)