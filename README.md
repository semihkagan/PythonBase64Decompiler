# Base64 Decoder - Python Script 🎉

![Base64 Decoder](https://raw.githubusercontent.com/semihkagan/PythonBase64Decompiler/main/assets/main.png)

This project is a simple Python script designed to decode Base64 encoded text and display the decoded content. It also features batch decoding of Base64 strings from a file. 📄

## Features ✨

- Decode Base64 code entered by the user.
- Batch decode Base64 strings from a specified file.
- Ignore comment lines (`//`) during the decoding process.
- Simple and user-friendly interface. 😊

## Usage 🚀

### 1. File Creation 📂

When the program runs, an `input.txt` file is automatically created with some sample Base64 strings. You can add your own Base64 strings to this file for batch decoding.

### 2. Decoding Base64 Strings 🔍

When the program runs, it will prompt the user to enter either a Base64 code or a filename.

- If the user enters a Base64 code, the code is decoded and the result is displayed on the screen.
- If the user enters a filename, all Base64 strings in the file are decoded and displayed.
- If nothing is entered, the program defaults to using the `input.txt` file.

### 3. Commands 💻

- **Enter a Base64 code:** Directly decode a Base64 string.
- **Enter a filename:** Decode all Base64 strings in the specified file.
- **exit/close/stop:** Terminates the program.

## Example Usage 💡

```
> python Main.py

Base64 Decoder - Github : semihkagan

Enter Base64 Code or,
Enter the name of the input file or path:
> aGVsbG8gd29ybGQ=
---------------------------------------
Decoded string [0]: hello world

Decoding Successfully! , total decompiled texts(1).
Please press enter to continue...
```

```
> python Main.py

Base64 Decoder - Github : semihkagan

Enter Base64 Code or,
Enter the name of the input file or path:
> input.txt
---------------------------------------
Decoded string [0]: hello world

Decoding Successfully! , total decompiled texts(1).
Please press enter to continue...
```
