# HENNGE Admission Challenge: Simple Explanation

This document explains the HENNGE Admission Challenge in simple terms for your future reference.

## What was the Challenge?
The HENNGE Admission Challenge was a coding test given by HENNGE to evaluate technical skills. It had three main parts, or "missions," that needed to be completed.

## Why was this Challenge Given?
This challenge helps HENNGE understand how well a candidate can:
*   **Solve problems creatively**: Especially when faced with unusual rules (like no loops).
*   **Understand and follow strict technical specifications**: This is important for real-world software development.
*   **Work with security concepts**: Like generating one-time passwords (TOTP).
*   **Interact with APIs**: Sending data to a server correctly.
*   **Manage code**: Using Git and GitHub for version control.

## What Types of Missions were There?

### Mission 1: The Coding Puzzle
*   **What it was**: You had to write a program that reads numbers and calculates a special sum. The main trick was that you **could not use common programming loops** (like `for` or `while`).
*   **Why it was tricky**: This forced the use of a technique called **recursion**, where a function calls itself. It tests how you think about problems differently.

### Mission 2: Sharing Your Code Securely
*   **What it was**: You had to share your Mission 1 code on GitHub, but not publicly. It had to be a **secret Gist**.
*   **Why it was important**: This shows you can use GitHub correctly and understand how to keep sensitive code private when needed.

### Mission 3: Talking to a Server (API)
*   **What it was**: You needed to send a special message (a JSON payload) to a HENNGE server. This message included your Gist link and email.
*   **The big challenge here**: Before sending the message, you had to create a **one-time password (TOTP)**. This password changes every 30 seconds and uses a specific, strong encryption method (HMAC-SHA-512).
*   **Why it was important**: This tests your ability to work with web APIs, understand security protocols (like TOTP and HTTP Basic Authentication), and implement cryptographic functions accurately. It's a very practical skill for secure online systems.

In summary, the challenge was designed to test a range of skills from basic programming logic to advanced security and API interaction, all while following very specific rules.
