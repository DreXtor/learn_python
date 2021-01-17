import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page():
	result = requests.get(URL)
	soup = BeautifulSoup(result.text, "html.parser")
	pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
	pages = pages[-2].get_text(strip = True)
	return int(pages)

def extract_job(html):
	
	title = html.find("div", {"class":"grid--cell fl1"}).find("h2").find("a")["title"]
	
	company,location = html.find("div", {"class":"grid--cell fl1"}).find("h3").find_all("span", recursive = False) 
	#리스트 안에있는 변수의 갯수를 정확히 알때 순서대로 변수명을 적어서 넣어줄수있다.
	#recursive = False 는 더 아래 카테고리로 들어가지 못하게 한다
	
	company = company.get_text(strip=True)
	location = location.get_text(strip=True)
	
	link_id = html["data-jobid"]
	link = f"https://stackoverflow.com/jobs/{link_id}"

	return {"title" : title , "company" : company , "location" : location , "link" : link}

def extract_jobs(pages):

	jobs = []

	for page in range(pages):
		print(f"Scrapping SO p{page}")
		result = requests.get(f"{URL}&pg={page}")
		soup = BeautifulSoup(result.text, "html.parser")
		results = soup.find_all("div", {"class":"-job"}) #클래스 안에 어떤 한 단어만도 찾을수있는것같다

		for r_results in results:
			#print(r_results["data-jobid"]) ##result가 있는곳에 'data-jobid'안에 있는 값을 가져온다
			job = extract_job(r_results)
			jobs.append(job)
	
	return jobs

def get_jobs():
	last_page = get_last_page()
	jobs = extract_jobs(last_page)
	return (jobs)
