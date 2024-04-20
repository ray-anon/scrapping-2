from bs4 import BeautifulSoup
import time
import requests

print("put some unfamiliar skill")
unfamiliar_skill = input('>')
print(f"filtering the unfamiliar skill {unfamiliar_skill}")
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=software&txtLocation="
def find_jobs():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text , 'lxml')
    jobs = soup.find_all("li" , class_="clearfix job-bx wht-shd-bx")
    for index , job in enumerate(jobs):
            skills = job.find("span" , class_="srp-skills").get_text().replace(' ' , '')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt' , 'w') as f:
                    published_date = job.find("span" , class_="sim-posted").span.get_text()
                    company_name = job.find("h3" , "joblist-comp-name").get_text().replace(' ' , '')
                    more_info = job.header.h2.a['href']
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Requried Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                    f.write(f"The Job was published  {published_date}")
                print(f"file save {index}")

if __name__ == '__main__':
     while(True):
          find_jobs()
          time_wait = 10
          print(f"waiting 10 minutes")
          time.sleep(60 * time_wait)