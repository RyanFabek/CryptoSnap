# Steganosaurus - Steganography Applicaton

A simple application to hide text message data in images. Created with Python, PySide6 framework.  

# Table of Contents

* [Background](#background)
* [Technologies](#technologies)
* [Demo](#demo)
* [Setup](#setup)


# Background

## Introduction to Steganography

Steganography is a bit level technique used to concel data into another file or message. 

## Least Significant Bit (LSB) Technique

The simplest method to hide data within an file is to use the LSB Technique. 
In Crypto, the least significant bit of each RGB color value for each pixel is replaced with 
one bit of data from the inputted message. 

The resulting image will have insignificant changes to its pixels not noticable to the human eye.





# Technologies

This project is created with:
* Python 3.6
* Pyside6

# Setup


# Future Development

Future features to add:

* Discrete Fourier Transform Technique
* Support for other files (.mp4, .docx)

## License
MIT
