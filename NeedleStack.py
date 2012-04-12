testString = '''http://freshsources.com/page5.html">Page 5</a>. And here is a link back to <a href   = "http://freshsources.com/page3.html">Page 3</a>.'''

import urllib
import re
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
    

def get_all_links(urlString):
    urlSet = {}
    urlSet = set(re.findall(r'href\s*=\s*[\'"]?(\http://[^\'">]+)', urlString)) 
    return urlSet

print get_page('http://freshsources.com/page5.html')   
urlString = get_page('http://freshsources.com/page5.html')

print get_all_links(urlString)

