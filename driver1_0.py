def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
def tillall(mode='till'):
	#
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if mode=='till':
				if get_ground_type() != Grounds.Soil:
					till()
				move(North)	
			elif mode=='back':
				if get_ground_type() == Grounds.Soil:
					till()
				move(North)	
		move(East)	
def harvestall():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)	
		move(East)
def goto(x=0,y=0):
	#前往指定坐标，左下角为0，0
	selfx,selfy=get_pos_x(),get_pos_y()
	#print(selfx,selfy)
	dx,dy=selfx-x,selfy-y
	#print(dx,dy)
	if dx==0:
		pass
	elif dx>0:
		move_n_dir(dx,West)
	else:
		move_n_dir(abs(dx),East)
	if dy==0:
		pass
	elif dy>0:
		move_n_dir(dy,South)
	else:
		move_n_dir(abs(dy),North)
def swap_L(index1,index2):
	
	pass
def setarea(begin,x,y):
	if x>get_world_size() or y>get_world_size() :
		print('out of index')
		
	
		