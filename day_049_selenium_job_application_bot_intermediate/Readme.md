# LinkedIn Job Search Automation

A Python automation project that demonstrates interacting with a modern web application using Selenium.  
The script logs into LinkedIn, performs a job search, and extracts job titles from the results.

## Overview

This project was built to practice browser automation techniques on a real-world website.  
It automates the initial steps of a job search workflow and collects information from the results page.

The script:

- Opens a browser session
- Logs into LinkedIn
- Performs a job search
- Waits for job listings to load
- Extracts and prints job titles from the results

The focus of this project is learning reliable automation patterns for dynamic web pages.

## Features

- Automated login workflow
- Job search automation
- Dynamic element handling using explicit waits
- Extraction of job titles from job cards
- Demonstrates practical Selenium automation techniques

## Tech Stack

- Python
- Selenium WebDriver

## What This Project Demonstrates

- Working with dynamic web content
- Locating elements using CSS selectors
- Handling asynchronous page loading with explicit waits
- Structuring a small automation project with Python classes

## Note

This project intentionally **does not automatically apply to jobs**.  
The goal was to practice automation and data extraction rather than submit applications programmatically.

Many large platforms implement anti-automation protections, so this project focuses on interacting with the job search interface and retrieving information from the results page.

## How to run

`python main.py`

## Configuration

This project uses environment variables to store login credentials for linkedIn. See the `.env.dist` file
