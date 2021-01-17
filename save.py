import csv

def save_to_file(jobs):
	file = open("jobs.csv", mode = "w") #open하려는 파일이 없으면 만들어준다.
	writer = csv.writer(file)
	writer.writerow(["title", "company", "location", "link"]) #리스트로 만들어줘야 칸마다 깔끔하게 들어간다.
	for job in jobs:
		writer.writerow(list(job.values()))


	return