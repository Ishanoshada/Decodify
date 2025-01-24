# setup.py
from setuptools import setup, find_packages

setup(
    name='decodify',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'decodify=decodify.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='An advanced package to detect encoding algorithms and decode messages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/decodify',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)