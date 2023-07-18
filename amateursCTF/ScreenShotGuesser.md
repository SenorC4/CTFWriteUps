## Name: Sen0rC4
## Challenge Name: ScreenshotGuesser
## Category: OSINT
## Points: 454**


## Challenge:

I screenshotted a list of wifi networks on vacation but forgot where I was at.
To check your coordinates use the provided server (pass in format x, y, example: 123.456789, -123.456789).
"try to look at the direction ish in which stuff becomes more clustered" - author, note: we relaxed the coordinate precision as an update.
You should be able to solve this in a manageable amount of guesses.
nc amt.rs 31450

## Approach:

I first looked at the most unique BSSIDs. This usually will be the longest network name, in this case “PRIMAVERA FOUNDATION 5G_2.4GEXT”. 

I found that Primavera Foundation is only in Tucson, AZ.

I used Wigle.net to get the longitude and latitude of all PRIMAVERA networks

In the same map view of PRIMAERA, I then used the strongest signal wireless network to find a more accurate coordinate to submit, for this I used the CenturyLink network.

I then computed the proof of work and the coordinates and received the flag.








