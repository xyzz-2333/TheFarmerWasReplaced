#木头
while True:
	plant(Entities.Bush)
	move(North)
	if can_harvest():
		harvest()
		
	