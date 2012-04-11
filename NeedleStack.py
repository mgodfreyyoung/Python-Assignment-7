from urllib import *
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
    
print get_page('http://freshsources.com/page5.html')