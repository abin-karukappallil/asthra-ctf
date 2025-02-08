# Flask Password Challenge

This is a simple Capture The Flag (CTF) challenge built using Flask. The goal is to find the correct password by predicting it. Once the correct password is entered, you will receive the flag.

## Difficulty: Easy

### Challenge Details:
In this challenge, the correct password has been hashed using the SHA-256 hashing algorithm. Your task is to predict the original password that, when hashed with SHA-256, matches the stored hash.

### Steps to Solve:
1. **Understand the Process**: The password is hashed using SHA-256. If you can figure out the original password that matches the hash, you will successfully solve the challenge.
2. **Predict the Password**: The hash is stored in the code (`password_hash`). Your task is to reverse engineer the hash and guess the correct password.
3. **Submit the Password**: Once you correctly predict the password, enter it in the input field on the webpage.
4. **Get the Flag**: If the password is correct, you will receive the flag 
