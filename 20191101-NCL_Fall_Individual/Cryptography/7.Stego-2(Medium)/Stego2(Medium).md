# Stego 2 (Medium)
## We have come across this image that appears to be tampered. Which we think there may be a hidden "flag". See what you can uncover.

![stego1](./Stego2.jpg)

- What is the flag hidden in the image?

---

### - What is the flag hidden in the image?
This one took a little bit longer to figure out. NCL in the past has been known to only use the [Digital Invisible Ink Toolkit](http://diit.sourceforge.net/) for harder stego challenges. After going through each of the decoding algorithms, I decided to turn to some basic stego tools that are well known. The list of common tools to try was strings, Exiftool, Steghide, Foremost, Stegsolve. I ended up trying Steghide first and found the flag. Read more about [Steghide](http://steghide.sourceforge.net/documentation/manpage.php).

```
$ steghide extract -sf Stego\ 2.jpg
Enter passphrase: [no passwd]
wrote extracted data to "flag.txt".
$ cat flag.txt
```

`SKY-QUAK-7261`

Notes:
- `extract` - Required keyword to extract. Steghide can also be used to encrypt.
- `-sf` - Tells Steghide that you are working with a stegofile.