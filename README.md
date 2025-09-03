# Flask HTML Web & Database Project Starter

This is a starter project for you to use to start your Flask HTML web & database
projects.

It contains quite a lot of example code. You can use this to see how the various
parts of the project work, or you can delete it and start from scratch.

There are two videos to support:

* [A demonstration of setting up the project](https://www.youtube.com/watch?v=YStsRfMVx44&t=0s)
* [A walkthrough of the project codebase](https://www.youtube.com/watch?v=YStsRfMVx44&t=314s)

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv html-application-starter-venv

# Activate the virtual environment
; source html-application-starter-venv/bin/activate 

# Install dependencies
(html-application-starter-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Install the virtual browser we will use for testing
; playwright install
# If you encounter problems at this stage please contact your coach

# Create a test and development database
(html-application-starter-venv); createdb YOUR_PROJECT_NAME
(html-application-starter-venv); createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(html-application-starter-venv); open lib/database_connection.py

# Seed the development database
(html-application-starter-venv); python seed_dev_database.py

# Run the tests (with extra logging) - see below if you have any issues
(html-application-starter-venv); pytest -sv

# Run the app
(html-application-starter-venv); python app.py
# Now visit http://localhost:5001/emoji in your browser
```

<br>
<details>
  <summary>I get a <code>ModuleNotFoundError: No module named 'psycopg'</code></summary>
  <br>
If, after activating your <code>venv</code> and installing dependencies, you see this error when running <code>pytest</code>, please deactivate and reactivate your <code>venv</code>. This should solve the problem - if not, contact your coach.
</details>
<br>

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```
