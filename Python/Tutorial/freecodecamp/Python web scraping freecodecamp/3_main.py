from bs4 import BeautifulSoup 
import requests 
import lxml 

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=' 
html_text = requests.get(url=url).text 

soup = BeautifulSoup(html_text, 'lxml') 
# print(soup.prettify())

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') 
for job in jobs: 
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') 
    skill = job.find('span', class_ = 'srp-skills').text.replace(' ', '') 
    publication_date = job.find('span', class_ = 'sim-posted').span.text 
    print(publication_date) 
    print(f'''
        company name : {company_name} 
        Required skill: {skill} 
        ''') 
    print(' ')


