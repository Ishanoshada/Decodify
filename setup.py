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
    author='Ishan Oshada',
    author_email='ishan.kodithuwakku.offical@gmail.com',
    description='An advanced package to detect encoding algorithms and decode messages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/decodify',
    keywords=['encoding', 'decoding', 'cryptography', 'cipher', 'decode', 'encoder', 'decoder', 'base64', 'hash'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta'
    ]
)