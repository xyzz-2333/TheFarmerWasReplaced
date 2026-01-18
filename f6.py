#暴力种南瓜
p=0
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if p>=36:
				harvest()
			if can_harvest():
				move(North)
				p=p+1
			else:
				p=0
				plant(Entities.Pumpkin)
				move(North)
		move(East)