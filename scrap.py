

def getExt(data):
    
    ind = data.find("www.amazon.")
    length = len(data)
    shorturl = data[ind:length]
    fi = shorturl.find("/")
    ext = shorturl[11:fi]
    #print(ext)
    
    return ext
 