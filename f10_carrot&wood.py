from utills import *
#多线程生产
#虽然不知道为什么目前只能单线程运行
def drone_func():
	change_hat(Hats.Wizard_Hat)
	do_a_flip()
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				if (get_pos_y()%2==0 and get_pos_x()%2==0)or  (get_pos_y()%2==1 and get_pos_x()%2==1):
					plant(Entities.Tree)
				else:
					plant(Entities.Carrot) 
				move(S)
			move(A)
#
tillall()
spawn_drone(drone_func())
print(num_drones())
flag=0
while True:
	if spawn_drone(drone_func()) and flag==0:
		flag=1
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if (get_pos_y()%2==0 and get_pos_x()%2==0)or  (get_pos_y()%2==1 and get_pos_x()%2==1):
				plant(Entities.Tree)
			else:
				plant(Entities.Carrot) 
			move(W)
		move(D)