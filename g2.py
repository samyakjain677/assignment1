import requests
from bs4 import BeautifulSoup
url='http://cms.nic.in/ncdrcusersWeb/servlet/util.GetDistricts'
url2='http://cms.nic.in/ncdrcusersWeb/login.do?method=caseStatus'
url3='http://cms.nic.in/ncdrcusersWeb/servlet/util.GetCaseStatus'
method='GetDistricts'
method2='GetCaseStatus'
headers ={"User-Agent":	
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
def OnlineCaseStatus(fano,state='select',district='select'):
	session=requests.session()
	r2=requests.get(url2,headers=headers)
	data2=r2.text
	soup2=BeautifulSoup(data2,'html.parser')
	dd2=soup2.find_all('select',{'class':'selBox'})
	distCode='0'
	stateCode='0'
	for i in dd2:
		ss2=i.find_all('option')
		for j in ss2:
			if state==(j.get_text()):
				qq2=j.get('value')
				stateCode=qq2
	Params={'method':method,'scode':stateCode,'type':'part'}
	r=requests.post(url,data=Params,allow_redirects=True,headers=headers)
	data=r.text
	soup=BeautifulSoup(data,'html.parser')
	dd=soup.find_all('detail')
	for i in dd:
		ss=i.find_all('distname')
		for j in ss:
			if district==(j.get_text()):
				qq=i.find('distid').get_text()
				distCode=qq
	caseidin=stateCode+'/'+distCode+'/'+fano
	Params3={'caseidin':caseidin,'distCode':distCode,'fano':fano,'loginType':'B','method':method2,'stateCode':stateCode}
	r3=requests.post(url3,data=Params3,allow_redirects=True,headers=headers)
	data=r3.text
	soup=BeautifulSoup(data,'html.parser')
	Detail=soup.find_all('detail')
	case=[]
	for row in Detail:
		elem={}
		cells=row.find_all("desc")
		if len(cells)>0:
			elem=cells[0].get_text().rstrip()
		case.append(elem)
	return case
print("press 1 for NCDRC")
print("press 2 for State Commission ")
print("press 3 for District Forum")
c=input()
if c=='1':
	caseNo=input("caseNo:")
	case=OnlineCaseStatus(caseNo);
elif c=='2':
	state=input("State:")
	caseNo=input("caseNo:")
	case=OnlineCaseStatus(caseNo,state);
elif c=='3':
	state=input("State:")
	district=input("District:")
	caseNo=input("caseNo:")
	case=OnlineCaseStatus(caseNo,state,district);
print("");
print("CaseNo. :"+ case[0]);
if case[0]!="Sorry. No Details Available, Please Check Case No.":
	print("filingDate :"+ case[1]);
	print("filedIn :"+ case[2]);
	print("Complainant :"+ case[3]);
	print("Respondent :"+ case[4]);
	print("NextHearing :"+ case[5]);
	print("CaseStage :"+ case[6]);
	print("AttachedOrLowerCourt :"+ case[7]);
	print("ApplicationFiled :"+ case[8]);
	print("DateOfDestruction :"+ case[9]);
	print("RBTDetails :"+ case[10]);


	



