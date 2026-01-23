#快速刷草，需要水
while True:
	if can_harvest():
		harvest()
	if get_water()<0.75:
		use_item(Items.Water)