from utills import *

change_hat(Hats.Gold_Hat)
spawn_maze()

directions = [W,D,S,A]
index = 0
def right(index):
	return (index + 1) % 4
def left(index):
	return (index -1) % 4
def back(index):
	return (index + 2) % 4
x,y=measure()
t=get_time()
while True:
	if get_pos_x() == x and get_pos_y() == y:
		if get_entity_type() == Entities.Treasure:
			respawn_maze()
			x,y=measure()
			t=get_time()
			continue       
	if can_move(directions[right(index)]):
		move(directions[right(index)])
		index = right(index)
	elif can_move(directions[index]):
		move(directions[index])
		
	elif can_move(directions[left(index)]):
		move(directions[left(index)])
		index = left(index)

	elif can_move(directions[back(index)]): 
		index = back(index)
	elif get_time() - t > 50:
		clear()
		spawn_maze()
		x,y=measure()
		t=get_time()
	else:	
		print('状态异常')