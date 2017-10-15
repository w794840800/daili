from selenium import webdriver
import os
import requests
def get_commic(url):
    url_list = []
    browser = webdriver.PhantomJS()
    browser.get(url)
    browser.implicitly_wait(3)
    #print(browser.title)
    title = browser.title.split(',')[0]
    #print(title)
    mkdir(title)
    comic_list = browser.find_elements_by_xpath('//div[@class="comic_Serial_list"]/a')
    #print(comic_list.text)
    for a in comic_list:
        url = a.get_attribute("href")
        name = a.text
        #print(name)
        #print(url)
        url_list.append(url)

    Commic = dict(name= title,urls = url_list)
    browser.quit()
    return Commic
def mkdir(path):
    print("path",path)
    if not os.path.exists(path):
        os.mkdir(path)


def save_img(fileName, pic_url):
    content = requests.get(pic_url).content
    with open(fileName,"wb") as f:
        f.write(content)

def get_pic(commics):
    basedir = commics['name']

    proxy_urls = commics['urls']
    browser = webdriver.PhantomJS()
    for url in proxy_urls:
        #print('url',url)
        browser.get(url)
        browser.implicitly_wait(3)
        print("getpic",browser.title)
        dir = basedir+"/"+browser.title.split("-")[1]
        print("dir",dir)
        mkdir(dir)
        next_button = browser.find_element_by_xpath('//div[@id="AD_j1"]/div/a[4]')
        print("nextbutton")
        pageNum = len(browser.find_elements_by_xpath('//select[@id="pageSel"]/option'))
        print("pagenum",pageNum)
        for i in range(pageNum):
            pic_url = browser.find_element_by_xpath('//img[@id="curPic"]').get_attribute("src")
            print("pic_url",pic_url)
            fileName = dir+"/"+str(i)+'.png'
            print("filename",fileName)
            save_img(fileName,pic_url)
            next_button.click()
        print("当前章节完成\t{}".format(browser.title))
def main():
    url = "http://manhua.sfacg.com/mh/XXSJ/"
    commics = get_commic(url)

    get_pic(commics)
if __name__=="__main__":
    main()