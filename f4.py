#树和灌木,优化空间不小
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()			
			if (get_pos_y()%2==0 and get_pos_x()%2==0)or  (get_pos_y()%2==1 and get_pos_x()%2==1):
				plant(Entities.Tree)
			else:
				plant(Entities.Bush) 

			move(North)
		move(East)
			