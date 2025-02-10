# Flask Double Hashing CTF Challenge

This is a Capture The Flag (CTF) challenge where the goal is to find the correct password by reversing a double hashing process. The flag can be obtained once the password is correctly cracked.

## Difficulty: Medium

### Challenge Details:
In this challenge, the correct password has been hashed twice:
1. First, the password is hashed using **SHA-256**.
2. Then, the resulting SHA-256 hash is hashed again using **MD5**.

The **double-hashed password** (the MD5 hash of the SHA-256 hash) is given in the **hashed_password.txt** file and you need to reverse the process to figure out the original password.