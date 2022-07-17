from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://boss.az/vacancies?search%5Bcategory_id%5D=38').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='results-i')

    for index, job in enumerate(jobs):
        title = job.find('h3', class_='results-i-title').text
        company = job.find('a', class_='results-i-company').text
        salary = job.find('div', class_='results-i-salary-and-link').find('div', class_='results-i-salary salary').text.replace(' - ','-')
        with open(f'posts/{index}.txt', 'w') as f:
            f.write(f'{title} : {company} : {salary}')
            print('File saved')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)



