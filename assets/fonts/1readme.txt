
I was looking for a good small font to display on a couple of RGB Matrix. (6mm and 3mm) 

Spent some time converting a bunch of fonts to BDF files using the excellent article here:

https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display

Some success.  FYI 6-7 pt (6-8px) fonts are the limit.  5 pt is unreadable.

Only attached the BDFs *most* are stripped of anything above 127 char.  (I think)

The BDF are labeled with <n>pt or <n>px based on how I did the conversion.  At first I used FontForge, but then I moved to the command line otf2bdf (Linux) to speed up the process.  
otf2bdf are all the <n>pt versions.

Some of the fonts are very limited in the char set.  (Like PressStart2P)

Enjoy

L Bilello 8/9/2023