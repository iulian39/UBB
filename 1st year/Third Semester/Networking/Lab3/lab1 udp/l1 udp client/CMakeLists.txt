cmake_minimum_required(VERSION 3.8)
project(l1_udp_client)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c)
add_executable(l1_udp_client ${SOURCE_FILES})