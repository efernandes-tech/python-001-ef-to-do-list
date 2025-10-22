<h1 align="center">
    <a href="#" alt="Python To-Do List">Python To-Do List</a>
</h1>

<h3 align="center">
    A simple, elegant command-line to-do list application with persistent storage
</h3>

<p align="center">
    <a href="https://github.com/efernandes-tech/python-001-ef-to-do-list/commits/main">
        <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/efernandes-tech/python-001-ef-to-do-list" />
    </a>
    <img alt="Repository size" src="https://img.shields.io/github/repo-size/efernandes-tech/python-001-ef-to-do-list">
    <a href="https://edersonfernandes.com.br">
        <img alt="made by @efernandes-tech" src="https://img.shields.io/badge/Made_by-@efernandes%E2%80%93tech-blue">
    </a>
    <img alt="Python version" src="https://img.shields.io/badge/python-3.x-blue.svg">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg">
</p>

<h4 align="center">
    Status: Finished
</h4>

<p align="center">
    <a href="#about">About</a> •
    <a href="#features">Features</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#project-structure">Project Structure</a> •
    <a href="#tech-stack">Tech Stack</a> •
    <a href="#license">License</a> •
    <a href="#author">Author</a>
</p>

## About

A lightweight, command-line to-do list application built with Python that helps you manage your tasks efficiently. This application provides a clean, interactive menu-driven interface for organizing your daily tasks with automatic persistence to ensure your data is never lost.

**Key Highlights:**
- 100% Python standard library - no external dependencies required
- Interactive command-line interface with numbered menu options
- Automatic data persistence using JSON format
- Simple task management with completion tracking
- Lightweight and fast execution

---

## Features

-   **View Tasks**: Display all tasks with their completion status at a glance
-   **Add Tasks**: Quickly add new tasks with descriptions
-   **Complete Tasks**: Mark tasks as done with a simple numbered selection
-   **Persistent Storage**: All tasks automatically saved to `tasks.json`
-   **User-Friendly Menu**: Clean, numbered menu interface for easy navigation
-   **Task Status Tracking**: Visual indicators show completed [x] vs pending [-] tasks
-   **Error Handling**: Graceful handling of invalid inputs and missing files

---

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- [Git](https://git-scm.com) - Version control system
- [Python 3.x](https://www.python.org/downloads/) - Python 3.6 or higher recommended

No additional Python packages or dependencies are required.

### Getting Started

```bash
# Clone this repository
git clone https://github.com/efernandes-tech/python-001-ef-to-do-list.git

# Access the project folder
cd python-001-ef-to-do-list

# Navigate to backend folder
cd backend

# Run the application
python to_do_list.py
```

Alternatively, you can use `python3` if you have both Python 2 and 3 installed:
```bash
python3 to_do_list.py
```

---

## Usage

When you run the application, you'll see an interactive menu with the following options:

```
=== To Do List ===
1. View tasks
2. Add task
3. Complete task
4. Exit

Choose an option:
```

### Menu Options

#### 1. View Tasks
Displays all your tasks with their current status:
```
Your tasks:
1. [-] Buy groceries
2. [x] Complete Python project
3. [-] Call the dentist
```
- `[-]` indicates a pending task
- `[x]` indicates a completed task

#### 2. Add Task
Prompts you to enter a new task description:
```
Enter task description: Learn Python advanced features
Added: Learn Python advanced features
```

#### 3. Complete Task
Shows your task list and lets you mark a task as complete:
```
Your tasks:
1. [-] Buy groceries
2. [-] Learn Python advanced features

Enter task number to complete: 1
Task completed!
```

#### 4. Exit
Saves all changes and closes the application:
```
Goodbye!
```

### Data Persistence

All tasks are automatically saved to `tasks.json` in the same directory as the application. The file is created automatically on first run and updated after each add or complete operation.

**Example JSON structure:**
```json
[
  {
    "description": "Buy groceries",
    "completed": true
  },
  {
    "description": "Learn Python advanced features",
    "completed": false
  }
]
```

---

## Project Structure

```
python-001-ef-to-do-list/
├── backend/
│   ├── to_do_list.py      # Main to-do list application
│   ├── hello.py           # Example: Hello World script
│   ├── greeting.py        # Example: Greeting script
│   └── tasks.json         # Task data storage (created at runtime)
├── support/               # Supporting files
├── .vscode/              # VS Code configuration
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
└── README.md            # This file
```

---

## Tech Stack

**Language:**
- [Python 3](https://www.python.org/) - Core programming language

**Standard Libraries Used:**
- `json` - For data serialization and storage
- Built-in file I/O operations

**Development Tools:**
- [Visual Studio Code](https://code.visualstudio.com/) - Code editor
- [Git](https://git-scm.com/) - Version control

**Data Storage:**
- JSON file format for lightweight, human-readable persistence

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Ideas for contributions:**
- Add task deletion functionality
- Implement task editing
- Add task priority levels
- Support for task categories/tags
- Add due dates for tasks
- Export tasks to different formats

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

<a href="https://github.com/efernandes-tech">
    <img style="border-radius: 50%;" src="https://github.com/efernandes-tech.png" width="100px;" alt="Ederson Fernandes" />
    <br />
    <sub><b>Ederson Fernandes</b></sub>
</a>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/efernandes-tech)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:efernandes.tech@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/efernandes-tech)

---

<p align="center">Made with Python by <a href="https://github.com/efernandes-tech">@efernandes-tech</a></p>
