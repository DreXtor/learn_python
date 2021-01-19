from flask import Flask, render_template#html을 가져올수있다.

app = Flask("SuperScrapper")

# @(데코레이터)는 요청받으면 바로 아래에 있는 함수만을 호출한다.
@app.route("/") #/는 웹의 root를 나타낸다.(ex: google.com == google.com/)
#인자로 url 뒤에 붙는 root를 입력해준다.
#</input>는 입력되는 input에 맞는 db를 불러온다? 
def home():
	return render_template("job_search.html")#templates에 있는 job_search.html을 가져온다.

app.run(host = "0.0.0.0")