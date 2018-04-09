# crypttool
This is my _little_ commandline tool which I wrote to learn Python. It performs various cryptographic and miscalleneous tasks.

## Instructions
1. Clone this repository.
2. ´cd cryptool´
3. ´chmod +x crypttool.py´
4. ´./crypttool.py´
----

## Features:
### ROT/Ceasar "Encryption"
* Allows rotating strings by a given amount, aswell as 'bruteforcing an encrypted string (when asked, type all)

### Hashing
* Can hash files (absolute paths) or strings
* Supports all algorithms from hashlib

### Translation
* Translate/convert strings between binary, decimal, octal, hex and ASCII

### Base64 Encoder/Decoder
* Guaranteed to work with strings and files (this is not a guarantee) 
* Uses a regex to automatically detect b64 strings
* Needs absolute Paths for files
* __currently broken (atleast for files)__

### String Reverser
* .syas ti tahw seod

### Fixed XOR
*  XORs two hex strings

### Single Byte XOR Bruteforce
* Takes a file or a string
* Tries to XOR decrypt with a key between 0 and 255, then returns the best matching results

### XOR Repeating Key
* I'm not sure anymore but I _think_ this doesn't work

### Zero-Width Strings
* Create binary-encoded zerowidth-strings to hide in your texts
* Or find and decode them!