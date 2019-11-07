# PayPal (Hard)
## An online retail vendor has had a purchase marked as fraudulent after it had been shipped. Investigate the transaction logs to find the anomaly.

-	What is the Merchant Id of the vendor?
-	How much does the flat-rate shipping cost?
-	How many seconds elapsed from the first transaction to the last transaction?
-	How many payments were processed?
-	What is the total amount of revenue (in USD) that was processed?
-	What is the email address of the buyer who initiated the anomalous transaction in this log?

---

###	What is the Merchant Id of the vendor?
We will use `grep` with color set to always. This will allow us to quickly see where the merchant_id is. This is required because grep returns the whole line. The problem is that the line is still quite large so it is difficult to manually scan through.
`$ cat paypal.log | grep --color=always merchant_id | head -1` - ID is the same throughout the transactions.
**`"merchant_id":"P3FSA9QMG5GZ4"`**
###	How much does the flat-rate shipping cost?
Same as looking for the merchant_id but just change it out with shipping. I added the " to grep so that it wouldn't also pick up on the shipping address field.
`$ cat paypal.log | grep --color=always 'shipping"' | head -20` <br>
**`..."shipping":"5.99"...`**

###	How many seconds elapsed from the first transaction to the last transaction?
We can use a little trick to display both the first record and the last record in the file. <br>
`$ (head -n10 && tail -n10) < paypal.log` <br>
We can see from the output that:
Record | Time
---|---
First Record | [04-15-2018 09:32:16]
Last Record | [05-01-2018 19:15:32]

