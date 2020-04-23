# Error Log (Medium)
## Analyze HTTP error logs to track server behavior and identify malicious actors.

-	How many "File does not exist" errors are in the log?
-	How many unique IP addresses are listed in the log?
-	What IP address generated the most errors?
-	What IP address scanned for the most unique files?
-	How many unique files (count different cases as different files) did the top scanning IP scan that yielded "File does not exist" errors?

---

Basic structure of each line in the log:
```
[Mon Nov 21 19:26:59 2011] [error] [client 89.28.31.174] File does not exist: /usr/local/www/csmc/html/favicon.ico
[Tue Nov 22 11:32:49 2011] [error] [client 93.116.213.145] File does not exist: /usr/local/www/csmc/html/csmc, referer: http://csmc.netadv.md/
[Tue Nov 22 11:36:39 2011] [error] [client 93.116.213.145] File does not exist: /usr/local/www/csmc/html/favicon.ico
[Tue Nov 22 11:36:42 2011] [error] [client 93.116.213.145] File does not exist: /usr/local/www/csmc/html/favicon.ico
[Tue Nov 22 11:37:49 2011] [error] [client 93.116.213.145] File does not exist: /usr/local/www/data/UserManager/<, referer: http://89.28.74.82/ftpadm/
```

###	How many "File does not exist" errors are in the log?
```
$ cat error.txt | cut -d ']' -f 4 | cut -d ':' -f 1 | sort | uniq -c | sort -nr | head
  65119  File does not exist
  21446  script not found or unable to stat
   1027  client sent HTTP/1.1 request without hostname (see RFC2616 section 14.23)
    503  request failed
    138  script '/usr/local/www/phpMyAdmin/scripts/setup.php' not found or unable to stat
    100  script '/usr/local/www/csmc/html/testproxy.php' not found or unable to stat
     59  script '/usr/local/www/csmc/html/wp-login.php' not found or unable to stat
     38  Invalid URI in request GET  HTTP/1.1
     29  script '/usr/local/www/csmc/html/xmlrpc.php' not found or unable to stat
     27  Invalid URI in request GET login.cgi HTTP/1.0
```
Command Breakdown:


Example line from log: `[Tue Nov 22 11:36:39 2011] [error] [client 93.116.213.145] File does not exist: /usr/local/www/csmc/html/favicon.ico`
Command | Description | Result
--- | --- | ---
`cat error.txt` | Send the contents of the file to terminal | Whole file
`cut -d ']' -f 4` | 4th field using ']' as the delimeter | `File does not exist: /usr/local/www/csmc/html/favicon.ico`
`cut -d ':' -f 1` | 1st field using ':' as the delimeter | `File does not exist`
`sort` | Sort alphabetically
`uniq -c` | Count each occurance of particular string | `65119  File does not exist`
`sort -nr` | Sort by number of occurances and make high to low
`head` | Only show top 10 lines of the output

###	How many unique IP addresses are listed in the log?
```
$ cat error.txt | cut -d '[' -f 4 | cut -d ']' -f 1 | cut -d ' ' -f 2 | sort -n | uniq | wc -l
8121
```
###	What IP address generated the most errors?
```
$ cat error.txt | cut -d '[' -f 4 | cut -d ']' -f 1 | cut -d ' ' -f 2 | sort -n | uniq -c | sort -nr | head -5
  34533 88.80.10.1
   9158 115.239.228.99
   5345 115.239.248.245
   3546 115.230.127.237
   2112 176.53.21.162
```
`88.80.10.1`
###	What IP address scanned for the most unique files?
```
# cat error.txt | grep "File does not exist" | cut -d '[' -f 4 | sort -k 7 | uniq | cut -d ' ' -f 2 | sort -n | uniq -c | sort -nr | head -5
   1559 176.53.21.162
     98 64.202.102.97
     90 69.64.61.86
     77 178.216.51.2
     41 213.175.192.73
```
`176.53.21.162`
###	How many unique files (count different cases as different files) did the top scanning IP scan that yielded "File does not exist" errors?
```
# cat error.txt | grep "File does not exist" | cut -d '[' -f 4 | sort -k 7 | uniq | cut -d ' ' -f 2 | sort -n | uniq -c | sort -nr | head -5
   1559 176.53.21.162
     98 64.202.102.97
     90 69.64.61.86
     77 178.216.51.2
     41 213.175.192.73
```
`1559`