# NOTE

This project was outdated by the **pymodsecurity** project (https://github.com/actions-security/pymodsecurity). At **pymodsecurity** you can get a more stable and feature complete bindings for libmodsecurity.

# Introduction

The following are a set of Swig generated Python bindings for libmodsecurity. These bindings will allow users to utilize the exposed libmodsecurity interfaces directly from python, without the use of ctypes.

# Compilation

Although these are python scripts DO NOT use setup.py to compile this. Instead, one should use the Makefile in order to compile these. This can be done by typing 'make'. Be aware that the Python development headers and Swig are required to build this package. These can be obtained on RHEL via 'dnf install swig python-devel' 



