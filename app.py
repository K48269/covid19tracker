import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template


def Tracker_information():
    URL='https://www.mygov.in/covid-19'
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    samples=soup.find_all("strong",{"class":"testing_count"})
    total_caseEs=samples[0].get_text()
    yesterday=samples[1].get_text()
    title = soup.find_all("span", {"class": "icount"})
    total_cases=title[0].get_text()
    active_cases=title[1].get_text()
    discharged_cases=title[2].get_text()
    deaths=title[3].get_text()
    recov=soup.find("div",{"class":"per_block"})
    print(recov.get_text())
    return total_caseEs,yesterday,total_cases,active_cases,discharged_cases,deaths,recov


app = Flask(__name__)

@app.route('/')
def hello_world():
    sdf=Tracker_information()
    print(sdf)
    return render_template('indez.html',samples=sdf[0],ason=sdf[1],confirme=sdf[2],revd=sdf[4])

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)


