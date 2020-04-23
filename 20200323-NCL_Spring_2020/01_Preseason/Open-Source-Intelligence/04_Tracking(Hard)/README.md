# Tracking (Hard)
## One of our agents has lost the tail on a suspected hacker. Fortunately, they were able to install tracking software on the hacker's phone. To prevent detection, the tracker does not use location services - it simply records the wireless networks that the phone connects to. Use the logs to help us pick up the trail.

-	What city is the hacker in? | 20pts
-	We will need to conduct a visual verification of the hacker. They must have stopped at a store with CCTV to collect supplies on the first day. We can use footage from the CCTV. What is the address of a store that the hacker visited? | 20pts
-	We know that the hacker attacked the last network in their log, what's the name of the organization that they attacked?  Make sure that you are not guessing between possibilities. There should be 1 clear choice. | 25pts

Timestamp | Wifi Network
--- | ---
9/3/2018 12:48:01 | BC:F1:F2:2F:65:E0
9/4/2018 19:48:01 | 00:11:21:ee:71:30
9/4/2018 22:48:01 | 18:d6:c7:dd:45:77

---

## Since we are only given timestamps and MAC addresses, we need to find a service that keeps track of publicly discovered access points. [WiGLE](https://wigle.net/) is the best service for people to upload their own personal [wardriving](https://en.wikipedia.org/wiki/Wardriving) lists. We will use that in parallel with Google maps to get the answers.

###	What city is the hacker in? | 20pts
Enter the first MAC address (BC:F1:F2:2F:65:E0) into the BSSID box and select the `Filter` button. Scroll all the way out of the map and look for a purple circle on the map. Scroll into the map to find that it resides in Springfield.<br>
`Springfield`

###	We will need to conduct a visual verification of the hacker. They must have stopped at a store with CCTV to collect supplies on the first day. We can use footage from the CCTV. What is the address of a store that the hacker visited? | 20pts
When you scroll all the way in, eventually the name of the WiFi will show up. Scrolling into the first MAC address, we can see that the name is "Walmartwifi." Lets use this map and find the matching Walmart on Google maps to come up with the address. <br>
`1100 Lejune Dr, Springfield, IL 62703`

###	We know that the hacker attacked the last network in their log, what's the name of the organization that they attacked?  Make sure that you are not guessing between possibilities. There should be 1 clear choice. | 25pts
Filter by the last MAC address in the list and you'll find that the name of the WiFi network is the answer they were looking for. It is confusing though because they ask for an organization that was attacked. The GPS coordinates of the network make it look like it was a network belonging to Western Union or Dollar General. <br>
`Dept Of Homeworld Security`
