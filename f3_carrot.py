#需要解锁感知，自动耕地并生产萝卜
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type()!= Grounds.Soil:
				till()
			if can_harvest():
				harvest()
			plant(Entities.Carrot)
			move(North)	
		move(East)