# Career & HR Page Checker

A simple Python tool that checks company webpages for career and HR-related information.

## What It Does

When applying for jobs, you may have a large number of company websites to go through. Some companies have a careers page, some have job or recruitment information somewhere on their website, and some have no careers-related information at all.

This program is designed as a quick first check.

It accepts multiple company URLs and searches each webpage for career, job, hiring, recruitment, HR, and contact-related keywords.

If nothing is found in the initial webpage, the program performs a second check using Playwright, which opens the website in a browser and allows JavaScript-rendered content to load.

The purpose is simply to help determine **which websites may be worth opening and checking manually**.

## How It Works

1. Enter one or more company URLs, separated by commas.
2. The program validates the URLs.
3. It requests each webpage using `requests`.
4. BeautifulSoup parses the HTML.
5. The program searches the webpage text and HTML attributes for relevant keywords.
6. If nothing is found, Playwright opens the webpage in Chromium so JavaScript can execute.
7. The rendered webpage is checked again.
8. The program reports whether relevant careers/HR information was found.

## Installation

The program uses Python and the following additional packages:

* `validators`
* `playwright`
* `requests`
* `beautifulsoup4`

The packages I installed specifically for this project were:

```bash
pip install validators
pip install playwright
```

Playwright also requires its browser binaries to be installed:

```bash
playwright install
```

### Note

`BeautifulSoup` is imported from the `beautifulsoup4` package:

```python
from bs4 import BeautifulSoup
```

The program also uses the `requests` package:

```python
import requests
```

If these packages are not already installed in your Python environment, they will need to be installed before running the program.

## Running the Program

Run the Python file:

```bash
python career_hr_checker.py
```

You will be asked to enter company URLs separated by commas.

For example:

```text
https://www.apple.com/careers/in/, https://stripe.com/careers, https://example.com
```

## Example Output

```text
Valid URL
Valid URL
Valid URL

Relevant careers/HR information found: https://www.apple.com/careers/in/
Relevant careers/HR information found: https://stripe.com/careers
No relevant careers/HR information found: https://example.com
```

If a website refuses the request:

```text
Access denied: https://example.com
```

## Limitations

This is a **general-purpose, keyword-based webpage checker**, not a highly accurate careers or HR detection system.

It is intentionally simple and is mainly useful as a first-pass check when you have a large number of company websites to go through.

For example, if you have 50 companies you are considering applying to, instead of manually opening every website, you can run them through the program first and see which ones contain careers, jobs, hiring, recruitment, HR, or related information.

The results should be treated as an indication of whether a website is **worth opening and checking manually**, rather than as a definitive answer.

The program:

* Only checks the webpage URLs provided by the user.
* Does not crawl the rest of the company's website.
* Does not extract specific job listings.
* Does not extract HR email addresses.
* Does not identify the exact careers page.
* May miss information that is not present in the webpage HTML or rendered content.
* May produce false positives because it relies on keyword matching.
* Cannot access websites that refuse the request or require authentication/CAPTCHA.
* Does not attempt to bypass website access restrictions.

## Purpose

This project was created primarily as a **learning and portfolio project** to practice:

* Python
* Input validation
* HTTP requests
* HTML parsing
* Web scraping
* Working with HTML attributes
* Keyword-based searching
* Browser automation
* JavaScript-rendered webpages
* Using external Python libraries

It is not intended to replace manually checking a company's website.
