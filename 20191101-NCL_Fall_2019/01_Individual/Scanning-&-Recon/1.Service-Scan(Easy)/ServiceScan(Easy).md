# Service Scan (Easy)
## Test your understanding of port scanning by scanning scanme9423.cityinthe.cloud and answering these questions. 
### Note: You are allowed to run automated tools on this target. Please be aware of any manipulation of traffic that your ISP may be doing.

-	What is the lowest open TCP port on the server?
-	What is the second lowest open TCP port on the server?
-	What is the third lowest open TCP port on the server?
-	What is the fourth lowest open TCP port on the server?
-	What is the name of the software service running on the 3rd lowest port?
-	What is the "Instance ID" of the service running on the 3rd lowest TCP port?
-	What is the name of the software service running on the 4th lowest TCP port?

---

Let's first discover every port on the host. We will do a scan on all the ports<br> 
```
$ nmap -p- scanme9423.cityinthe.cloud

PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
194/tcp open  irc
6667/tcp open  irc
```


###	What is the second lowest open TCP port on the server?
`80`
###	What is the third lowest open TCP port on the server?
`194`
###	What is the fourth lowest open TCP port on the server?
`6667`
###	What is the name of the software service running on the 3rd lowest port?
Visiting the website `http://scanme9423.cityinthe.cloud:194` will provide us the software running on it. <br>
`Rocket.Chat`
###	What is the "Instance ID" of the service running on the 3rd lowest TCP port?
 X-Instance-ID: `5oEfZ5aizdk8Ghm7R`
###	What is the name of the software service running on the 4th lowest TCP port?
```
nmap -sC -sV -p 6667 scanme9423.cityinthe.cloud
6667/tcp open  irc
| irc-info: 
|   users: 2
|   servers: 1
|   chans: 0
|   lusers: 2
|   lservers: 0
|   server: 24a5ae1b0ed7.example.com
|   version: InspIRCd-3. 24a5ae1b0ed7.example.com 
|   source ident: nmap
|   source host: 64-126-80-175.dyn.everestkc.net
|_  error: Closing link: (nmap@64-126-80-175.dyn.everestkc.net) [Client exited]
Service Info: Host: 24a5ae1b0ed7.example.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Software: `InspIRCd`