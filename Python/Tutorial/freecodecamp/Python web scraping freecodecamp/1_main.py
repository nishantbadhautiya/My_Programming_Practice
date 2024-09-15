from bs4 import BeautifulSoup 
import lxml

with open('index.html', 'r') as html_file: 
    content = html_file.read() 
    # print(content) 

    soup = BeautifulSoup(content, 'lxml') 
    # print(soup.prettify())

    course_html_tags = soup.find_all('h5') 
    # print(course_html_tags) 

    for course in course_html_tags: 
        # print(course)
        print(course.text) 
        


