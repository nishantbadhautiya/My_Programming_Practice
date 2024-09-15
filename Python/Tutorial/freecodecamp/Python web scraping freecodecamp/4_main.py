from bs4 import BeautifulSoup 
import requests 
import time 
import lxml 

print('Enter the skills you are not familiar with (comma seperated): ') 
unfamiliar_skills = input('>') 


def get_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=' 
    html_text = requests.get(url=url).text 

    soup = BeautifulSoup(html_text, 'lxml') 
    # print(soup.prettify())

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') 
    for index, job in enumerate(jobs): 
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '') 
        if unfamiliar_skills not in skills: 
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') 
            publication_date = job.find('span', class_ = 'sim-posted').span.text 
            more_info = job.header.h2.a['href']
            with open(f'posts/{index}.txt', 'w') as fp:
                fp.write(f'More info: {more_info}')
                fp.write(f'Publication Date is: {publication_date}') 
                fp.write(f"Company Name: {company_name.strip()}") 
                fp.write(f'Required Skill: {skills.strip()}') 
                fp.write(' ')


while True: 
    get_jobs() 
    wait_time = 10
    print(f"Waiting for {wait_time} ....")
    time.sleep(wait_time) 

