import requests
from bs4 import BeautifulSoup
url = 'http://www.mca.gov.in/mcafoportal/showCheckLLPName.do'

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

page = requests.get(url, headers=agent)

soup = BeautifulSoup(page.text,'html.parser')

y=soup.find('input',{'id':'name1'})
print(y) 
z=soup.find('input',{'id':'checkLLPName_0'})
print(z)
