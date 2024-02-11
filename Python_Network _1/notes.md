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