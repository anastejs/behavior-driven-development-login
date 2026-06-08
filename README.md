# BDD Login Test Suite
### Playwright + Python + Behave

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.60-2EAD33?style=flat&logo=playwright&logoColor=white)
![Behave](https://img.shields.io/badge/Behave-1.3.3-FF6B35?style=flat)
![BDD](https://img.shields.io/badge/Methodology-BDD-8A2BE2?style=flat)

---

A hands-on pet project exploring **Behavior-Driven Development (BDD)** testing methodology using **Playwright** for browser automation and **Behave** as the Python BDD framework. 

The project covers automated login flow testing with scenarios written in human-readable **Gherkin** syntax — bridging the gap between business requirements and test automation.

---

## 🗂️ Project Structure

```
behavior-driven-development-login/
├── features/
│   ├── login.feature           # Gherkin scenarios
│   └── steps/
│       └── login_steps.py      # Step definitions (Python)
├── requirements.txt
└── README.md
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/anastejs/saucedemo-playwright-tests.git
cd behavior-driven-development-login

# Create and activate virtual environment
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass    # (optional) I needed this
venv\Scripts\activate       

# Install dependencies
pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
# Run all scenarios
behave

# Run a specific feature file
behave features/login.feature

# Run with verbose output
behave --no-capture

```

---

### 💡 What is BDD?

> **Behavior-driven development (BDD)** — is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

> **Behavior-Driven Development** — это подход к разработке (+ стиль описания тестов), в котором поведение системы описывается на понятном человеку языке (почти как сценарии), а затем эти сценарии автоматизируются как тесты.

**Key idea:** tests read like plain English (or any human language), making them understandable to the whole team — not just developers and QA engineers.

> **Behave** — это BDD framework для Python, он запускает тесты, читает .feature файлы (Gherkin), связывает шаги с Python-функциями, управляет execution flow

---

### Формат сценариев (язык Gherkin), пример:

```gherkin
Feature: Login
    Identify the visitor and store their data

  Scenario: Successful login
    Given user opens login page
    When user enters valid username and password
    And clicks login button
    Then user should be redirected to dashboard
```

Each `Given / When / And / Then` step maps to a Python function in `steps/login_steps.py` that drives the browser via Playwright.