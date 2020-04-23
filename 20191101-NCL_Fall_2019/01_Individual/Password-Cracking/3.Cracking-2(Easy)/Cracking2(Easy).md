# Cracking 2 (Easy)
## Our officers have obtained password dumps storing hacker passwords. Try your hand at cracking them.

-	8DB1487EE6A5A8A6F95968FD0DEEE3F2:8678EF2D73D249922033B212DBFD9BF3
-	B5B79ECCB284EFCA3B7B4BB08EB2E5AC:F1E029BB3C1207E968C20165E19E5429
-	281CAAB14F07C1622E9D59C9A4716FCD:0AD2652E53AFEB54B90B8890BD324BD1

---

## I used an online [database](https://crackstation.net/) of cracked hashes to complete this challenge.

This output that we are given is in the form of a dump of the Windows SAM file. The format is [LM Hash]:[NTLM Hash]. You can read up more about what that means [here](https://medium.com/@petergombos/lm-ntlm-net-ntlmv2-oh-my-a9b235c58ed4). For now, we will just take the NTLM hashes and plugging them into the online service. They immediately return our answers.
```
8678EF2D73D249922033B212DBFD9BF3	NTLM	grimreaper08
F1E029BB3C1207E968C20165E19E5429	NTLM	darkskulls
0AD2652E53AFEB54B90B8890BD324BD1	NTLM	6witchkid
```