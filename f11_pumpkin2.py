from utills import *
def pumpkin_func(x,y):
	listx=[]
	listy=[]
	while True:    
		for i in range(6):
			for j in range(6):
				if get_ground_type()!= Grounds.Soil:
					till()
				elif get_ground_type()== Grounds.Soil:	 
					plant(Entities.Pumpkin)
					if get_water()==0:
						use_item(Items.Water)
				move(W)
			move(D)
		goto(x,y)        
		for i in range(6):
			for j in range(6):   
				if can_harvest():
					continue
				if not can_harvest():
					listx.append(get_pos_x())
					listy.append(get_pos_y())
				move(W)
			move(D)            
		for i in range(len(listx) - 1, -1, -1): # 从后往前遍历
			goto(listx[i], listy[i])
			if can_harvest():
				# 从后往前删除，不会影响前面元素的索引
				listx.pop(i)
				listy.pop(i)
			elif not can_harvest():
				plant(Entities.Pumpkin)
				continue
			if listx == []:
				harvest()

pumpkin_func(0,0)