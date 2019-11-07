# Decoding 5 (Hard)
## We have intercepted encrypted messages between hackers. Along with the messages were the numbers "3" and "7". Decipher them and find out what they are doing.
- `w     eytaihtkyddyuuet nrp h rhv?aeiosoctece`
- `s ersnusdoh y m kyee`

---

## All messages can be decoded using [this](https://crypto.interactive-maths.com/rail-fence-cipher.html).

### `w     eytaihtkyddyuuet nrp h rhv?aeiosoctece`
The '3' and '7' will be our best hints here. It is pretty common the the 'Rail Fence Cipher' uses a default 'Rail Key' of 3. Seeing how there is some odd spacing as well as the random '?', we can assume the a rail fence cipher is being used. Using Crypto Corner's derypter, we input the text in the 'Ciphertext' box, make sure the rail key is set to 3 and then decrypt the message. Make sure to re-add the '?' to the end of the sentance. Their decrypter doesn't like punctuation.<br>
`what key did you use to encrypt the archive?`

### `s ersnusdoh y m kyee`
Since the last messsge used a key of 3, we can assume that this one will use a key of 7. After inputing our ciphertext, we get our plaintext message. <br>
`send me your ssh key`
