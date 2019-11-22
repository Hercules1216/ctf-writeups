# Printer (Medium)
## Analyze network traffic of a print request and see if you can extract the print job.

-	What is the Job Id of the print job that was sent to the printer?
-	What is the MIME type of the file that was sent for printing?
-	What is the IP address of the printer?
-	What is the version number of the interpreter that is displayed on the document that was sent to the printer?

---

###	What is the Job Id of the print job that was sent to the printer?
Sort the packets by `Protocol` and look at the IPP packets in order. In frame 149, when you look in the IPP dropdown list, you can see a `job-attribute-tag` section. Taking a look in there reveals the job-id.

`16`
###	What is the MIME type of the file that was sent for printing?
`incomplete`
###	What is the IP address of the printer?
All responses are coming from the printer... So...
`10.10.10.49`
###	What is the version number of the interpreter that is displayed on the document that was sent to the printer?
`incomplete`