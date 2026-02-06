# Python Test Automation Learning

This repository tracks my structured learning of Python and pytest with a focus on test automation.
The goal is to build strong fundamentals and showcase a working automation setup.

---

## Objectives

1. Learn Python fundamentals required for test automation
2. Learn pytest and write automated tests
3. Build a small but real automation project
4. Follow professional project structure and best practices

---

## Repository Structure

```
basics/
```

Contains Python fundamentals practice scripts such as variables, data types, collections, and control flow.

```
utils/
```

Reusable helper functions and business logic used by tests.

```
tests/
```

Pytest-based test cases used to validate logic and practice testing concepts.

```
api_tests/
```

API automation tests using requests and pytest. This will be expanded gradually.

```
requirements.txt
```

List of Python dependencies required for this project.

```
venv/
```

Python virtual environment. This is local only and not committed to Git.

---

## Prerequisites

* Python 3.10 or above
* Git
* macOS or Linux

---

## Project Setup (Recommended)

Use this setup after cloning the repository.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Virtual Environment Setup (Manual / Learning Purpose)

Use this section if you want to understand how the environment and dependencies are created from scratch.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install pytest requests

# Save installed dependencies
pip freeze > requirements.txt

# Install dependencies from requirements file
pip install -r requirements.txt
```
