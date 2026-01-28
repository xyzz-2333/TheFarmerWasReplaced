from utills import *
x,y=5,5
sorted=False
while sorted == False:
	
	if get_pos_x() == x:
		goto(0,get_pos_y())
	if measure() > measure(D):
		swap(D)
	move(D)