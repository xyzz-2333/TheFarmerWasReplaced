def preplant():
	while True:
		plant(Entities.Sunflower)
		if measure()>7:
			harvest()
		if measure()==7:
			break
			
#preplant()
while True:
	plant(Entities.Sunflower)
	
	if can_harvest():
		harvest()
	elif get_water()< 0.75:
		use_item(Items.water)
	else:
		pass
		
		#use_item(Items.Fertilizer)