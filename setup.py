#!/usr/bin/env python 
"""

 ModSecurity, http://www.modsecurity.org/
 Copyright (c) 2015 Trustwave Holdings, Inc. (http://www.trustwave.com/)

 You may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 If any of the files related to licensing are missing or if you have any
 other questions related to licensing please contact Trustwave Holdings, Inc.
 directly using the email address security@modsecurity.org.

 Author: Felipe "Zimmerle" Costa <fcosta at trustwave dot com>

"""

from distutils.core import setup, Extension
import os
import sys

possible_modsecurity_dirs = [
    "/usr/local/modsecurity/",
    "/usr/",
    "/usr/local/"
    ]

libraries_dir = [
    "lib/",
    "lib64/",
    "./"
    ]

headers_dir = [
    "include/",
    "headers/",
    "./"
    ]


def find_modsec():
    def find_library(modsec_dir):
        for i in libraries_dir:
            path = os.path.join(modsec_dir, i, "libmodsecurity.so")
            if os.path.isfile(path):
                return os.path.join(modsec_dir, i)
        return None

    def find_header(modsec_dir):
        for i in headers_dir:
            path = os.path.join(modsec_dir, i, "modsecurity", "modsecurity.h")
            if os.path.isfile(path):
                return os.path.join(modsec_dir, i)
        return None

    inc = lib = None
    for modsec_dir in possible_modsecurity_dirs:
        if not inc:
            inc = find_header(modsec_dir)
        if not lib:
            lib = find_library(modsec_dir)

    return (inc, lib)

inc_dir, lib_dir = find_modsec()


print("*** found modsecurity at:")
print("    headers: " + str(inc_dir))
print("    library: " + str(lib_dir))


if inc_dir == None or lib_dir == None:
    print("libModSecurity was not found in your system.")
    print("Make sure you have libModSecurity correctly installed in your system.")
    sys.exit(1)


#if os.path.isfile("modsecurity/_modsecurity_module.cc") == False:
#    print "Swig generated code was not found. Please run `make' first"
#    sys.exit(1)


extension_mod = Extension(
    "_modsecurity", [
        "modsecurity/modsecurity_wrap.cxx"
    ],
    libraries=["modsecurity"],
    swig_opts=['-Wextra', '-builtin'],
    library_dirs=[lib_dir],
    runtime_library_dirs=[lib_dir],
    include_dirs=[inc_dir, "."],
    extra_compile_args=["-std=c++11", "-Wno-maybe-uninitialized"]
)


setup(
    name         = "modsecurity",
    description  = 'Python Bindings for libModSecurity',
    author       = 'Felipe Zimmerle',
    author_email = 'felipe@zimmerle.org',
    url          = 'https://github.com/SpiderLabs/ModSecurity-Python-bindings',
    ext_modules  = [extension_mod],
    packages     = ['modsecurity'],
    classifiers  = [
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP'
    ]
 )


