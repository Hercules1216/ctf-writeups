# GTP (Medium)
## Analyze GTP traffic to understand how a mobile device connects to a GSM network.

-	What is the IP address of the mobile handset?
-	What is the IP address of the SGSN?
-	What country is the mobile handset located in?
-	What is the name of the mobile network of the mobile handset?
-	What is the Mobile Subscription Identification Number of the mobile handset?
-	What is the local phone number (without country code or dashes) of the mobile handset?
-	What is the id used by the mobile handset to authenticate with the network?
-	What is the password used by the mobile handset to authenticate with the network?

---

###	What is the IP address of the mobile handset?
Echo request is coming from `127.0.0.2`
###	What is the IP address of the SGSN?
Echo response is coming from `127.0.0.1`
###	What country is the mobile handset located in?
Packet #3 is the request coming from the handset so the country code is most likely in there. Expand the `GPRS Tunneling Protocol` and the first thing that stands out is `MS international PSTN/ISDN number`. Seeing the international part tipped me off. Expanding that reveals the [MSISDN](https://www.webopedia.com/TERM/M/MSISDN.html).
We can see that the internationl code is `46` and wireshark tells us that that number is the country code for `Sweden`

It can also be found under `IMSI` under alongside `Movile Country Code (MCC)` but whatever.
###	What is the name of the mobile network of the mobile handset?
The mobile network can be found under `GPRS Tunneling Protocol` -> `IMSI` -> `Mobile Network Code (MNC)` <br>
`Telia Sverige AB`

Quick google search verifies that it is a real company and the correct answer.

###	What is the Mobile Subscription Identification Number of the mobile handset?
Clue to how you get the answer [here](https://en.wikipedia.org/wiki/International_mobile_subscriber_identity) <br>
`GPRS Tunneling Protocol`->`IMSI` <br>
It's the number without the MCC and MNC <br>
`0123456789`
###	What is the local phone number (without country code or dashes) of the mobile handset?
This value is the same that we came across in the 3rd question. We just strip the country code from it. Swedish phone numbers are also slightly [different](https://en.wikipedia.org/wiki/Telephone_numbers_in_Sweden). <br>
`702123456`
###	What is the id used by the mobile handset to authenticate with the network?
The ID can be found by going to `GPRS Tunneling Protocol`->`Protocol configuration options`->`Protocol or Container ID`->`PPP Password Authentication Protocol`->`Data`->`Peer-ID` <br><br>
ID: `mig`


###	What is the password used by the mobile handset to authenticate with the network?
The password can be found by going to `GPRS Tunneling Protocol`->`Protocol configuration options`->`Protocol or Container ID`->`PPP Password Authentication Protocol`->`Data`->`Password` <br><br>
Password: `hemmelig`