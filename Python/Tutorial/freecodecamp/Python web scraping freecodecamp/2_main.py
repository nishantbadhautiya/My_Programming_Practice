from bs4 import BeautifulSoup 
import lxml 

with open('index.html', 'r') as html_file: 
    content = html_file.read() 

    soup = BeautifulSoup(content, 'lxml') 
    # print(soup.prettify()) 

    course_cards = soup.find_all('div', class_ = 'card') 
    for course in course_cards:
        # print(course.h5.text) 
        # print(course.a.text.split()[-1]) 

        print(f"{course.h5.text} costs {course.a.text.split()[-1]}") 


