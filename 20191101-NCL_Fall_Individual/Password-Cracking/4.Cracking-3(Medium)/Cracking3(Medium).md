# Cracking 3
## Our officers have obtained password dumps storing hacker passwords. It appears that they are all in the format: "SKY-QQTY-" followed by 4 digits. Can you crack them?

-	3334c06568fd23d624392b5fabadbc32
-	2a09d2c2fbb03144c799d6e27fd736dd
-	fb92ccb90957b1a8f5e187680ae2328d

---

## I used [hashcat](https://hashcat.net/wiki/doku.php?id=hashcat) to crack all passwords.

This can be easily accomplished using hashcat's brute-force method with their built-in charsets.
1. Put the hashes into a file called 'hashes.txt'
```
$ cat hashes.txt
3334c06568fd23d624392b5fabadbc32
2a09d2c2fbb03144c799d6e27fd736dd
fb92ccb90957b1a8f5e187680ae2328d
```

2. Run hashcat with the brute-force mode and add the character set cards at the end to find each plain-text password.
```
$ hashcat -a 3 -m 0 hashes.txt SKY-QQTY-?d?d?d?d


fb92ccb90957b1a8f5e187680ae2328d:SKY-QQTY-3532
2a09d2c2fbb03144c799d6e27fd736dd:SKY-QQTY-5199
3334c06568fd23d624392b5fabadbc32:SKY-QQTY-5255

Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: hashes.txt
Time.Started.....: Wed Nov  6 13:54:03 2019 (1 sec)
Time.Estimated...: Wed Nov  6 13:54:04 2019 (0 secs)
Guess.Mask.......: SKY-QQTY-?d?d?d?d [13]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    43338 H/s (0.60ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 3/3 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 10000/10000 (100.00%)
Rejected.........: 0/10000 (0.00%)
Restore.Point....: 0/10000 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: SKY-QQTY-1234 -> SKY-QQTY-6497
```

Notes:
1. `hashcat -a 3` - Set the attack mode to 'Brute-Force.'
2. `hashcat -m 0` - Set the hashtype to crack equal to MD5. The codes for each hash type are on the hashcat wiki linked at the top of this page.
3. `?d?d?d?d` - Tells hashcat to brute force using 4 digits. Ex. 0000, 0001, 0002...9999.
4. `--force` - May need to be appended to the end of the hashcat command if using an Intel CPU.
