# CMakeLists.txt for the micromegas directory

# Copy files from source directory to build directory
message("Setting up micromegas build directory")
file(COPY ${CMAKE_CURRENT_SOURCE_DIR} DESTINATION ${CMAKE_BINARY_DIR}/micromegas_5.2.1 FILES_MATCHING PATTERN "*")

# Create empty directories in the binary directory (needed by micromegas to build)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/MSSM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Z3IDM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Z3IDM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Z3IDM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/NMSSM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/NMSSM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/NMSSM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Z4IDSM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Z4IDSM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Z4IDSM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/lib)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/SingletDM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/SingletDM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/SingletDM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/mdlIndep/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/mdlIndep/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/mdlIndep/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CalcHEP_src/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CalcHEP_src/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CalcHEP_src/work/batch_results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CalcHEP_src/lib)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CPVMSSM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CPVMSSM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/CPVMSSM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/Packages/LanHEP/test/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/LLL_scalar/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/LLL_scalar/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/LLL_scalar/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/ZpPortal/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/ZpPortal/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/ZpPortal/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/LHM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/LHM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/LHM/work/tmp)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/IDM/work/so_generated)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/IDM/work/results)
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/micromegas_5.2.1/IDM/work/tmp)

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