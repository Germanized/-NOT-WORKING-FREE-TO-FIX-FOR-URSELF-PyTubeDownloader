# setup.py

from setuptools import setup, find_packages

setup(
    name='PyTubeDownloader',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pytube',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'pytubedownloader = PyTubeDownloader.test_script:main',
        ],
    },
)
