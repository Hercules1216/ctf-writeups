# Access Log (Easy)
## Analyze HTTP access logs to track server behavior.

-	How many requests were made to the server?
-	How many requests were made for robots.txt?
-	What is the IP address of the device that made the most requests to the server?
-	How many Partial Content response codes did the server return?
-	What URL returned a "bad request" error code?

---

###	How many requests were made to the server?
The file is compleatly made of requests so we can just use `wc -l` to count every line in the file.
```
$ cat access_log.txt | wc -l
5880
```
###	How many requests were made for robots.txt?
We will just `grep` for the robots.txt request and pipe it to `wc -l`
```
$ cat access_log.txt | grep "GET /robots.txt" | wc -l
791
```
###	What is the IP address of the device that made the most requests to the server?
Lets get our hands dirty with some `cut` and `sort`...

```
$ cat access_log.txt | cut -d ' ' -f 1 | sort -n | uniq -c | sort -nr | head -5
 727 162.251.20.188
 120 35.193.112.44
  97 87.250.244.11
  88 149.56.142.135
  64 100.35.75.170
```

**162.251.20.188 would be our answer**


Lets dissect this command that we just ran...
Example line from the file:<br>
`87.250.244.11 - - [06/Oct/2019:05:29:17 +0200] "GET /robots.txt HTTP/1.1" 404 208` <br><br>
`cat access_log.txt` - Output contents of file to terminal
<br>`cut -d ' ' -f 1 ` - Only look at the IP addresses in the file. Use a space as the delimeter between "fields"
<br>`sort -n` - Sort IP addresses numerically. This is required because of how uniq detects duplicate entries.
<br>`uniq -c` - uniq gets rid of any duplicate entries. The `-c` flag instead counts up the occurances of a particular string. In this case, how many occurances of an IP.
<br>`sort -nr` - Sort the number of occurances numerically (`-n`) and reverse the order (`-r`). The default to sort is the the first field and from lowest to highest.
<br>`head -5` - Only show the first 5 lines of output. This is just for readability. `tail` would show the last 5 lines.


###	How many Partial Content response codes did the server return?

A quick Google search brings up a [list](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) of HTTP status codes. It looks like status code 206 is what we're looking for.

Looking at the last two fields in our access log, we can see that the first of the two is our status code. (** are added for emphasis)
```
87.250.244.11 - - [06/Oct/2019:05:29:17 +0200] "GET /robots.txt HTTP/1.1" **404** 208
87.250.244.11 - - [06/Oct/2019:05:29:21 +0200] "GET /favicon.ico HTTP/1.1" **200** 15086
```
We need to craft a command that will return the number of request that returned a 206 but won't accidently pick on a '206' anywhere else. So we can't just do `cat access_log.txt | grep 206`

However, we can cheat a bit to make it simpler than using `cut` or `awk`. One example of a line that would mess us up is <br>
`13.124.85.55 - - [09/Oct/2019:07:21:23 +0200] "POST //flame.php HTTP/1.1" 404 206` <br>
Simply grepping for 206 would return this line but mess up our overall count. Instead, we observe that our status code is the only place that:
1. Would be 206
2. Has a space on both sides. The last field technically ends with a line break.

So...
```
$ cat access_log.txt | grep '206' | wc -l
86

$ cat access_log.txt | grep ' 206 ' | wc -l
4
```
Notice the difference?

**4 is our right answer**



###	What URL returned a "bad request" error code?
All we have to do is modify our last command slightly and we get the answer.
```
$ cat access_log.txt | grep ' 400 '
182.100.67.238 - - [20/Oct/2019:10:59:08 +0200] "POST /utility/convert/index.php?a=config&source=d7.2_x2.0 HTTP/1.1" 400 226
```

**`/utility/convert/index.php?a=config&source=d7.2_x2.0` would be our correct answer**