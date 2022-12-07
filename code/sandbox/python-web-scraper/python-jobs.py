import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# parse html code
soup = BeautifulSoup(page.content, "html.parser")

# find elements by id
results = soup.find(id="ResultsContainer")
# print(results.prettify())

# find elements by html class name
job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element)
#     print(company_element)
#     print(location_element)
#     print()

# extract text from html elements
# .strip() nullifies white-space
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()