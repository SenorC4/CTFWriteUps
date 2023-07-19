**Name: Sen0rC4**

**Challenge Name: MinceRaft**

**Category: Forensics**

**Points: 449**



## Challenge:

I found these suspicious files on my minecraft server and I think there's a flag in them. I'm not sure where though.
Note: you do not need minecraft to solve this challenge. Maybe reference the minecraft region file format wiki?


## Approach:

1. Research .mca files using the minecraft region file format wiki
2. Look for a tool that can parse the data stored in the region files
3. Find and download *NBT Explorer* (https://github.com/jaquadro/NBTExplorer/tree/v2.8.0-win)
4. Open the four region files with NBT Explorer
5. Use *find* on each mca file looking for flag format “amateursCTF{”
6. Flag: `amateursCTF{cow_wear_thing_lmao_0f9183ca}`

   










