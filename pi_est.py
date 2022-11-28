import random
 
n = 1000000
 
inside_points = 0
outside_points = 0

for i in range(n):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
 
    origin_dist = rand_x**2 + rand_y**2 
    if origin_dist <= 1:
        inside_points += 1
 
    outside_points += 1
    pi = 4 * inside_points / outside_points

print("Pi= ", pi)
