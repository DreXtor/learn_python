import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}&radius=25&start=0"

def extract_indeed_pages():
	
	result = requests.get(URL)

	soup = BeautifulSoup(result.text, "html.parser")

	pagination = soup.find("div", {"class": "pagination"})

	links = pagination.find_all('a')
	pages = []
	for link in links[:-1]:
		pages.append(int(link.string))

	max_page = pages[-1]

	return max_page


def information_jobs(html):
		job_title = html.find("h2", {"class" : "title"}).find("a")["title"]
		company = html.find("span", {"class" : "company"})
		anchor_company = company.find("a")
		if anchor_company is not None:
			company = anchor_company.string
		else:
			company = company.string
		company = company.strip()

		location = html.find("span", {"class" : "location"}).string
		link = html["data-jk"]
		apply_link = f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={link}&tk"

		return {"title" : job_title , "company" : company , "location" : location , "link" : apply_link}


def last_indeed_jobs(last_pages):
	
	jobs = []
	
	for page in range(last_pages):
		result = requests.get(f"{URL}&start={page*LIMIT}")
		soup = BeautifulSoup(result.text, "html.parser")
		results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
		
		

		for card in results:
			job = information_jobs(card)
			jobs.append(job)

	return(jobs)

def get_jobs():
	last_page = extract_indeed_pages()
	list_job = last_indeed_jobs(last_page)
	
	return list_job