import requests
from bs4 import BeautifulSoup as bs

def get_jobs(keyword, location):
    url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location}&start='

    idx = 0
    count = 0
    unwantedWordsList = ['senior', 'lead', 'sr', 'staff', 'manager']
    company_set = set()

    while True:
        try:
            result = requests.get(url + str(count))
            soup = bs(result.content, "html.parser")

            job_titles = soup.find_all('h3')
            company_names = soup.find_all('h4')

            for title, company in zip(job_titles, company_names):
                company_name = str(company.text).lower()
                if company_name not in company_set:
                    company_set.add(company_name)
                    title_text = str(title.text).replace("\n", "").replace(" ", "").lower()
                    if all(word not in title_text for word in unwantedWordsList) and keyword in title_text:
                        idx += 1
                        print(f"{idx} {company.text.strip()} - {title.text.strip()}")
            
            count += 25
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    keyword = 'network'
    location = 'Canada'
    get_jobs(keyword, location)
