from utills import *
def muddy_farm():
	a=get_world_size()
	while True:
		for i in range(a):
			for j in range(a):
				if get_water()< 0.5:
					use_item(Items.water)
				else:
					move(North)
			move(East)
def reverse_cactus(x,y,mode):
	#未测试
	sorted = False
	i=0
	if mode=='y':
		while sorted == False:
			if get_pos_y() == y:
				goto(get_pos_x(),0)		
			if measure() > measure(S):
				swap(S)
				i=0
			move(S)
			i=i+1
			if i == y:
				sorted=True
	else:
		while sorted == False:
			if get_pos_x() == x:
				goto(0,get_pos_y())
			if measure() > measure(A):
				swap(A)
				i=0
			move(A)
			i=i+1
			if i == x:
				sorted=True