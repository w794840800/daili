from selenium import webdriver
broswer = webdriver.PhantomJS()
url = 'http://www.doudoubird.com:8080/ddn_app/toBaiduIndex'
broswer.get(url)
broswer.set_window_size(1120, 550)
broswer.implicitly_wait(5)
#print(broswer.page_source)
text = broswer.find_element_by_id("kw")
text.send_keys('python')
#button = broswer.find_element_by_id("searchBt")
#button.submit()
broswer.save_screenshot('test.png')

print(broswer.title)

path = broswer.find_elements_by_xpath('//a[@class="list-news list-img"]')
print("path",len(path),type(path))
for a in path:
    url = a.get_attribute("href")
    print('url',url)

#list = broswer.find_elements_by_class_name("c-blocka")

# for a in list:
#     url = a.get_attribute("href")
#     text = a.text
#     #print(text)
#     #print(url)
#     print("标题:{}  网站:{}".format(text,url))