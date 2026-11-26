from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="decodify",
    version="0.1.5",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "decodify=decodify.cli:main",
        ],
    },
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.official@gmail.com",
    description="Detect and decode (or encode) messages with 29 classic and modern encodings/ciphers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/decodify",
    keywords=[
        "encoding", "decoding", "cryptography", "cipher", "decode", "encoder",
        "decoder", "base64", "morse", "caesar", "vigenere", "jwt", "base58",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
)
