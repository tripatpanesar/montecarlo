#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:50:55 2023

@author: tripatpanesar
"""

from setuptools import setup, find_packages

setup(
    name = 'montecarlo',
    version = '1.0.0',
    url = 'https://github.com/tripatpanesar/montecarlo.git',
    author='Tripat Panesar',
    author_email = 'tp6mt@virginia.edu',
    description = 'For DS5100',
    packages = find_packages(),    
    install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)