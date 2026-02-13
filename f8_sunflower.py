from utills import *
def preplant(dir):
	i=0
	while True:
		plant(Entities.Sunflower)
		if measure()>7:
			harvest()
		if measure()==7:
			move(dir)
			i+=1
			if i >=10:
				break
			
preplant(W)
while True:
	plant(Entities.Sunflower)
	
	if can_harvest():
		harvest()
	elif get_water()< 0.9:
		use_item(Items.water)
	else:
		#pass
		
		use_item(Items.Fertilizer)