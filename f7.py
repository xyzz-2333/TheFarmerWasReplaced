#仙人掌
from utills import *

tillall()

for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Cactus)
		move(North)
	move(East)

