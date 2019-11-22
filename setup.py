#!/usr/bin/env python
#
# Copyright (C) 2019 Matt Struble
# Licensed under the MIT License - https://opensource.org/licenses/MIT

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='gym_chrome_dino',
    version='0.0.1',
    author='Matt Struble',
    description='OpenAI Gym Chrome Dino',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mattstruble/gym-chrome-dino',
    packages=find_packages(),
    package_dir={'gym_chrome_dino':'gym_chrome_dino'},
    package_data={
        'gym_chrome_dino': ['*.png']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requries=[
        'selenium>=3.141.0',
        'gym>=0.15.4',
        'Pillow>=6.2.1',
        'numpy>=1.17.3',
        'opencv-python>=4.1.2.30'
    ],
    license='MIT',
    zip_safe=True
)