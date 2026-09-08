# IMPORTS

from playwright.sync_api import sync_playwright
import validators
import requests
from bs4 import BeautifulSoup

# URL INPUT AND VALIDATION

while True:
    url = input("Enter company URLs seperated by commas: ").strip()
    list_conv = url.split(",")
    valid_urls = []
    for url in list_conv:
        clean_url = url.strip()
        if clean_url.count("https://") == 1 or clean_url.count("http://") == 1:
            if validators.url(clean_url):
                print("Valid URL")
                valid_urls.append(clean_url)
            else:
                print("Invalid URL")
                while True:
                    retype_url = input(f"Please type {clean_url} again correctly").strip()
                    if validators.url(retype_url):
                        print("Valid URL")
                        valid_urls.append(retype_url)
                        break
                    else:
                        print(f"try typing {clean_url} again correctly")
        else:
            print("Multiple or no URL detected, please try again")
            break
    break

# KEYWORDS

keywords = [
    "career", "careers",
    "career opportunity", "career opportunities",
    "job", "jobs",
    "job opening", "job openings",
    "job opportunity", "job opportunities",
    "employment", "employment opportunity",
    "employment opportunities",
    "vacancy", "vacancies",
    "available positions",
    "open position", "open positions",
    "positions available",

    "join us", "join-us",
    "join our team", "join the team",
    "work with us", "work-with-us",
    "work for us",
    "we are hiring", "we're hiring",
    "hiring", "now hiring",

    "talent acquisition",
    "talent opportunities",
    "recruitment", "recruiting",
    "internship", "internships",
    "apprenticeship", "apprenticeships",
    "early career", "early careers",
    "graduate opportunities", "graduate jobs",
    "students and graduates",
    "students & graduates",

    "job application",
    "job applications",
    "submit application",
    "submit your application",
    "apply for this job",
    "apply for position",

    "human resources",
    "human resource",
    "people team",
    "people & culture",
    "people and culture",
    "people operations",
    "people ops",
    "employee relations",
    "talent team",
    "recruitment team",
    "recruiting team",

    "applicant", "applicants",
    "candidate", "candidates",

    "contact us",
    "contact-us",
    "contact information",
    "contact details",
    "email us",
    "our contact"
]

# SEARCH PAGE TEXT

def contains_keywords(soup):
    page_text = soup.get_text().lower()
    page_match = False
    for keyword in keywords:
        if keyword in page_text:
            page_match = True
            break
    return page_match

# SEARCH HTML ATTRIBUTES

def contains_attributes(soup):
    attribute_list = []
    for tag in soup.find_all():
        attribute_list.append(tag.attrs)
    attribute_match = False
    for attributes in attribute_list:
        for value in attributes.values():
            if isinstance(value, list):
                for item in value:
                    for keyword in keywords:
                        if keyword in item.lower():
                            attribute_match = True
                            break
                    if attribute_match:
                        break
            elif isinstance(value, str):
                for keyword in keywords:
                    if keyword in value.lower():
                        attribute_match = True
                        break
            if attribute_match:
                break
        if attribute_match:
            break
    return attribute_match

# CHECK EACH WEBSITE

for url in valid_urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        if contains_keywords(soup) or contains_attributes(soup):
            print(f"Relevant careers/HR information found: {url}")
        else:
            # SECOND CHECK:
            # Open the website in a browser so JavaScript can execute.
            with sync_playwright() as p:

                browser = p.chromium.launch()

                page = browser.new_page()

                page.goto(url)

                rendered_html = page.content()

                rendered_soup = BeautifulSoup(rendered_html, "html.parser")

                if contains_keywords(rendered_soup) or contains_attributes(rendered_soup):

                    print(f"Relevant careers/HR information found: {url}")

                else:
                    print(f"No relevant careers/HR information found: {url}")

                browser.close()

    elif response.status_code == 403:
        print(f"Access denied: {url}")

    else:
        print(f"Website returned status code {response.status_code}: {url}")