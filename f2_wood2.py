#二维，木头
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant(Entities.Bush)
			if can_harvest():
				harvest()
				
			move(North)	
		move(East)