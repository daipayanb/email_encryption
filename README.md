# Email Encryption
Repository of code for sending and encrypting email using Python v3.4 .
Due to RSA algorithm's limits, it uses AES to encrypt the message and subject of the email.
It creates a .PEM for every new user login.
And then RSA to Encrypt the AES Key. The basic UI has been created with PyQt5.
PyCrypto and Crypto libraries have been used. Visual Studio was used as the primary IDE.
This code has still some flaws. Any kind of contribution would be greatly appreciated.

# Getting Started
Run GUI.py. This will open the UI.
Enter Your details. This creates your password file.
Enter sender's email ID, receiver's email ID, subject and message.
You'll be then prompted for the password.
Click on send.

copy-paste the encrypted-message of the email from the browser into the app.
enter your emailID and click on decrypt.
the decrypted text will appear in the Decrypted-text section

# Prerequisites
Python v3.4
Packages:
PyQt5
PyCrypto
rsa
ast
base64

# Installation
download the files from https://sourceforge.net/projects/rsev1/
Extract them and import them to your IDE
make sure you have all the packages installed. 
If not some can be installed using PIP or easy-install.

#1

Example of a commit daipayan@f03a5f2766fe27033a0cda29e3b0e8f3b7d4ff3



