testString = '''http://freshsources.com/page5.html">Page 5</a>. And here is a link back to <a HrEf   = "http://freshsources.com/page3.html">Page 3</a>.'''

import urllib
import re
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
    

def get_all_links(urlString):
    urlSet = set()
    urlList = re.findall(r'href\s*=\s*[\'"]?(\http://[^\'">]+)', urlString,re.IGNORECASE)
    for x in urlList:
        urlSet.add(x)
    return urlSet


def crawl(seed,max_level):
    index = {}
    graph = {}
    urlString = get_page(seed)
    urlSet = get_all_links(urlString)
    for x in urlSet:
        index.add(
    


crawl('http://freshsources.com/page5.html',0)
