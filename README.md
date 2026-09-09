# Password Checker

A command-line tool that checks whether a password has appeared in known data breaches. It uses the [Pwned Passwords](https://haveibeenpwned.com/Passwords) range API.

The password itself is never sent to the API: the script hashes it with SHA-1 and sends only the first five characters of that hash.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required package:

```bash
python -m pip install requests
```

## Run

```bash
python password_checker.py
```

Type the password when prompted and press Enter. Your input is hidden, so it does not appear in the terminal or command history.
