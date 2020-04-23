# Decoding 5 (Hard)
## We have intercepted encrypted messages between hackers. Along with the messages were the numbers "3" and "7". Decipher them and find out what they are doing.
- `w     eytaihtkyddyuuet nrp h rhv?aeiosoctece`
- `s ersnusdoh y m kyee`

---

## All messages can be decoded using [CryptoCorner](https://crypto.interactive-maths.com/rail-fence-cipher.html).

### `w     eytaihtkyddyuuet nrp h rhv?aeiosoctece`
The fact that they told us `3` and `7` and the code has a randomly placed `?` in the mix denotes the use of a rail-fence cipher. Using the site linked above, change the rail key and decode the message. Don't forget to append the `?` as the site strips it out by default. <br>
Rail key = 3 <br>
`what key did you use to encrypt the archive?`

### `s ersnusdoh y m kyee`
Rail key = 7 <br>
`send me your ssh key`