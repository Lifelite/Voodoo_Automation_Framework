# Introduction

TODO: provide a concise readme file!  :) 

This is intended to be a "do all" automation framework, utilizing Playwright and possibly other other frameworks as it grows.
Primary language currently is Python, though I do intend to expand to JS and potentially other languages, depending on how crazy I want to get!

This project will likely split at some point, one to be a playwright implementation template, 
to showcase proper examples of how the framework can (and maybe should) be structured.



## Installation
Some day this will be implemented as a package, but for now this code can cloned. 

### Prerequisits
[Python](https://www.python.org/downloads/)
Download python for your specific OS and follow instructions for adding python to PATH in your system's environment variables.

After having Python setup install Poetry

```bash
pip install poetry
```
Same as python, assure you have your environment variables configures correctly for your OS's CLI

### Install Dependencies
```bash
poetry lock
```
This will install all of the necessary dependencies to run VooDoo

## Usage

To write tests, create a folder for your website/application/etc. in the __Tests__ folder
In that folder create a python file ie: "my_voodoo_test.py"

Example of a relatively simple login test:
```python
from Helpers.VD_Connectors import Database
from Helpers.Voodoo import *
from Helpers.MySQL import Query



def test_herokuapp_login(page: Page):

    # Initialize Classes

    validate = Validate(page)
    interact = Interact(page)
    q = Query(Database)

    # Retrieve Test Data (in this scenario, credentials) using MySQL

    creds = q.credentials("herokuapp")
    uname = creds[0]
    upassword = creds[1]

    # Navigate to the page

    interact.navigate_to_url("https://the-internet.herokuapp.com/login")

    # Quick Page Validation

    validate.title("The Internet")
    validate.text("Login Page")

    # Fill in the login fields and submit

    interact.fill_by_label("Username", uname)
    interact.fill_by_label("Password", upassword)
    interact.click_button("Login")

    # Validate Login was Successful

    validate.id("flash")
```

## Contributions and Usage

Currently I am just working on this by myself, but eventually I will be open to input and contributions.  
This is a current work in progress, so I don't believe this is quite for others to start utilizing, but I'm always open to feedback!

## License

[MIT](https://choosealicense.com/licenses/mit/)
