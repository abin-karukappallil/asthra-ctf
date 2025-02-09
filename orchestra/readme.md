# CTF Challenge: Orchestra - Setup and Execution Guide

## Prerequisites
- Python 3.x installed on your system
- Basic knowledge of command line operations
- Text editor for viewing files

## Detailed Setup Instructions

### 1. Environment Setup
1. Clone or download the challenge files to your local machine
2. Ensure you have the following files in your directory:
   - `ctf_challenge.py`
   - `check_flag.py`
   - `readme.md`

### Difficulty Level
This challenge is designed for intermediate-level participants. It requires basic knowledge of Python scripting and text file manipulation.(requires only 5-10 mins)

### Steps to Solve

1. **Run the Challenge Script:**
    Execute the `ctf_challenge.py` script to generate the necessary files:
    ```bash
    python ctf_challenge.py
    ```

2. **Locate the Generated File:**
    After running the script, a file named `orchestra.txt` will be created in the same directory.

3. **Find the Flag:**
    Search through the `orchestra.txt` file to find the hidden flag. The flag format is typically `asthra{...}`.

### Hints
- Pay attention to any unusual patterns or strings within the `orchestra.txt` file.
- Use text search tools or scripts to help locate the flag more efficiently.

### Flag Submission

1. **Submit the Flag:**
    Once you have found the flag, submit it by running the `check_flag.py` script with the flag as an argument:
    ```bash
    python check_flag.py <your_flag>
    ```

2. **Example Submission:**
    ```bash
    python check_flag.py asthra{example_flag}
    ```

Good luck and happy hunting!
