cmake_minimum_required(VERSION 2.8.12)
project(XboxInternals CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE SOURCES Velocity/XboxInternals/*.h Velocity/XboxInternals/*.cpp)

add_library(XboxInternals ${SOURCES})
target_include_directories(XboxInternals PUBLIC Velocity/XboxInternals)

if (MSVC)
    target_include_directories(XboxInternals PRIVATE Velocity/thirdparty/msvc/dirent/include)
    target_compile_definitions(XboxInternals PRIVATE _CRT_SECURE_NO_WARNINGS UNICODE _UNICODE WIN32 _WIN32 __WIN32)
endif()

target_link_libraries(XboxInternals PRIVATE ${CONAN_LIBS})
target_compile_definitions(XboxInternals PRIVATE XBOXINTERNALS_LIBRARY)
