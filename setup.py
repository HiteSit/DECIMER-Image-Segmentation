#!/usr/bin/env python

import setuptools
import platform
import subprocess

# Determine the base TensorFlow package
if (
    platform.processor() == "arm" or platform.processor() == "i386"
) and platform.system() == "Darwin":
    tensorflow_os = "tensorflow-macos==2.10.0"
else:
    # Check for CUDA-compatible GPU
    try:
        # Use nvidia-smi if available to check for CUDA support
        if subprocess.run(["nvidia-smi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            tensorflow_os = "tensorflow[and-cuda]>=2.12.0,<=2.15.0"
        else:
            tensorflow_os = "tensorflow-cpu==2.12.0"
    except FileNotFoundError:
        tensorflow_os = "tensorflow-cpu==2.12.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decimer_segmentation",
    version="1.4.0",
    author="Kohulan Rajan",
    author_email="kohulan.rajan@uni-jena.de",
    maintainer="Kohulan Rajan",
    maintainer_email="kohulan.rajan@uni-jena.de",
    description="DECIMER Segmentation - Extraction of chemical structure depictions from scientific literature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kohulan/DECIMER-Image-Segmentation",
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=[
        tensorflow_os,
        "numpy>=1.20.0,<1.25.0",
        "scikit-image>=0.2.0",
        "pillow",
        "opencv-python",
        "matplotlib",
        "IPython",
        "scipy",
        "pandas",
        "notebook",
        "rdkit",
        "datamol",
        "scikit-image"
    ],
    package_data={"decimer_segmentation": ["mrcnn/*.*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
