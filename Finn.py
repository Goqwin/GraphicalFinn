from SimpleGraphics import *

# Set up the background color and window size
w = 800
h = 700
background("lawn green")
resize(w, h)

# Define the dimensions and offsets for Finn's drawing
offsetx = w // 2 - 400
offsety = h // 2 - 350

# Get user input for x and y coordinates
input_x = int(input("Enter the x-coordinate: "))
input_y = int(input("Enter the y-coordinate: "))

# Calculate the centered x and y coordinates
x = offsetx + input_x
y = offsety + input_y

# Bunny Ears
offsetbunnyx = 130
offsetbunnyy = 65
w_bunny = 117
h_bunny = 202
setFill("white")
setOutline("black")
ellipse(x + offsetbunnyx, y + offsetbunnyy, w_bunny, h_bunny)

offsetbunnyx2 = 613
offsetbunnyy2 = 65
setFill("white")
setOutline("black")
ellipse(x + offsetbunnyx2, y + offsetbunnyy2, w_bunny, h_bunny)

offsethatx = 130
offsethaty = -120
w_hat = 600
h_hat = 400
rect(x + offsethatx, y - offsethaty, w_hat, h_hat)

offsetfacex = 200
offsetfacey = -140
w_face = 425
h_face = 355
setFill("khaki")
setOutline("black")
ellipse(x + offsetfacex, y - offsetfacey, w_face, h_face)

offseteyesx = 250
offseteyesy = 210
setFill("black")
setOutline("black")
w_eyes = 115
h_eyes = 110
ellipse(x + offseteyesx, y + offseteyesy, w_eyes, h_eyes)

offseteyesx1 = 450
offseteyesy1 = 208
setFill("black")
setOutline("black")
ellipse(x + offseteyesx1, y + offseteyesy1, w_eyes, h_eyes)

# LEFT SIDE OF EYE
offseteyeswhitex = 250
offseteyeswhitey = 240
w_eyeswhite = 50
h_eyeswhite = 60
setFill("white")
setOutline("black")
ellipse(x + offseteyeswhitex, y + offseteyeswhitey, w_eyeswhite, h_eyeswhite)

offseteyeswhitex1 = 320
offseteyeswhitey1 = 215
w_eyeswhite1 = 20
h_eyeswhite1 = 20
setOutline("black")
setFill("white")
ellipse(x + offseteyeswhitex1, y + offseteyeswhitey1, w_eyeswhite1, h_eyeswhite1)

# RIGHT SIDE OF EYE
offseteyeswhitex2 = 500
offseteyeswhitey2 = 210
w_eyeswhite2 = 20
h_eyeswhite2 = 20
setOutline("black")
setFill("white")
ellipse(x + offseteyeswhitex2, y + offseteyeswhitey2, w_eyeswhite2, h_eyeswhite2)

offseteyeswhitex3 = 450
offseteyeswhitey3 = 240
w_eyeswhite3 = 50
h_eyeswhite3 = 60
setOutline("black")
setFill("white")
ellipse(x + offseteyeswhitex3, y + offseteyeswhitey3, w_eyeswhite3, h_eyeswhite3)

# THIS CODES FOR THE MOUTH
offsetx_mouth = 300
offsety_mouth = 310
s_m = 180
e_m = 180
setFill("firebrick")
setOutline("black")
w_m = 185
h_m = 150
pieSlice(x + offsetx_mouth, y + offsety_mouth, w_m, h_m, s_m, e_m)

# THIS CODES FOR THE TEETH
offsetteeth1x = 299
offseteeth1y = 364
w_t1 = 60
h_t1 = 40
setFill("white")
setOutline("black")
s_t1 = 180
e_t1 = 180
pieSlice(x + offsetteeth1x, y + offseteeth1y, w_t1, h_t1, s_t1, e_t1)

offsetteeth2x = 425
offsetteeth2y = 364
w_t2 = 60
h_t2 = 40
setFill("white")
setOutline("black")
s_t2 = 180
e_t2 = 180
pieSlice(x + offsetteeth2x, y + offsetteeth2y, w_t2, h_t2, s_t2, e_t2)

# THIS CODES FOR THE TONGUE
offsettonguex = 370
offsettonugey = 439
s_ton = 0
e_ton = 175
w_tong = 50
h_tong = 40
setFill("dark red")
setOutline("black")
pieSlice(x + offsettonguex, y + offsettonugey, w_tong, h_tong, s_ton, e_ton)

# THIS CODES FOR THE STRUCTURE OF THE BODY
offsetbodx = 125
offsetbody = 510
w_body = 620
h_body = 200
setFill("cyan")
setOutline("black")
rect(x + offsetbodx, y + offsetbody, w_body, h_body)

# THIS CODES FOR FINN'S LEFT ARM & HANDS
offset_left_shirtx = 100
offset_left_shirty = 505
w_shirtleft = 70
h_shirtleft = 90
setFill("cyan")
setOutline("black")
ellipse(x + offset_left_shirtx, y + offset_left_shirty, w_shirtleft, h_shirtleft)

offset_handx = 100
offset_handy = 515
w_hand = 60
h_hand = 90
setFill("khaki")
setOutline("black")
ellipse(x + offset_handx, y + offset_handy, w_hand, h_hand)

# THIS CODES FOR THE THUMB
offsetthumbx = 115
offsetthumby = 515
w_thumb = 20
h_thumb = 35
s_thumb = 180
e_thumb = -270
setOutline("black")
setFill("black")
arc(x + offsetthumbx, y + offsetthumby, w_thumb, h_thumb, s_thumb, e_thumb)

# This codes for the 2 fingers
offsetx_finger = 100
offsety_finger = 540
w_finger = 15
h_finger = 30
s_finger = 180
e_finger = -260
setOutline("black")
setFill("black")
arc(x + offsetx_finger, y + offsety_finger, w_finger, h_finger, s_finger, e_finger)

offsetx_finger2 = 105
offsety_finger2 = 574
w_finger2 = 15
h_finger2 = 28
s_finger2 = 180
e_finger2 = -270
setOutline("black")
setFill("black")
arc(x + offsetx_finger2, y + offsety_finger2, w_finger2, h_finger2, s_finger2, e_finger2)

# THIS CODES FOR FINN'S RIGHT ARM
offsetrightx = 720
offsetrighty = 490
w_right = 70
h_right = 110
setFill("cyan")
setOutline("black")
ellipse(x + offsetrightx, y + offsetrighty, w_right, h_right)

offsetrightarmx = 722
offsetrightarmy = 570
w_rightarm = 60
h_rightarm = 120
setFill("khaki")
setOutline("black")
rect(x + offsetrightarmx, y + offsetrightarmy, w_rightarm, h_rightarm)

# Comment/quirky dialogue
offsettextx = 300
offsettexty = 50
setFont("time", "12", "bold")
text(x + offsettextx, y + offsettexty, "The name's Finn, what's yours?")

# Credits and ownership
offsetsignx = 700
offsetsigny = 590
setFont("time", "8", "bold")
text(x + offsetsignx, y + offsetsigny, "Made by: Godwin JB Mercado")


