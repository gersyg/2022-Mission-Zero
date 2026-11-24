from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(270)

from time import sleep

humid = sense.get_humidity()

w = (0,89,179)

b = (0,128,255)

o = (204,204,0)

r = (51,102,0)

y = (255,255,255)

sense.show_message("Greetings from the 2nd Gymnasium of Chaidari", scroll_speed=0.052, text_colour=w)

picture = [

   w, w, w, w, b, o, y, o,
 
   w, b, w, w, w, w, o, y,

   w, w, w, b, w, w, w, o,

   w, w, r, w, w, b, w, w,

   w, b, w, r, w, r, w, w,

   w, w, w, w, r, w, w, r,

   w, w, w, w, r, w, w, b,

   r, r, r, r, r, r, r, r,

   ]

sense.set_pixels(picture)

sleep(3)

humid = round(sense.get_humidity(), 1)

sense.show_message( "The humidity is at" + str(humid) + " %", scroll_speed=0.052, text_colour=w) 
