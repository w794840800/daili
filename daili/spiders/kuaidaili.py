from selenium import webdriver

class Item(object):
    ip  = None
    port = None

class getProxy(object):
    def __init__(self):
        self.starturl = "http://www.kuaidaili.com/free/"
        self.proxylist = self.getproxylist(self.starturl)
        self.saveFile(self.proxylist)
    def getproxylist(self, starturl):
        browser = webdriver.PhantomJS()
        print("starturl",starturl)
        proxy_list = []
        browser.get(starturl)
        browser.implicitly_wait(3)
        content = browser.find_elements_by_xpath("//tbody/tr")
        print("content",content)
        for tr in content:
            item = Item()
            ip = tr.find_element_by_xpath("./td[1]").text
            port = tr.find_element_by_xpath("./td[2]").text
            item.port = port
            item.ip = ip
            proxy_list.append(item)
            print('ip',ip)
            print('port',port)
        browser.quit()
        return proxy_list

    def saveFile(self, proxylist):
        with open("proxy1.txt","a") as f:
            for list in proxylist:
                f.write(list.ip+"\t")
                f.write(list.port+"\n")



if __name__=="__main__":
    getProxy()