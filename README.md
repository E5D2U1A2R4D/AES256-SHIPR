# AES256-SHIPR
Prerequisites:
Python:

Make sure you have Python installed on your computer. You can download Python from the official website: Python Downloads.
During the installation, ensure that you check the option to add Python to your system's PATH.
pip (Python Package Installer):

pip is a package installer for Python. It is usually included with Python installations.
If you don't have it, you can install it by following the instructions here: Installing pip.
Required Python Libraries:
-----------------------------------------------------------------------------------------------------------
You need to install the required external libraries using pip. Open a terminal or command prompt and run the following commands:

bash
Copy code
-- pip install cryptography
-- pip install colorama
Running the Script:
Download the Script:
--------------------------------------------------------------------------------------------------------------
Copy the provided Python script and save it with a .py extension, for example, encryption_script.py.
Navigate to Script Directory:

Open a terminal or command prompt and navigate to the directory where you saved the script using the cd command. For example:
bash
Copy code
-- cd path/to/directory
Run the Script:
--------------------------------------------------------------------------------------------------------------
Execute the script by running the following command:
bash
Copy code
-- python encryption_script.py
If you're on a system where Python 3 is the default, you might use python3 instead of python:
bash
Copy code
-- python3 encryption_script.py
Follow On-Screen Instructions:
---------------------------------------------------------------------------------------------------------------

The script will provide instructions and prompts for various actions (encryption, decryption, etc.).
Enter the desired commands or follow the instructions on the screen.
Notes:
If you encounter any issues during installation, ensure that your Python and pip installations are up-to-date.
If the colorama library is not installed, the script attempts to install it automatically at the beginning.
-----------------------------------------------------------------------------------------------------------------
=================================================================================================================
The provided Python script is designed to create a command-line interface for basic encryption and decryption operations using the cryptography library. It allows users to interactively encrypt and decrypt messages using either the Advanced Encryption Standard (AES) or the Triple Data Encryption Standard (Triple DES) algorithms.

Here's a breakdown of the script's main functionalities:

Encryption:

Users can input a message they want to encrypt.
They can choose between two encryption methods: AES (Advanced Encryption Standard) and Triple DES (Data Encryption Standard).
The script generates encryption keys and Initialization Vectors (IVs) based on the chosen method.
The user's message is then encrypted using the selected algorithm and displayed.
Decryption:

Users can input an encrypted message.
The script decrypts the message using the previously generated keys and algorithms.
The decrypted message is displayed.
Displaying Original Unencrypted Word:

Users can set and display an original unencrypted word. This is stored in the variable original_word.
Terminal Clearing:

Users can clear the terminal to enhance the readability of the console.
Help and Exit Options:

Users can access a help menu that displays available actions.
They can exit the program at any time.
Colored Output:

The script uses the colorama library to provide colorful and stylized output in the terminal, making the user interface more visually appealing.
The script operates in a loop, allowing users to perform multiple actions sequentially without restarting the program. It provides a straightforward way for users to experiment with encryption and decryption using different algorithms and messages in a command-line environment.
