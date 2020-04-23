# Decoding 1 (Easy)
## A couple of hackers have encoded their messages using different number bases. See if you can decode them.
- `00110100 01101000 01100001 01101001 01110010 01100011 01100001 01110010 01100101 00110010`
- `3262656c6c746f776e32`
- `NTk2d2lsZHNob3QzNTA=`

---

## All messages can be decoded using [CyberChef](https://gchq.github.io/CyberChef/).

### `00110100 01101000 01100001 01101001 01110010 01100011 01100001 01110010 01100101 00110010`
Due to the fact that only '1's and '0's are used and it is grouped in octets, it is resonable to assume the message is encoded using binary. Select 'From Binary' with 'Space' as the delimiter in CyberChef to get the plaintext. CyberChef will reccomend decoding from binary as well. <br>
`4haircare2`

### `3262656c6c746f776e32`
The encoded message only consists of numbers 0-9 and letters a-f. That is a good indication that is is encoded using hex. Select 'From Hex' with 'None' as the delimiter in CyberChef to get the plaintext. CyberChef will reccommend decoding from hex as well. <br>
`2belltown2`
### `NTk2d2lsZHNob3QzNTA=`
The '=' (or even '==') sign at the end of the encoded message in a CTF is almost always a giveaway that Base64 is being used. Selecting 'From Base64' with 'A-Za-z0-9+/=' set as the alphabet and 'Remove non-alphabet chars' checked will successfully decode the message. <br>
`596wildshot350`