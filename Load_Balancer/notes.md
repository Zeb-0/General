# Load Balancer
When you have an enterprise or website that gets a lot of hits, you may run into an overload problem. In that case you will need to distribute the load across multiple servers.  
This is where a load balancer comes in handy.

The Load balancer will distribute the workload across multiple individual systems or group of systems thus reducing the amount of work load on an individual system.

This consequently increases reliability, efficiency and availability of your enterprise APP.
---

## Resources:
**Read or watch:**
- [Load-balancing](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
- [Load-balancing algorithms](https://community.f5.com/kb/technicalarticles/intro-to-load-balancing-for-developers-%E2%80%93-the-algorithms/273759)
- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTPHeader](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/#distribution=Ubuntu&release=focal&version=2.8)
---

**TYpes of loade Balancers:**
- There are 2 types:
 * `Software load balancers`
 * `Hardware load balancers`

 ## Software Load Balncer
 It implements a combination of one or more scheduling algorithms.  
 The mostly used ones include:
 - Weighted scheduling
 - Round Robin scheduling
 - Least connection first scheduling

 ### Weighted scheduling algo.
 Work is assigned to the server according to the weight assigned to that server.  
 The balancer calculates the % of the traffic to be sent to a particular server.

 This algo is used when there is a `considerable difference in capabilities and specs` of different servers in the cluster.

 ### Round Robin scheduling
 Requests are sent to sever sequentially one after the other.

 Useful when the servers are of `equal specs`

 ### Least Connection First Scheduling
 Rquests are first served to the server currently handling the `least number of persistent connections`.

 When we have large number of persistent connections in the traffic unevenly distributed between the servers. It is often coupled with Sticky Session or Session aware load balancing. In this, all the request related to a session is sent to the same server to maintain the session state and syncronization.

 This approach is used when we have` session aware write operations in sync with client and the server` so that it avoids any inconsistency.

 ### Software Load Balancer Examples
**The following are few examples of software load balancers:**
- [HAProxy](https://www.haproxy.org/) – A TCP load balancer.
- [NGINX](https://www.nginx.com/resources/wiki/) – A http load balancer with SSL termination support. (install Nginx on Linux)
- [mod_athena](https://ath.sourceforge.net/mod_athena_doc/html/index.html) – Apache based http load balancer.
- Varnish – A reverse proxy based load balancer.
- Balance – Open source TCP load balancer.
- LVS – Linux virtual server offering layer 4 load balancing

---

## Hardware Load Balancers
Are often referred to as `specialized routers or switches` deployed btw servers and the cient.   
Are implemented btw `Layer4`(transport layer) and `Layer7`(application layer) of the OSI model



---

## Introduction to HAPxoxy & Load Balancing.
- `HAProxy` - refers to `High Availabilty Proxy`
- is a popular open source software TCP/HTTP Load balancer and proxying solution.
- commonly used to improve server environment perfomance & reliability by distirbuting workload across multiple servers.

### Access Control List (ACLs)
- are used to test some condition and perfom an action based on the test results.
     * the condition could be for example selecting a sever of blocking  a request

- Using `ACLs` allows flexible network traffic forwarding based on a variety of factors like pattern-matching and number of connections to a backend.

### Backend
- A Backend is a set of servers that receive forwarded requests.
- Basically can be defined by:
    * load balancing algo to use
    * lis of servers and ports

More servers increases potential load capacity.  
**Example of a two backend configuration of 2 web servers each listening to `port 80`

**1. web-backend:**
```
backend web-backend
    balance roundrobin
    server web1 web1.yourdomain.com:80 check
    server web2 web2.yourdomain.com:80 check
```
**2. Blog-backend:**
```
backend blog-backend
    balance roundrobin
    mode http
    server blog1 blog1.yourdomain.com:80 check
    server blog1 blog1.yourdomain.com:80 check
```

### Frontend
- define how requests should be forwarded to the backends
- their definitions are comprised of the following:
    * a set of IP addresses and a port (e.g. 10.1.1.7:80, *:443, etc.)
    * ACLs
    * `Use_backend` rules - define which backends touse depending on which ACL conditions are matched.
    * `Default_backend` rule - handles every other cases

## Types of Load Balancing
- No Load balancing
- Layer 4 Load Balancing
- Layer 7 Load Balancing

### nO Load Balancing
User connects directly via `yourdomain.com` to the server withouth any load balancing.  
If your server goes down so does everything.

### Layer 4 Load Balancing
Also `transport layer`  
User traffic is forwarded based on the ip range and port  
The user accesses the load balancer, which forwards the user’s request to the web-backend group of backend servers. Whichever backend server is selected will respond directly to the user’s request. Generally, all of the servers in the web-backend should be serving identical content–otherwise the user might receive inconsistent content. Note that both web servers connect to the same database server.
