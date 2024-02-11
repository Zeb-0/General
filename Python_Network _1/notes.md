# Resources
**Read or watch:**
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)

---
 ## Intro - HOWTO Fetch Internet Resources Using urllib Package

 ### urllib.request
 Is a python module for fetching URL by offerring a simple interface in the form of `urlopen()` function.  
 Supports many `URL schemes` such as `FTP`, `HTTP`, `SMPT`, etc.  

 ### Feching URLs
 Simplest way:  
```
import urllib.request
with urllib.request.urlopen("http://python.org/") as response:
    html = response.read()
```

### Retrieve resource and store it temporarily
- Use the following functions:
    * `shutil.copyfileobj()`,
    * `tempfile.NamedTemporaryFile()`

***Example:***  
```
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen("http://python.org/") as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass
```
---

HTTP is based on requests and responses - the client makes requests and servers send responses. urllib.request mirrors this with a Request object which represents the HTTP request you are making. In its simplest form you create a Request object that specifies the URL you want to fetch. Calling urlopen with this Request object returns a response object for the URL requested. This response is a file-like object, which means you can for example call `.read()` on the response:


```
import urllib.request

req = urllib.request.Request('http://python.org/')
with urllib.request.urlopen(req) as response:
   the_page = response.read()

```