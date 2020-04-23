# Cracking 4 (Hard)
## Our officers have obtained password dumps storing hacker passwords. It appears that they are all themed around movies. Can you figure them out?

-	$1$uxff$upSLedgZAXoyF6sgZbxsK0
-	$1$tnck$hCk5g8U8mmmItOokmQCMv.
-	$1$dgsn$2ZgX3pvquWorGD2Lgjj3W1
-	$1$vgah$VnxHyh1o3FwMZAvKA5AQo0
-	$1$lkwc$iOXF5ekiNNyj1KByGFO8s/


---

We can figure out what type of hashes these are by looking at the hash examples list [here](https://hashcat.net/wiki/doku.php?id=example_hashes). The first three hashes can be cracked using hashcat and the rockyou.txt dump.

```
$ cat hashes.txt
$1$uxff$upSLedgZAXoyF6sgZbxsK0
$1$tnck$hCk5g8U8mmmItOokmQCMv.
$1$dgsn$2ZgX3pvquWorGD2Lgjj3W1
$1$vgah$VnxHyh1o3FwMZAvKA5AQo0
$1$lkwc$iOXF5ekiNNyj1KByGFO8s/

$ hashcat -a 0 -m 500 hashes.txt rockyou.txt
Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

$1$tnck$hCk5g8U8mmmItOokmQCMv.:stepup2thestreets
$1$uxff$upSLedgZAXoyF6sgZbxsK0:starwars1516
$1$dgsn$2ZgX3pvquWorGD2Lgjj3W1:$tarTr3k
Approaching final keyspace - workload adjusted.


Session..........: hashcat
Status...........: Exhausted
Hash.Type........: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)
Hash.Target......: hashes.txt
Time.Started.....: Wed Nov  6 15:06:53 2019 (19 mins, 41 secs)
Time.Estimated...: Wed Nov  6 15:26:34 2019 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    42717 H/s (9.95ms) @ Accel:256 Loops:125 Thr:1 Vec:8
Recovered........: 3/5 (60.00%) Digests, 3/5 (60.00%) Salts
Progress.........: 71721920/71721920 (100.00%)
Rejected.........: 0/71721920 (0.00%)
Restore.Point....: 14344384/14344384 (100.00%)
Restore.Sub.#1...: Salt:4 Amplifier:0-1 Iteration:875-1000
Candidates.#1....: $HEX[206b6d3831303838] -> $HEX[042a0337c2a156616d6f732103]
```


I tried creating multiple dicitonaries with rules using lists online but had no luck with the last two hashes.

1. `hashcat -a 0` - Set the attack mode to 'Straight.' Basically for use with wordlists/dictionaries
2. `hashcat -m 500` - Set the hashtype to crack equal to MD5Crypt. The codes for each hash type are on the hashcat wiki linked at the top of this page.
3. `--force` - May need to be appended to the end of the hashcat command if using an Intel CPU.