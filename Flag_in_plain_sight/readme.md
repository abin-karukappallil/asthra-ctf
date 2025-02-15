# Flag in Plain Sight - CTF Challenge

Welcome to the "Flag in Plain Sight" Capture The Flag (CTF) challenge! In this challenge, your task is to find the hidden flag that is cleverly concealed within this repository. 

## Challenge Description

The flag is hidden in plain sight within the files of this repository. Your goal is to locate the flag by carefully examining the contents of the files. Pay close attention to details, as the flag could be hidden in various forms such as comments, metadata, or even within the text itself.

## Getting Started

1. Clone the repository to your local machine:
    ```sh
    git clone <repository_url>
    ```
2. Navigate to the repository directory:
    ```sh
    cd Flag_in_plain_sight
    ```
3. Start exploring the files to find the hidden flag.

## Rules

- Do not use automated tools to search for the flag.
- Work individually to solve the challenge.
- Do not share the flag or any hints with others.

## Submission

Once you have found the flag, submit it through the designated submission portal.

## Confidential

<details>
<summary>Solution (Confidential)</summary>

To solve this CTF challenge, follow these steps:

there is a hidden string which is encrypted in ceaser cipher shift 3 ,we can find the encrypted flag in the inspect section of the html body element,so take the encrypted flag and decrypt it in the ceaser cipher shift 3.and submit yaaay

Example:
```sh
cat assets/hidden_file.txt | base64 --decode
```

The flag is: `asthra{hidden_inside_HTML}`

</details>

Good luck and happy hunting!
