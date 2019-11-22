# Cisco (Easy)
## Analyze a Cisco router broadcasting via the Cisco Discovery Protocol and identify information about the router.

-	What is the Device ID of the router?
-	On what day was the router's software last updated?
-	What is the product number of the Cisco router?
-	What is the IP address of the Cisco router?

---

## Wireshark Time!!
![wireshark](./wireshark2.jpg)

Honestly, most of this is just going through a bunch of dropdown lists and looking for what you need...

###	What is the Device ID of the router?
Looks like there is only one packet in our capture.
The Device ID can be found in 
`Cico Discovery Protocol` -> `Device ID` <br>
`APb838.61f3.05ac`


###	On what day was the router's software last updated?
`Cico Discovery Protocol` -> `Software Version` -> `Compiled...` <br>
`Tue 30-Jul-13 22:57`

###	What is the product number of the Cisco router?
`Cico Discovery Protocol` -> `Software Version` <br>
`AIR-CAP2602I-Q-K9`

A quick google search verifies that our product number is [correct](https://www.cisco.com/c/en/us/products/collateral/wireless/aironet-2600-series/eos-eol-notice-c51-737512.html).

###	What is the IP address of the Cisco router?
`Cico Discovery Protocol` -> `Address`<br>
`192.168.10.10`