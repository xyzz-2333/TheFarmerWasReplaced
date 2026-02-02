#仙人掌
from utills import *
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Cactus)
		move(North)
	move(East)
x,y=get_world_size(),get_world_size()
sorted=False
#goto(get_pos_x(),0)
for i in range(x):
	cactus_sort_1_0(x,y,'y')
	goto(get_pos_x()+1,0)
for i in range(y):
	cactus_sort_1_0(x,y,'x')
	goto(0,get_pos_y()+1)
harvest()
