import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"

r_request = requests.get(URL)

# 마지막 페이지의 값을 구하여 'list_job_page()'에 전달한다
def extract_so_pages():

	soup = BeautifulSoup(r_request.text, "html.parser")
	pagination = soup.find("div", {"class": "s-pagination"}).find_all('a') #'s-pagination'안에 모든 'a'를 찾는다
	
	last_pages = pagination[-2].get_text(strip=True)
	# 'pagination' 리스트 안에 뒤에서 두번째(마지막에 '...'과 'next'가 있었음)값을 'last_pages'에 저장한다.

	return int(last_pages)

# job = { title, company, location, link} 를 구한다.
def job_card(html): #'html'의 값은 'list_job_page()'에서 가져온다
	
	job_title = html.find('a')['title'] #'job_title'을 구한다

	company = html.find('span').string 
	#'company'를 구한다. find_all이 아닌 find를 써서 첫번째'span' 값만 구할수있었다
	if company is not None:
		company = company.strip()
	else:
		company = 'None'
		
	location = html.find('span',{'class':'fc-black-500'}).string #'location'을 구한다
	if location is not None:
		location = location.strip()
	else:
		location = 'None'
	
	links= html.find('a')['href'] #'link'를 구한다. 'jobid'를 나타내는 class로 짧고 쉽게 구할수있었는데 'html'의 범위를 너무 좁게 잡아서 지저분한 링크주소가 되었다
	link = f"https://stackoverflow.com/{links}"

	return (f"'title' : {job_title} ,'company' : {company} , location : {location} , 'linki' : {link}")



def list_job_page(pages):
	
	list_jobs = [] # for문 밖에있어야 리셋되지않고 데이터가 축적된다.

	for page in range(pages): #페이비순서대로 'loop'한다. extract_so_pages()의 리턴값을 int형으로 수정하여 range()를 사용하였다.
		print(page)
		r_request = requests.get(f"{URL}&pg={page+1}")
		soup = BeautifulSoup(r_request.text, "html.parser")
		job_info = soup.find_all('div', {'class' : 'grid--cell fl1'}) #범위를 너무 좁게 설정하여 링크가 조금 지저분해졌다.

		for info in job_info: # 각 페이지의 html data를 job_card()에 전달 후 그 값을 리스트로 저장한다.
			so_job_list = job_card(info)
			list_jobs.append(so_job_list)

	return (list_jobs)


def get_jobs(): # 이 모듈을 실행시킨다

	last_page = extract_so_pages()
	list_job = list_job_page(last_page)
	
	return (list_job)
