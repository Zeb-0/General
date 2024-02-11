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

## Data
Sometimes you want to send data to a URL (often the URL will refer to a CGI (Common Gateway Interface) script or other web application). With HTTP, this is often done using what’s known as a POST request. This is often what your browser does when you submit a HTML form that you filled in on the web. Not all POSTs have to come from forms: you can use a POST to transmit arbitrary data to your own application. In the common case of HTML forms, the data needs to be encoded in a standard way, and then passed to the Request object as the data argument. The encoding is done using a function from the [urllib.parse](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) library.

***Example:***  
```
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'Name' : 'Zeberio Morande',
'locatio' : 'Nairobi',
'language': 'Python'}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
```
### Use HTTP GET request
URL Request will use a GET request if `data` is not passed as the argument.  
You can pass data into HTTP GET request by directly encoding it in the URL.

***Example:***
```
import urllib.parse
import urllib.request

data = {}
data['name'] = 'Zeberio Morande'
data['location'] = 'Nairobi'
data['language'] = 'python'
url_values = urllib.parse.urlencode(data)
print(url_values)
print()

name=Zeberio+Morande&language=python&location=Nairobi
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)
```

## Headers
A browser identifies itself through the `user-agent` header.  
You can pass a dictionary of headers into the `Request object` when creating it. See below:
```
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'Name' : 'Zeberio Morande',
'locatio' : 'Nairobi',
'language': 'Python'}

headers = {'user_agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.reuest.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
```

## Handling Exceptions
urlopen raises [URLError](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError) when it cannot handle a response.

### URLError
Raised incse of no `network connection` or Server doesn't exist.  
The exception raised has a `reason` atribute - tuple with (error code, text error message).

***Example:***
```
req = urllib.request.Request('http://www.pretend_server.org')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
(4, 'getaddinfo failed')
```

### HTTPError
These only occur between codes 400 - 599 range.  
[Read more](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses).

When an error is raised, the server responds by sending an error code and an error page.  
You can use the HTTPError instance as a response on the page returned. This means that as well as the code attribute, it also has read, geturl, and info, methods as returned by the `urllib.response` module:

***Example:***
```
req = urllib.request.Request('http://www.python.org/fish.html')
try: urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
```

when dealing with these errors you can use:

**Approach 1:**
```
from urllib.request import Request urlopen
from urllib.error import URLError HTTPError

req = Request(someurl)
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)

else:
    # all good

```

**Approach 2:**
```
from urllib.request import Request, urlopen
from urllib.error import URLError

req = Request(someurl)
try:
    response = urlopen(req)
except URLError as e:
    if hasatt(e, 'reason'):
        print('We failed to reach a server')
        print('reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    else:
        # all good
```