from bs4 import Beautifulsoup
import requests
import time

print('Put some skill that you are not familiar with')
Unfamiliar_Skill = input('>')
print(f'Filtering out {Unfamiliar_Skill}')

def Find_Jobs():
    Html_Text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python+Developer&txtLocation=').text
    soup = BeautifulSoup(Html_Text,'lxml')
    Jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(Jobs):
        Published_Date = Jobs.find('span',class_='sim-posted').span.text
        if few in Published_Date:
            Company_Name = Jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
            Skills = Jobs.find('span',class_='srp-skills').text.replace(' ','')
            More_Info = Jobs.header.h2.a['href']
            if Unfamiliar_Skill not in Skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name:{Company_Name.strip()}\n")
                    f.write(f"Required Skills:{Skills.strip()}\n")
                    f.write(f"More Info:{More_Info.strip()}\n")
                print(f"File saved:{index}")


if __name__== "__main__":
    while True:
        Find_Jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait=60)



