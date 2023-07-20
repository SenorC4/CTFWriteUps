**Name: Sen0rC4**

**Challenge Name: MinceRaft**

**Category: Forensics**

**Points: 449**



## Challenge:

I found these suspicious files on my minecraft server and I think there's a flag in them. I'm not sure where though.
Note: you do not need minecraft to solve this challenge. Maybe reference the minecraft region file format wiki?
[r.1.135.mca](files/r.1.135.mca) [r.1.136.mca](files/r.1.136.mca) [r.2.135.mca](files/r.2.135.mca) [r.2.136.mca](files/r2.136.mca)


## Approach:

1. Research .mca files using the minecraft region file format wiki

2. Discover that .mca files hold minecraft chunk data (could contain a nametag or book)
   
3. Look for a tool that can parse the data stored in the region file

4. Find and download *NBT Explorer* (https://github.com/jaquadro/NBTExplorer/tree/v2.8.0-win)

5. Open the four region files with NBT Explorer

6. Use *find* on each mca file looking for flag format “amateursCTF{”
   
7. Flag: `amateursCTF{cow_wear_thing_lmao_0f9183ca}`

   










