# Capture the Flag (Medium)
## We have found an image of a hacker that has captured the flag! Help us retrieve the flag!

![CTF](ctf.jpeg)
<!-- <img src="./ctf.jpeg" width="100" height="100"> -->

-	What city or town is the hacker located in?
-	On what date was this photo taken?
-	What is the name of the business that owns the field in the image?
-	What is the value of the flag?

---

## All answers can be found via [this](https://29a.ch/photo-forensics/) online photo forensics service.

### 	What city or town is the hacker located in?
Scroll down to the **Geo Tags** section and select **View on Google Maps**. Once you look at the **Satellite** view, you can tell that the maze you're looking at is connected to **Long Acre Farms**. Looking at the address of the farm, you can see exactly in what city the picture was taken. <br>
`Macedon`
### 	On what date was this photo taken?
Scroll down to the **Meta Data** section and there will be an entry for **Create Date**. <br>
`Mon Oct 14 2019`
### 	What is the name of the business that owns the field in the image?
Refer to the first question... <br>
`Long Acre Farms`
### 	What is the value of the flag?
Scroll down to the **String Extraction** section and the 19th line should be our flag. <br>
`SKY-MAZE-1014`