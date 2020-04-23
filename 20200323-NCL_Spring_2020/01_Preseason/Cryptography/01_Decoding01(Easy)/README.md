# Decoding 1 (Easy)
## Our officers have obtained password dumps storing hacker passwords. After obtaining a few plaintext passwords, it appears that they are all encoded using different number bases.
- `067 070 143 157 154 157 162 145 166 145 162 171 065 064`
- `33 34 20 33 31 20 36 34 20 37 32 20 36 35 20 37 33 20 37 33 20 36 36 20 37 35 20 36 63 20 36 63 20 33 38 20 33 33`
- `31 30 5c 6c 67 6d 62 6f 61 5g 36 35`

---

## All messages can be decoded using [CyberChef](https://gchq.github.io/CyberChef/).

### `067 070 143 157 154 157 162 145 166 145 162 171 065 064`
Since you know that all of these are based off of different number bases, take a look at [this]() ASCII chart and it looks most likely to be octal. Also, there are leading zeros on numbers less than 100 so that is another hint. Use `From Octal` to decode the cipher text. <br>
`78colorevery54`

### `33 34 20 33 31 20 36 34 20 37 32 20 36 35 20 37 33 20 37 33 20 36 36 20 37 35 20 36 63 20 36 63 20 33 38 20 33 33`
CyberChef will automatically solve this one. The cipher text is double encoded using hex. Use `From Hex` twice to get the plaintext password. <br>
`41dressfull83`

### `31 30 5c 6c 67 6d 62 6f 61 5g 36 35`
This one stumped me for a second because I didn't see the `5g` near the end. `g` is outside fo the range for hex, signaling that it uses a higher base. We will use the `From Charcode` operation and go through the bases. We see that setting `Base` to `17` will give us the plaintext password. <br>
`43armshuge98`