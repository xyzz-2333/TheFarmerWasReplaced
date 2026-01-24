def move_n_dir(n, dir):
	#向指定方向连续移动
	for i in range(n):
		move(dir)
def tillall(mode='till'):
	#全图改地形
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
	#全图收割
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)	
		move(East)
def goto(x=0,y=0):
	#前往指定坐标，左下角为0，0
	#还有优化空间
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
def snake_bubble_sort(l=get_world_size(),):
	for row in range(l):
		if row%2==0:
			for col in range(l):
				if col<l-1 and measure()> measure(East):
					swap(East)
			for col in range(l):
				if col>0 and measure()> measure(West):
					swap(West)	
def swap_L(index1,index2):
	
	pass
def setarea(x1,y1,x2,y2):
	if x1>get_world_size() or y1>get_world_size() :
		print('out of index')
	
	return (x1,y1,x2,y2)
		
		
	
