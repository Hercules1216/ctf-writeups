# Stego 2 (Medium)
## Find the flag in the image.

![stego2](Steg2.bmp)

- What is the algorithm used to encrypt the flag?
- What is the hidden flag in the image?

---

### What is the algorithm used to encrypt the flag?
From past experience, I know that NCL commonly uses a stego tool called [Digital Invisible Ink Toolkit](http://diit.sourceforge.net/). Go ahead and download the application.
1. Select the `Decode` tab.
2. Select the image using the `Get Image` button.
3. Select the `Set Message` button to specify where you want the hidden message outputted to.
4. Cycle through the algorithms until you get a successful message.

`BlindHide` will give us the successful message letting us know that the message has been written to our file. 

### What is the hidden flag in the image?
Open the output file and our flag is printed there. <br>
`SKY-ERNT-4183`