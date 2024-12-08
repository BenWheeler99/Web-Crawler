from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text

soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('div', { 'class' : "srp-job-bx"})

for job in jobs:
    
    job_title = job.find("h3").text.replace(' ', '')

    skills = job.find('div', { 'class' :'srp-keyskills'}).text

    published_date = job.find('span', { 'class' : "posting-time"}).text.replace(' ', '')
    
    print(f'''
    Job Title: {job_title}
    Skills: {skills}
    Published Date: {published_date})''')
          
    print(" ")




