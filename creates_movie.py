import os

# frame rates is a squared number
# if you want a frame rate of 12 frames per second, you put 144

# start number is the year you want it to start at
# if there's a break, eg, a year no one is alive,
# you'll have to create two mp4s and join them.

os.system('ffmpeg -f image2 -framerate 1 -start_number 1973 -i "frame_%d.png" -vcodec mpeg4 -y "output1973.mp4"')