To calculate the difference, I just used [this](https://www.timeanddate.com/date/duration.html) online tool.

Answer came out to `1417396` seconds.

###	How many payments were processed?
Payments are only technically processed if the `state` is set to `approved`. So, we just make sure to `grep`, first, only those lines that include an invoice number and then `grep` for only those that were approved.
```
$ cat paypal.log | grep invoice_number | grep '"state":"approved"' | wc -l
383
```
###	What is the total amount of revenue (in USD) that was processed?
They cound shipping, tax, and the original item as revenue so we will take the first price that the log lists.
```
[04-15-2018 09:32:22] PayPal\Core\PayPalHttpConnection : DEBUG: Response Data: {"id":"PAY-KQROGHZ6REZHDVHCPIFX6BK2","intent":"sale","state":"approved","cart":"7aPEMehW6dBwJ6zxo","payer":{"payment_method":"paypal","status":"VERIFIED","payer_info":{"email":"MCassin@hotmail.com","first_name":"Moises","last_name":"Cassin","payer_id":"471982AE559CA","shipping_address":{"recipient_name":"Moises Cassin","line1":"7337 Tremblay Freeway","city":"Monroeville","state":"OH","postal_code":44847,"country_code":"US"},"country_code":"US"}},"transactions":[{"amount":{"total":"58.98","currency":"USD","details":{"subtotal":"49.99","tax":"3.00","shipping":"5.99"}},"payee":{"merchant_id":"P3FSA9QMG5GZ4","email":"payments@hakrshop.cityinthe.cloud"},"description":"Please enter description here.","invoice_number":"2383E8272EC66","item_list":{"items":[{"name":"Plunder Bug","price":"49.99","currency":"USD","quantity":1}],"shipping_address":{"recipient_name":"Moises Cassin","line1":"7337 Tremblay Freeway","city":"Monroeville","state":"OH","postal_code":44847,"country_code":"US"}},"related_resources":[]}],"links":[]}
```

We run `$ cat paypal.log | grep invoice_number | grep '"state":"approved"' | cut -d '"' -f 80`

```
58.98
59.98
---[snip]---
110.98
69.98
```

We use [this](https://miniwebtool.com/sum-calculator/) online calculator that allows us to just paste in the values... but we get an error... Why?

After looking through the numbers, we find that there is an anomoly in our list of numbers. It looks like the log is slightly different on one single line compared to the others based on how we `cut` the log up.

We pipe the our list to `nl` and find that line 288 is where our problem lies.
```
$ cat paypal.log | grep invoice_number | grep '"state":"approved"' | cut -d '"' -f 80 | nl
...
287  139.94
288  total
289  195.93
...
```

Let's modify our original command so that we can pull out the problem line and a known good line in the logs. <br>
```
$ cat paypal.log | grep invoice_number | grep '"state":"approved"' | head -288 | tail -2
[04-27-2018 13:07:45] PayPal\Core\PayPalHttpConnection : DEBUG: Response Data: {"id":"PAY-GC5JPV2R3IP0G4DIGYRWY9AY","intent":"sale","state":"approved","cart":"GH09B5rtrJbgew7Ew","payer":{"payment_method":"paypal","status":"VERIFIED","payer_info":{"email":"SLueilwitz@hotmail.com","first_name":"Savion","last_name":"Lueilwitz","payer_id":"5005DFC85B01E","shipping_address":{"recipient_name":"Savion Lueilwitz","line1":"458 Bayer Points","city":"Kwigillingok","state":"AK","postal_code":99622,"country_code":"US"},"country_code":"US"}},"transactions":[{"amount":{"total":"139.94","currency":"USD","details":{"subtotal":"133.95","tax":"0.00","shipping":"5.99"}},"payee":{"merchant_id":"P3FSA9QMG5GZ4","email":"payments@hakrshop.cityinthe.cloud"},"description":"Please enter description here.","invoice_number":"2669E956C6E06","item_list":{"items":[{"name":"Great Scott Gadgets Ubertooth One, Antenna & Aluminum Enclosure Bundle by Nooelec","price":"133.95","currency":"USD","quantity":1}],"shipping_address":{"recipient_name":"Savion Lueilwitz","line1":"458 Bayer Points","city":"Kwigillingok","state":"AK","postal_code":99622,"country_code":"US"}},"related_resources":[]}],"links":[]}
[04-27-2018 13:41:15] PayPal\Core\PayPalHttpConnection : DEBUG: Response Data: {"id":"PAY-KHPGXIRRJJUBYATJUPQQ5ALY","intent":"sale","state":"approved","cart":"MkqQBGAfxAhzSlmsP","payer":{"payment_method":"paypal","status":"VERIFIED","payer_info":{"email":"JHarrington@gmail.com","first_name":"Julia","last_name":"Harrington","payer_id":"50063D59BE9EA","shipping_address":{"recipient_name":"Julia Harrington","line1":"18814 Doty Avenue","city":"Torrance","state":"CA","postal_code":"90504","country_code":"US"},"country_code":"US"}},"transactions":[{"amount":{"total":"111.98","currency":"USD","details":{"subtotal":"99.99","tax":"6.00","shipping":"5.99"}},"payee":{"merchant_id":"P3FSA9QMG5GZ4","email":"payments@hakrshop.cityinthe.cloud"},"description":"Please enter description here.","invoice_number":"26700AE4E3AFF","item_list":{"items":[{"name":"Bash Bunny","price":"99.99","currency":"USD","quantity":1}],"shipping_address":{"recipient_name":"Julia Harrington","line1":"2 Claremont Street","city":"Rockland","state":"ME","postal_code":"04841","country_code":"US"}},"related_resources":[]}],"links":[]}
```
Now, we know that the anomoly occurs before our `total` value and that the error probably has something to do with double quotes.

Scanning through the two logs, we quickly learn that the good line takes the `"postal_code"` as an integer while the anomolious line takes it as a string. Let's replace `"total"` in our list of prices with the actual price and sum up everything using the online calculator.

$`52983.60` is our final answer.

###	What is the email address of the buyer who initiated the anomalous transaction in this log?
We figured out our anomolous record by luck just because of how we were cutting the logs up. Sweet!
![luck](./luck.gif)

Anyway... Looking at our problem line, we can see that the email is `JHarrington@gmail.com`