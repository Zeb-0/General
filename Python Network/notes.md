# Python Network

## Resources
***Read or watch:***
- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)


### [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)

- Is an asymmetric ***request-response*** protocol
    * An HTTP client sends a request to the server - `pulls`
    * The server then returns a response message - `pushes`
- An HTTP request is a stateless protocol - current is unaware of prev requests.
- It permits data-type negotiation & representation - systems can be built independently of the data being transferred.

### Browser
Receives URL reuest:
- turns it into a `request message`,
- sends it to `HTTP`,
- `HTTP` interprets the `request message`,
- `HTTP` then returns an appropriate `response message` - could be requested resource or an error.