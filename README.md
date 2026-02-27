# Python Test Automation Learning

This repository tracks my structured learning of Python and pytest with a focus on test automation.
The goal is to build strong fundamentals and showcase a working automation setup following professional practices.

---

## Objectives

1. Learn Python fundamentals required for test automation
2. Learn pytest and write automated tests
3. Build a small but real automation project
4. Follow professional project structure and best practices

---

## Repository Structure

basics/  
Contains Python fundamentals practice scripts such as variables, data types, collections, control flow, OOP, decorators, and more.

utils/  
Reusable helper functions and business logic used by tests.

tests/  
Pytest-based test cases used to validate logic and practice testing concepts.

api_tests/  
API automation tests using `requests` and `pytest`.

requirements.txt  
List of Python dependencies required for this project.

venv/  
Python virtual environment (not committed to Git).

---

## Prerequisites

- Python 3.10+
- Git
- macOS or Linux

---

## Project Setup

```bash
# Clone repository
git clone <your-repo-url>

# Navigate into project
cd <repo-name>

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt