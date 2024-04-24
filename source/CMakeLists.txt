# Mandatory setting for minimal CMake requirement:
cmake_minimum_required( VERSION 3.14 )
# cmake_minimum_required( VERSION 2.8 )

# Create a project:
project( Run3ModelGen )

# # Build the library:
# add_library( MyLibrary SHARED lib/mylibrary.h lib/mylibrary.cxx )
# target_include_directories( MyLibrary PUBLIC ${CMAKE_SOURCE_DIR}/lib )

# # Build the executable:
# add_executable( MyExecutable app/myexecutable.cxx )
# target_link_libraries( MyExecutable MyLibrary )

# add_custom_target(
#    SPheno
#    COMMAND make
#    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/SPheno-4.0.5beta
# )

add_subdirectory( SPheno-4.0.5beta )

add_executable( helloworld helloworld.cxx )
add_dependencies(helloworld SPheno)

# target_link_libraries(helloworld SPheno)

target_link_libraries(helloworld SPheno)