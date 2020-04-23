# Compromise Report (Easy)
## CCleaner 5.33 was found to contain malware. We know that several computers on our network run that software. Conduct research to determine if we have been compromised.



- What is the name of the malware included in CCleaner? | 10pts
- How many seconds does the malware wait before starting malicious operations? | 10pts
- What is the DLL that the malware infects? | 10pts
- What is the registry location where the malware stores the DGA IP address? | 10pts
- What specific IP address does the malware make HTTP POST requests to? | 10pts


---

## All answers can be found on [this](https://blog.talosintelligence.com/2017/09/avast-distributes-malware.html) post by Cisco Talos group.

### What is the name of the malware included in CCleaner? | 10pts
`Floxif`
### How many seconds does the malware wait before starting malicious operations? | 10pts
`601`
### What is the DLL that the malware infects? | 10pts
`CBkrdr.ddl`
### What is the registry location where the malware stores the DGA IP address? | 10pts
`HKLM\SOFTWARE\Piriform\Agomo:NID`
### What specific IP address does the malware make HTTP POST requests to? | 10pts
`216[.]126[.]225[.]148`