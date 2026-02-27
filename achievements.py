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
	#已测试
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
def achievement_reverse_cactus():
	set_world_size(4)
	tillall()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant(Entities.Cactus)
			move(North)
		move(East)
	x,y=get_world_size(),get_world_size()
	for i in range(x):
		reverse_cactus(x,y,'y')
		goto(get_pos_x()+1,0)
	for i in range(y):
		reverse_cactus(x,y,'x')
		goto(0,get_pos_y()+1)
achievement_reverse_cactus()