# HENNGE Admission Challenge Solution

This repository contains the solution for the HENNGE Admission Challenge.

## Mission 1: Python Solution
The core logic is implemented in `main.py`. 
- **Requirements**: Python 3.13+
- **Constraints**: No `for`/`while` loops, no list/set/dict comprehensions. Used recursion for processing.
- **Functionality**: Calculates the sum of powers of four of non-positive integers from the input test cases.

## Mission 2: Secret Gist
The solution has been published as a secret gist as required.
- **Gist URL**: [https://gist.github.com/aryanbarde80/1ce8320c838ef24691848652e86e49c4](https://gist.github.com/aryanbarde80/1ce8320c838ef24691848652e86e49c4)

## Mission 3: API Submission
The mission was completed by generating a TOTP (RFC 6238) using HMAC-SHA-512 and submitting the required JSON payload to the HENNGE API.
- **Submission Script**: `submit_mission3.py`
- **TOTP Logic**: `totp_generator.py`

## How to Run
To test the Mission 1 solution:
```bash
python3 main.py < input.txt
```

To run the Mission 3 submission script (requires `requests` library):
```bash
python3 submit_mission3.py
```
