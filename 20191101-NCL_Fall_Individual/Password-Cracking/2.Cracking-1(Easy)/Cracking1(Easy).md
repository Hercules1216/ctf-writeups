# Cracking 1 (Easy)
## Our officers have obtained password dumps storing hacker passwords. After obtaining a few plaintext passwords, it appears that they overlap with the passwords from the rockyou breach.


-	807103935564020ae6df7301f0e34605
-	2562205460b692619fa42ff3bc157c56
-	A746f03bb092d346884fa2fa69654ced
-	F69f3b3795be46c1a83bf68774ac1a2d
-	ca76bbb75f141a5d33d30ec23bce26f0



---

## I used [hashcat](https://hashcat.net/wiki/doku.php?id=hashcat) to crack all passwords.

The hashes are 33 characters long and are most likely MD5.

1. Create a text file called 'hashes.txt' and paste each hash in line by line.
```
$ cat hashes.txt
807103935564020ae6df7301f0e34605
2562205460b692619fa42ff3bc157c56
A746f03bb092d346884fa2fa69654ced
F69f3b3795be46c1a83bf68774ac1a2d
ca76bbb75f141a5d33d30ec23bce26f0
```
2. Download the **rockyou.txt** if you don't already have it. <br>
`$ wget -O rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt`

3. Running hashcat using our **hashes.txt** as the file and **rockyou.txt** as the dictionary/wordlist will give us the plaintext passwords. <br>
```
$ hashcat -a 0 -m 0 hashes.txt rockyou.txt
Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 2 secs

807103935564020ae6df7301f0e34605:vampire2009
2562205460b692619fa42ff3bc157c56:pumkin118
f69f3b3795be46c1a83bf68774ac1a2d:midnightspooky
ca76bbb75f141a5d33d30ec23bce26f0:ghoul666
a746f03bb092d346884fa2fa69654ced:1ghosts3

Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: hashes.txt
Time.Started.....: Wed Nov  6 13:21:45 2019 (2 secs)
Time.Estimated...: Wed Nov  6 13:21:47 2019 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  7414.3 kH/s (0.38ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 5/5 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 13025280/14344384 (90.80%)
Rejected.........: 0/13025280 (0.00%)
Restore.Point....: 13008896/14344384 (90.69%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: 1kanya31 -> 1cherrytop

Started: Wed Nov  6 13:21:36 2019
Stopped: Wed Nov  6 13:21:48 2019
```

Notes:
1. `wget` - A network downloader. You can read up on it [here](https://linux.die.net/man/1/wget)
2. `wget -O` - Specify the name of the output file downloaded from the given link.
3. rockyou.txt is password dump that occured in 2009. [Here](https://darknetdiaries.com/episode/33/) is a great podcast on the breach.
4. `hashcat -a 0` - Set the attack mode to 'Straight.' Basically for use with wordlists/dictionaries
5. `hashcat -m 0` - Set the hashtype to crack equal to MD5. The codes for each hash type are on the hashcat wiki linked at the top of this page.
6. `--force` - May need to be appended to the end of the hashcat command if using an Intel CPU.