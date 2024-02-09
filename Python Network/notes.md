# Python Network

## Resources
***Read or watch:***
- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)


## [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)

- Is an asymmetric ***request-response*** protocol
    * An HTTP client sends a request to the server - `pulls`
    * The server then returns a response message - `pushes`
- An HTTP request is a stateless protocol - current is unaware of prev requests.
- It permits data-type negotiation & representation - systems can be built independently of the data being transferred.

## Browser
Receives URL reuest:
- turns it into a `request message`,
- sends it to `HTTP`,
- `HTTP` interprets the `request message`,
- `HTTP` then returns an appropriate `response message` - could be requested resource or an error.
- browser then formats the `response message` and displays it to `user`.

## Uniform Resource Locator (URL)
A URL (Uniform Resource Locator) is used to uniquely identify a resource over the web. URL has the following syntax:

`protocol://hostname:port/path-and-file-name`

***There are 4 parts in a URL:***
- `Protocol`: The application-level protocol used by the client and server, e.g., HTTP, FTP, and telnet.
- `Hostname`: The DNS domain name (e.g., www.nowhere123.com) or IP address (e.g., 192.128.1.2) of the server.
- `Port`: The `TCP` port number that the server is `listening` for incoming requests from the clients.
- `Path-and-file-name`: The name and location of the requested resource, under the server document base directory.

## HTTP Protocol
It receives the `request message` from the brouswer and sends it to the server.  
When Idle it listens to IP addresse(s) and port(s) in the specified configuration for incoming requests.  
The `request message` when it reaches the server:
- interprets, maps to `file`, returns to client,
- interprets, maps to `program`, executes, return output to client,
- returns error if request can't be satisfied.

## HTTP over TCP/IP
HTTP is a client-server application-level protocol. It typically runs over a TCP/IP connection. It only presumes a reliable transport. Any transport protocols that provide such guarantees can be used.

### IP
Is a network-layer protocol, deals with network addressing and routing machines for communication.

### TCP (Transmission Control Protocol)
Is transport-layer protocol, responsible for establish a connection between two machines.  
TCP consists of 2 protocols: TCP and UDP (User Datagram Package).

## HTTP Specifications
The HTTP specification is maintained by W3C [(World-wide Web Consortium)](https://www.w3.org/) and available at [http://www.w3.org/standards/techs/http](https://www.w3.org/TR/?tags[0]=protocol).  

There are currently two versions of HTTP, namely, HTTP/1.0 and HTTP/1.1.  
The original version, HTTP/0.9 (1991), written by Tim Berners-Lee, is a simple protocol for transferring raw data across the Internet.  HTTP/1.0 (1996) (defined in RFC 1945), improved the protocol by allowing MIME-like messages.  HTTP/1.0 does not address the issues of proxies, caching, persistent connection, virtual hosts, and range download. These features were provided in HTTP/1.1 (1999) (defined in RFC 2616).

## Apache HTTP Server or Apache Tomcat Server
is needed to study the HTTP protocol.