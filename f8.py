while True:
	if get_water()<0.35:
		use_item(Items.Water)
	if can_harvest():
		harvest()
		move(North)