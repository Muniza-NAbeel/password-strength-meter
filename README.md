# Password Strength Meter by Muniza Nabeel

🔐 This is a **Password Strength Meter** built using **Streamlit**. It helps users check the strength of their passwords and gives suggestions on how to improve them to ensure they are more secure.

## Features

- **Password Strength Meter**: A tool that evaluates the strength of a password and provides a score based on:
  - Length of the password
  - Inclusion of uppercase and lowercase characters
  - Inclusion of digits (0-9)
  - Inclusion of special characters (e.g., !@#$%^&*)

- **Suggestions for Improvement**: If the password is weak or moderate, the app provides suggestions on how to improve its strength.

- **Common Weak Passwords Blacklist**: The app checks if the entered password is among the most commonly used and insecure passwords (e.g., "password123", "123456").

- **Random Strong Password Generator**: If the entered password is weak or moderate, the app provides a randomly generated strong password.

## Requirements

To run this project locally, you will need to have **Python 3.x** installed, along with the following packages:

- `streamlit`
- `re` (regular expressions)
- `random` (for generating random passwords)
- `string` (for creating password strings)

