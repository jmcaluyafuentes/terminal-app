# Terminal Application

## Term 1, Assignment 3

Web Development Accelerated
Coder Academy

## Purpose

Welcome to my Python project developed to showcase my knowledge and skills on Python Programming at Coder Academy. This is part of Term 1 assignment by developing terminal application.

## About the Application

The name of my app is "Pregnancy Tracker".

This application was inspired by my wife's pregnancy journey, as she was 9 weeks pregnant when I initially submitted the idea for approval. 

The purpose of this app is to provide helpful information related to pregnancy such as calculating the gestational age, estimate due date, countdown until due date and many more. Please refer to the Features section below for details.

## Github Repository

You can find the Github repository for my terminal app in [https://github.com/jmcaluyafuentes/terminal-app-T1A3](https://github.com/jmcaluyafuentes/terminal-app-T1A3).

## Preview of the application

Upon running the app, the console displays something like the below image as a preview of the application.

![Preview of the Pregnancy Tracker app](./markdown-images/app-screenshot-1.png)

## Development Plan

You can find the Trello board for my terminal app in [https://trello.com/b/qk7qA75c/t1a3-terminal-app](https://trello.com/b/qk7qA75c/t1a3-terminal-app).

Below is a snapshot of my Trello board during the initial stage of my terminal app development:

![Trello board at early stage](./markdown-images/trello-1-early-stage.png)

Below is a snapshot of the final stage:

![Trello board at early stage](./markdown-images/trello-2-final-stage.png)

The Trello board tool is very useful in organizing tasks, tracking progress, and managing the development process of my terminal app.

## Technology Stack

* Languages: Python 3 for the application logic and bash script for system-level interactions.  
* Project Type: Terminal application designed to run in a command-line interface (CLI).  
* IDE: Visual Studio Code (VS Code) used for writing code and debugging.  
* Version Control: Git for version and source control.  
* Repository Hosting: GitHub for hosting the Git repository remotely.  
* Package Manager: pip for managing Python packages and dependencies.  
* Operating System Compatibility: Developed for Microsoft Windows operating systems, utilizing the Windows Subsystem for Linux (WSL) for Linux compatibility.

## Code Styling Guide

* PEP8 Styling - guide and styling convention for writing code  
* PEP257 Styling - guide and styling convention for writing docstring

## Dependencies required by the application

#### Standard Library Modules

* sys: Provides access to system-specific parameters and functions.  
* textwrap: Offers convenient text wrapping and filling functionality.  
* datetime: Supports date and time manipulation and formatting.  
* csv: Facilitates reading and writing CSV (Comma-Separated Values)   files.

#### Third-Party Packages

* Colorama (version 0.4.6): Provides cross-platform colored terminal text.  
* Emoji (version 2.11.1): Allows easy usage of emoji characters in Python.  
* Pytest (version 8.2.0): A testing framework for Python projects.  

#### Pytest Dependencies (installed automatically with pytest)

* exceptiongroup (version 1.2.1)  
* iniconfig (version 2.0.0)  
* packaging (version 24.0)  
* pluggy (version 1.5.0)  
* tomli (version 2.0.1)  

## System and hardware requirements

### Prerequisites

* Make sure you have the latest version of Windows 10 or later.
* Enable the Windows Subsystem for Linux (WSL) on your Windows system.

#### Step 1: Install Windows 10

Install Windows 10 into your laptop or desktop. Check the latest version here https://learn.microsoft.com/en-us/windows/release-health/.

#### Step 2: Install Windows Terminal

Install Windows Terminal from Microsoft Store here https://apps.microsoft.com/detail/9n0dx20hk701?rtc=1&hl=en-au&gl=AU.

#### Step 3. Install Ubuntu 22.04 WSL

"Windows Subsystem For Linux (WSL) is a technology built into Windows that allows running a Linux operating system within it's own environment or container, side-by-side with Windows. This gives us the best of both worlds. (source: Coder Academy)"

1. Go to https://learn.microsoft.com/en-us/windows/wsl/install.

    Pre-requisite: You must be running Windows 10 version 2004 and higher.

2. Install WSL command

    "Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator", enter the wsl --install command, then restart your machine. (source: Microsoft)"

    In Powershell:

    ```
    wsl --install
    ```

3. Check the version of your Ubuntu

    ```
    lsb_release -rs
    ```

### Check your Python version

Guide is available here https://learn.microsoft.com/en-us/windows/python/web-frameworks#install-python-pip-and-venv.

"Ubuntu 18.04 LTS comes with Python 3.6 already installed, but it does not come with some of the modules that you may expect to get with other Python installations. We will still need to install pip, the standard package manager for Python, and venv, the standard module used to create and manage lightweight virtual environments. (source: Microsoft)"

#### Step 1. Open your Ubuntu terminal

Search 'Ubuntu' and click to open the terminal.

#### Step 2. You must have a Python3 version

1. Confirm if you already have Python3 by typing the command below and hit enter.

    ```
    python3 --version
    ```

    This should return your Python version number such as 3.12.10

2. Update your version in Python

    If you need to update your version of Python, first update your Ubuntu version by entering:

    ```
    sudo apt update && sudo apt upgrade
    ```

    Then update Python using:

    ```
    sudo apt upgrade python3
    ```

#### Step 3. Install pip

1. Enter the command below.

    ```
    sudo apt install python3-pip
    ```

2. Pip allows you to install and manage additional packages that are not part of the Python standard library.

## How to Install the Application

#### Step 1. Open the directory in your laptop or desktop

1. Open your Ubuntu terminal

2. Check your current directory

    ```
    pwd
    ```

3. Navigate to the directory where you want to install the Pregnancy Tracker app.

    ```
    cd ./path-to-your-folder
    ```

    Replace the 'path-to-your-folder' with the actual path of your directory.

#### Step 2. Clone my repository

1. Copy and paste below command into your terminal

    ```
    git clone git@github.com:jmcaluyafuentes/terminal-app-T1A3.git
    ```

#### Step 3. Run the Pregnancy Tracker app

1. Navigate to the project directory

    ```
    cd terminal-app-T1A3
    ```

2. Run the application by typing this command

    ```
    ./run_app.sh
    ```

    * This command will automatically install a virtual environment into your selected directory so that all packages in this app will not be installed to the global environment.

    * The command also automatically installs all dependencies (i.e., third-party packages) necessary to run the app as intended.

    * Lastly, the command will run the application.

#### Step 4. How to exit the app

1. To exit the app at anytime, type "QUIT" (case-insensitive) and press enter.  

2. Alternatively, you can use the 'CTRL + C' in your keyboard.

## Features of the Application

### 1. Pregnancy Information

Input: Date of last menstrual period entered by the user

Outputs:

a. Number of Weeks Pregnant: Calculates and displays the number of weeks pregnant based on the input date.

b. Trimester Information: Indicates whether the user is in her 1st, 2nd, or 3rd trimester of pregnancy.

c. Estimated Due Date: Provides an estimated due date based on the input date.

d. Countdown: Displays a countdown (in weeks and days) from current date to the estimated due date.

#### Run the app by entering the command "./run_app.sh" in the terminal. 

Please take note that every time you enter a command, hit enter so that the app can execute the command.

![Preview of the Pregnancy Tracker app](./markdown-images/app-screenshot-1.png)

Select 1 for Pregnancy Information:

![app snapshot](./markdown-images/feature1-1.png)

Enter the date of last menstrual period:

![app snapshot](./markdown-images/feature1-2.png)

Then the app will display the pregnancy information:

![app snapshot](./markdown-images/feature1-3.png)

Select 2 to go back to main menu.

### 2. Safety Information

In the early stage of development, this feature was previously named 'Precaution'.

However, I realized that the appropriate title is "Safety Information" because it encompasses a broader scope of ensuring the well-being and health safety of the pregnant user.

From the main menu, select 2 for Safety Information:

![app snapshot](./markdown-images/feature2-1.png)

### Sub-features:

#### 2.1 Food Safety Information

Input: Specific food item (e.g., Grapes) entered by the user

Output:

Determines whether the food is "Safe to Eat", "Not Safe to Eat" or other information relevant to food safety.

Select 1 for Food Safety:

![app snapshot](./markdown-images/feature2-2.png)

Enter the food:

![app snapshot](./markdown-images/feature2-3.png)

The app will display the food safety information:

![app snapshot](./markdown-images/feature2-4.png)

Select 2 to go back to Safety Information menu.

#### 2.2 Travel Safety Information

Input: Planned travel date and last menstrual period date entered by the user.

Outputs:

a. Estimated Weeks Pregnant on Travel Date: Calculates and displays the estimated number of weeks pregnant on the planned travel date.

b. Safety Advice: Provides tailored advice related to the planned travel, such as:
Whether it's safe to travel internationally.
Recommendations such as obtaining a medical certificate or precautions at airport security.
Activity Safety
This feature ensures that the user is aware of safe and appropriate activities during pregnancy.

Select 2 for the Travel Safety:

![app snapshot](./markdown-images/feature2-6.png)

Enter the last date of menstrual period:

![app snapshot](./markdown-images/feature2-7.png)

Enter the planned travel date:

![app snapshot](./markdown-images/feature2-8.png)

Select from the given questions related to travel safety:

![app snapshot](./markdown-images/feature2-9.png)

The app will display the travel safety information related to the question you selected:

![app snapshot](./markdown-images/feature2-10.png)

Select 2 to go back to Safety Information menu.

#### 3. Note-taking

Input: User-generated personal notes (e.g., milestone events, feelings).

Outputs:

a. Recording Notes: Notes are saved to a file, including the current date and time of entry.

b. Confirmation Message: The app confirms successful addition of the note to the file.

c. Viewing Recorded Notes: Users can view all past notes, providing a log of their pregnancy journey.

Select 3 for the note-taking:

![app snapshot](./markdown-images/feature3-1.png)

Select 1 to write your personal notes:

![app snapshot](./markdown-images/feature3-2.png)

Now, write your notes:

![app snapshot](./markdown-images/feature3-3.png)

The app will confirm the note was successfully recorded:

![app snapshot](./markdown-images/feature3-4.png)

Select 2 to go back to one menu up.

Then, select 2 to read your recorded note:

![app snapshot](./markdown-images/feature3-5.png)

The app will display your recorded notes.

![app snapshot](./markdown-images/feature3-6.png)

#### Guide to display the detailed instructions or exit the app

1. You can enter "INSTRUCTIONS" (case-insensitive) at any time in order to display the instructions.

![app snapshot](./markdown-images/instructions-1.png)

The app will then display the instructions.

![app snapshot](./markdown-images/instructions-2.png)

2. You can enter "QUIT" (case-insensitive) at any time to exit the app.

## Error Handling

### Invalid selection entered

If invalid selection number is entered, the app will display an error.

![app snapshot](./markdown-images/error-handling-1.png)

### Invalid date or format

If invalid date or format is entered, the app will display an error.

![app snapshot](./markdown-images/error-handling-2.png)

### Last menstrual period date is greater than the current date (this is invalid)

If the last menstrual period date is greater than the current date, the app will display an error.

![app snapshot](./markdown-images/error-handling-3.png)

### Travel date is less than the current date (this is invalid)

If travel date is less than the current date, the app will display an error.

![app snapshot](./markdown-images/error-handling-4.png)

### Safety information of food entered is not available

If safety information of food entered is not available, the app will display an error.

![app snapshot](./markdown-images/error-handling-5.png)

## References

The Royal Women's Hospital, Victoria Australia. "Food Safety During Pregnancy." Available at: https://thewomens.r.worldssl.net/images/uploads/fact-sheets/Food-safety-during-pregnancy.pdf

The Alphabetizer. "List of fruits and vegetables." Available at: https://alphabetizer.flap.tv/lists/list-of-fruits-and-vegetables.php

Better Health Channel. "Pregnancy and travel." Available at: https://www.betterhealth.vic.gov.au/health/healthyliving/pregnancy-and-travel

Greater Than. "10 Fun Activities for Pregnant Moms for All Stages of Your Pregnancy." Available at: https://drinkgt.com/blogs/news/activities-for-pregnant-moms

David Anson. Markdown lint MD007 - Unordered list indentation. Available at: https://github.com/DavidAnson/markdownlint/blob/v0.34.0/doc/md007.md

Colorama (version 0.4.6) package in 'pypi.org'. Available at: https://pypi.org/project/colorama/

Emoji (version 2.11.1) package in 'pypi.org'. Available at: https://pypi.org/project/emoji/

Pytest (version 8.2.0) package in 'pypi.org'. Available at: https://pypi.org/project/pytest/

Microsoft Website. How to install Linux on Windows with WSL. Available at: https://learn.microsoft.com/en-us/windows/wsl/install

Microsoft website. Get started using Python for web development on Windows. Available at: https://learn.microsoft.com/en-us/windows/python/web-frameworks#install-python-pip-and-venv


