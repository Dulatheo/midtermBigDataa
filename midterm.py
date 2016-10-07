from selenium import webdriver as w
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
from xlwt import Workbook



path_to_chromedriver = '/Users/dulat/Desktop/chromedriver' 
d = w.Chrome(executable_path = path_to_chromedriver)
d.get('https://vesti.kz/')


d.execute_script("window.scrollTo(0, 500)");
time.sleep(3)

element = WebDriverWait(d,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-top-news"]/div[@class="jspContainer"]/div[@class="jspPane"]/div[@class="single-item"]')))

try:
	print "found"

except selenium.common.exceptions.WebDriverException:
	print "not found"

link = d.find_elements_by_xpath('//*[@id="main-top-news"]/div[@class="jspContainer"]/div[@class="jspPane"]/div[@class="single-item"]/a')
links=[]
for a in link:
    print(a.get_attribute('href'))
    links.append(a.get_attribute('href'))


for i in range(0,len(links)):	
	d.get(links[i])
	d.execute_script("window.scrollTo(0, 700)");
	time.sleep(5)

	user = d.find_elements_by_xpath('//*[@id="comments_list"]/div[@class="comment"]/div[@class="comment-area"]/div[@class="comment-area-header"]/div[@class="comment-user"]')
	comment = d.find_elements_by_xpath('//*[@id="comments_list"]/div[@class="comment"]')
	#comment = d.find_elements_by_xpath('//*[@id="comments_list"]/div[@class="comment"]')

	users=[]
	comments=[]
	for a in user:
		users.append(a.text)
	for i in range(0,len(users)):
		print users[i]

	for a in comment:
		comments.append(a.text)
	for i in range(0,len(comments)):
		print comments[i]