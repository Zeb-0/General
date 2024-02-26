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