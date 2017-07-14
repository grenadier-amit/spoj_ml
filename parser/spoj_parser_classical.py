import re
import csv
import urllib.request
from bs4 import BeautifulSoup

global_row=[]
#########################################################################################################################################


def func_parse3(prb_rank_url):
	global global_row
	page=urllib.request.urlopen(prb_rank_url)
	soup=BeautifulSoup(page,"lxml")
	table_body=soup.find('tr',class_='lightrow')
	arr=[]
	for row in table_body.find_all('td'):
		arr.append(row.text)
	user_ac=arr[0]
	submissions=arr[1]
	acccepted=arr[2]
	wrong_answer=arr[3]
	cerror=arr[4]
	rterror=arr[5]
	tle=arr[6]
#	print(user_ac,submissions,acccepted,wrong_answer,cerror,rterror,tle)

	global_row.append(user_ac)
	global_row.append(submissions)
	global_row.append(acccepted)
	global_row.append(wrong_answer)
	global_row.append(cerror)
	global_row.append(rterror)
	global_row.append(tle)


#########################################################################################################################################


def func_parse2(prb_url):
	global global_row
	page=urllib.request.urlopen(prb_url)
	soup=BeautifulSoup(page,"lxml")
	table_body_all=soup.find_all('tbody')
	table_body=None
	for table_body in table_body_all:pass
	if table_body:
		table_href=table_body.find_all('a',href=True)
		author=table_href[0].contents[0]
		cluster=table_href[1].contents[0]
		global_row.append(author)
		global_row.append(cluster)
#		print(author,cluster)
		table_body=table_body.find_all('td')
		pr_date=table_body[3].text
		pr_date=re.search(r'(\d+)',pr_date)
		pr_date=pr_date.group(1)
		time_limit=table_body[5].text
		if re.search(r'(\d+\.\d+)',time_limit):
			time_limit=re.search(r'(\d+\.\d+)',time_limit)
			time_limit=time_limit.group(1)
		else:
			time_limit=re.findall(r'\d+',time_limit)[0]

		source_limit=table_body[7].text
		source_limit=re.findall(r'\d+',source_limit)[0]
		memory_limit=table_body[9].text
		memory_limit=re.findall(r'\d+',memory_limit)[0]
		global_row.append(pr_date)
		global_row.append(time_limit)
#		print(pr_date,time_limit)
		global_row.append(source_limit)
		global_row.append(memory_limit)
#		print(source_limit,memory_limit)


#########################################################################################################################################


def func_parse(row):
	global global_row
	global_row=[]
	prb_url_td=row.find(align=True)
	prb_url_href=prb_url_td.find("a")['href']
	prb_title   =prb_url_td.find("a").contents[0]   
	prb_url="http://www.spoj.com"+prb_url_href
	global_row.append(prb_title)
	print(prb_title)
	text_success=row.find('span',class_='text-success')
	if not text_success:
		text_success=row.find('span',class_='text-danger')
	thumbs_up=0
	thumbs_down=0
	if text_success:
		if 'title' in text_success.attrs:
			success=text_success['title']
		else:
			success=""
		if success:
			thumbs=re.findall(r'\d+',success)
			thumbs_up=thumbs[0]
			thumbs_down=thumbs[1]
	global_row.append(thumbs_up)
	global_row.append(thumbs_down)
#	print(thumbs_up, thumbs_down)
	prb_rank=row.find_all('td',class_='text-center')[2]
	prb_status=row.find('td',class_='text-right')

	prb_rank_url=prb_rank.find("a")['href']
	prb_rank_url="http://www.spoj.com"+prb_rank_url
	value=0

	prb_rank=prb_rank.find("a")
	rank=prb_rank['title']
	value=re.findall(r'\d+\.\d+',rank)
	if(value):
		value=value[0]
	else:
		value=re.findall(r'\d+',rank)[0]
	ac_percent=prb_status.find("a").contents[0]
	global_row.append(value)
	global_row.append(ac_percent)
#	print(value,ac_percent)

	difficulty=row.find('div',class_='progress problem-list-progress')
	implementation=0
	concept=0
	if 'title' in difficulty.attrs:
		difficulty=difficulty['title']
		if difficulty:
			difficulty=re.search(r'(Implementation)(.*?)(Concept)(.*)',difficulty)
			if difficulty:
				implementation=difficulty.group(2)
				concept=difficulty.group(4)
				implementation=re.search(r'(\d+)(.*?)',implementation)
				concept=re.search(r'(\d+)(.*?)',concept)
				implementation=implementation.group(1)
				concept=concept.group(1)
	global_row.append(implementation)
	global_row.append(concept)
#	print(implementation,concept)
	func_parse2(prb_url)
	func_parse3(prb_rank_url)

#	print("\n\n")


#########################################################################################################################################

myfile=open("spoj_metadata.csv",'w')
spoj_page_url="http://www.spoj.com/problems/classical/sort=0,start="

page_no=0

while page_no<=71:
	flag=page_no*50
	print(flag)
	spoj_cur_page_url=spoj_page_url+str(flag)
	page=urllib.request.urlopen(spoj_cur_page_url)
	soup=BeautifulSoup(page,"lxml")
	#print(soup)
	table_body=soup.find('tbody')
	#print(table_body)
	for row in table_body.find_all("tr"):
		func_parse(row)
		wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
		wr.writerow(global_row)
	page_no+=1
	print("\n\n")


#########################################################################################################################################	