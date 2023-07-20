**Name: Sen0rC4**

**Challenge Name: ScreenshotGuesser**

**Category: OSINT**

**Points: 454**



## Challenge:

I screenshotted a list of wifi networks on vacation but forgot where I was at.
To check your coordinates use the provided server (pass in format x, y, example: 123.456789, -123.456789).
"try to look at the direction ish in which stuff becomes more clustered" - author, note: we relaxed the coordinate precision as an update.
You should be able to solve this in a manageable amount of guesses.
nc amt.rs 31450

[screenshot.png](files/screenshot.png)

## Approach:

1. I searched for the most unique BSSIDs in the provied screenshot. This usually will be the longest network name, in this case “PRIMAVERA FOUNDATION 5G_2.4GEXT”. 

2. Using google maps I found that Primavera Foundation's only locations are all in Tucson, AZ.

3. I used Wigle.net (a [wardriving](https://en.wikipedia.org/wiki/Wardriving) database) to get the longitude and latitude of all PRIMAVERA networks

4. In the same geological area of the PRIMAERA networks, I then used the strongest signal wireless network to find a more accurate coordinate to submit, for this I used the CenturyLink network.

5. I then computed the proof of work and the coordinates and received the flag.

Flag: `amateursCTF{p01nt_mast3r}`









