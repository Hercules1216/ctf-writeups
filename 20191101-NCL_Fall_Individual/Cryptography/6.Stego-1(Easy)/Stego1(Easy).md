# Stego 1 (Easy)
## We have come across this image which we think may contain a flag. Try to make some sense out of it.

![stego1](./Stego1.jpg)

- What is the flag hidden in the image?

---

## The flag can be found by either running the 'strings' command on the file or using [Forensically](https://29a.ch/photo-forensics/).

### What is the flag hidden in the image?
Often with challenges rated easy, the flag can simply be found by running **strings** on the file. Basically, **strings** looks for (by default) 4 or more printable characters in a file. You can read more about it [here](https://linux.die.net/man/1/strings). <br>
`$ strings Stego1.jpg | grep 'NCL\|SKY'` <br>
`SKY-HONK-2651`

Notes:
- `'|'` is used to take the output of one command and give it as input to another command.
- `grep 'NCL\|SKY'` - Search through the input and look for any lines that conatain 'NCL' or 'SKY' (NCL flags always begin with either NCL or SKY).