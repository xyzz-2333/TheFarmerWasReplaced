from utills import *
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
while True:
	if get_pos_x() == x and get_pos_y() == y:
		if get_entity_type() == Entities.Treasure:
			respawn_maze()
			break        
	if can_move(directions[index]):
		move(directions[index])
	elif can_move(directions[right(index)]):
		move(directions[right(index)])
		index = right(index)
	elif can_move(directions[left(index)]):
		move(directions[left(index)])
		index = left(index)

	else: 
		index=right(index)
		#print('no way')