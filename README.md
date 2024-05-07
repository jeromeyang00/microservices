**Flask App Setup Guide**

This guide will walk you through the process of setting up and running a Flask web application. Flask is a lightweight Python web framework that allows you to quickly build web applications.

### Prerequisites

Before you begin, make sure you have the following installed on your system:

1. Python 3.x
2. pip (Python package manager)

### Step 1: Clone the Repository

Clone the repository containing your Flask application code from a version control system like Git:

```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 2: Set up a Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a specific project without affecting the system-wide Python installation.

Create a virtual environment using the following commands:

```bash
python3 -m venv venv
```

This command creates a directory named `venv` which will contain the virtual environment.

### Step 3: Activate the Virtual Environment

Activate the virtual environment to isolate your Python environment:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

You'll know the virtual environment is activated when you see `(venv)` in your terminal prompt.

### Step 4: Install Dependencies

All required Python packages for the Flask app are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Flask App

Once the dependencies are installed, you can run the Flask application using the `flask run` command:

```bash
flask run
```

This command starts the Flask development server, and by default, your app will be accessible at the ip in the terminal
