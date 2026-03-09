This project was done for a CSCI-213 - Linux Lab course. 

It consists of implementing a simple Caesar cipher where the main purpose is to become more familiar with using git and vim from a CLI, as is mostly seen in the Linux OS.

Sample usage includes:
1. git clone https://github.com/joezvan8/caesar-cipher
2. python3 mycipher [shift amount] < [source filename or line of text]
    > [destination file name]

N.B. using redirection ('<' and '>') is optional. However, when reading input
 directly from the terminal, extra steps are required to signal the end of file
(EOF) and have code run as intended.

Mac/Linux:
- After typing input, press Ctrl + D to signal EOF

Windows:
- After typing input, press Ctrl + Z followed by ENTER to signal EOF
  
