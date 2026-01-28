from utills import *
x,y=5,5
sorted=False
while sorted == False:
	
	if get_pos_y() == y:
		goto(get_pos_x(),0)
	if measure() > measure(W):
		swap(W)
	move(W)