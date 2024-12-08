# Importing BeautifulSoup libraries in order to use their methods.
from bs4 import BeautifulSoup

#This line of code opens the HTML document, to read, and saves it as a variable called html_file
with open("home.html", "r") as html_file:
    #This line of code places all of the file contents into a varibale called content.
    content = html_file.read()
    # This line of code creates a varibale called soup and stores a formated version of the content variable for better parsing
    soup = BeautifulSoup(content, "lxml")
    # This line of code finds all of the div elements with the class name 'card' and
    # stores them in the variable called course_cards.
    course_cards = soup.find_all("div", {'class':'card'})
    for course in course_cards:
        # This line of code extracts the elements in the course_cards variable 
        # and stores the text of first h5 elements in the course_name variable
        course_name = course.h5.text
        # This line of code extracts only the last word of the text in the 'a' element 
        # and stores it in the variable called course_price. to change where to split you change the (" "). 
        # This is so that we can just isolate the price. 
        course_price = course.a.text.split(" ")[-1]
        # This line of code prints the course_name and its price
        print(f"{course_name} cost: {course_price}")
        
        #Extra lines that might be valuable.
        '''
    # This line of code takes the formated version of the content "soup" 
    # and looks for all of the tags called "h5" and it stores it in a variable called courses_html
    courses_html_tags = soup.find_all("h5")
    # This line of code creates a for loop that iterates through the list of elements returned by 
    # courses_html_tags and prints the text content using course.text.
    for course in courses_html_tags:
        print(course.text)
    '''
    