# Integrity (Medium)
## We believe a file on a server have been compromised. Use a file integrity check log to identify the corrupted file. All of the files have been moved to the /root/samples folder.

-	How many files are in the /root/samples folder?
-	What is the file that does not match its corresponding hash in the integrity_check.log?

---

**I don't have any of the original files or the answer but I'll try to explain it best I can.**

###	How many files are in the /root/samples folder?
The files in the `/root/samples/` folder were .bin files named 0.bin to 999.bin
```
$ ls -l /root/samples/ | wc -l
1000
```
Be careful not to use the `ls -la` or it will also count the `..` and `.` directories

###	What is the file that does not match its corresponding hash in the integrity_check.log?

The format of the 'integrity check log' is something like this:
```
513ea344bbd8f476588b9987f5e255a8    0.bin
bb607b2027adf278cb8f23c2ed4a0a78    1.bin
...
e708864855f3bb69c4d9a213b9108b9f    998.bin
8fad3c2eeca28c6bd11f40fdb0f41693    999.bin
```

We can simply run `md5sum` on the entire samples folder.
This gives us all the correct output, but in the wrong order. For example, the output would look like:
```
...
513ea344bbd8f476588b9987f5e255a8    199.bin
bb607b2027adf278cb8f23c2ed4a0a78    2.bin
e708864855f3bb69c4d9a213b9108b9f    200.bin
...
```
All we have to do is sort numerically by the second column. The command would look like <br>
`/root/samples$ md5sum * | sort -n -k 2`

We would then run `diff` against both lists.
I ended up just pasting them into an online diff checker like [this](https://www.diffchecker.com/).

Only one file stood out as different.