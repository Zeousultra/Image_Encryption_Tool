# Image Encryption Tool

## Description
This project implements a simple image encryption and decryption tool using XOR-based pixel manipulation. It is written in Python and uses the `Pillow` and `NumPy` libraries for image processing. This tool allows you to securely encrypt an image and later decrypt it using the same key.

## Features
- Encrypt and decrypt images using XOR operation.
- Works on RGB images.
- User-friendly command-line interface.
- Input validation for secure and smooth user experience.

## Installation
Ensure Python 3 is installed on your system. Then clone the repository:

```bash
git clone https://github.com/Zeousultra/Image_Encryption_Tool.git
cd Image_Encryption_Tool
```

Install the required libraries:

```bash
pip install pillow numpy
```

## Usage
Run the script with:

```bash
python3 image_encryption.py
```

### Sample Workflow
```
Image Encryption Tool (XOR-based)
Do you want to (e)ncrypt or (d)ecrypt an image? e
Enter the input image path: input.png
Enter the output image path: encrypted.png
Enter the encryption/decryption key (integer 0–255): 123
Encrypted image saved to encrypted.png
```

### Notes
- Use the same key for both encryption and decryption.
- Ensure input image exists and is in RGB format.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Author
Developed by [Zeousultra](https://github.com/Zeousultra) as part of PRODIGY_CS_02.

