# 🐍 Learn Object Oriented Programming — Boot.dev

Welcome to my repository for the **Learn Object Oriented Programming** course, part of the [Boot.dev Backend Developer Path](https://www.boot.dev/paths/backend). This repository serves as a record of my progression, code solutions, unit testing setups, and notes as I build core backend programming foundations in Python.

---

## 📌 About the Course

This course covers the principles of object-oriented design and clean code architectures required for real-world software engineering:

- [x] **Ch 1.** Clean Code
- [x] **Ch 2.** Classes
- [ ] **Ch 3.** Encapsulation
- [ ] **Ch 4.** Abstraction
- [ ] **Ch 5.** Inheritance
- [ ] **Ch 6.** Polymorphism

---

## ⚙️ Local Development & Environment Setup

This repository is configured to mirror the automated testing and task submission environment of Boot.dev locally using VS Code.

### Prerequisites
- **Python 3.10+**
- **Git**
- **VS Code**

---

### First-Time Setup Instructions

Follow these steps to configure your local workspace when cloning this repository onto a new machine (macOS or Linux):

#### 1. System Package Requirements (Linux / Ubuntu / Debian)
On Debian-based systems like Ubuntu or Linux Mint, the standard Python virtual environment package is separated from the default installation. Install it system-wide before creating virtual environments:

```bash
sudo apt update && sudo apt install python3-venv -y
```
*(On macOS, Python's `venv` module comes pre-installed).*

#### 2. Create and Activate the Virtual Environment
Navigate to the project root directory and set up a workspace virtual environment named `.venv`:

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
# macOS / Linux:
source .venv/bin/activate
```

#### 3. Install Required Dependencies
Install `pytest` inside the activated virtual environment:

```bash
pip install -r requirements.txt
```

---

### 🛠️ VS Code Integration & Shortcuts

The repository includes a `.vscode/tasks.json` configuration to run exercises directly within VS Code.

#### Register Keyboard Shortcuts (`keybindings.json`)
To enable Boot.dev keybindings in VS Code:
1. Press `Cmd + Shift + P` (macOS) or `Ctrl + Shift + P` (Linux/Windows).
2. Search for **Open Keyboard Shortcuts (JSON)**.
3. Add the following configuration:

```json
[
  {
    "key": "cmd+enter",
    "command": "workbench.action.tasks.runTask",
    "args": "Boot.dev: Run",
    "when": "editorTextFocus"
  },
  {
    "key": "shift+cmd+enter",
    "command": "workbench.action.tasks.runTask",
    "args": "Boot.dev: Submit",
    "when": "editorTextFocus"
  }
]
```
*(On Linux/Windows, replace `cmd+enter` with `ctrl+enter` and `shift+cmd+enter` with `ctrl+shift+enter`).*

#### Workflow Shortcuts
* **Run (`Cmd + Enter` / `Ctrl + Enter`):** Runs non-submission test cases (`pytest -m "not submit"`) for rapid debugging.
* **Submit (`Shift + Cmd + Enter` / `Ctrl + Shift + Enter`):** Executes all tests including Boot.dev submission edge cases (`pytest`).

---

## 👤 Profile & Progress

- **GitHub Profile:** [@mauriciodaiki](https://github.com/mauriciodaiki)
- **Path:** Backend Developer Path (Boot.dev)
- **Previous Completed Track:** [Learn Python for Beginners](https://www.boot.dev/courses/learn-python-beginners)