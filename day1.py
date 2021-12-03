input_file = open("day1_input.txt", "r")
depths = input_file.read().splitlines()
print(depths)

# Part 1

depth_increase_p1 = 0
val = 0

for i in depths:
    if val != 0:
        if val < int(i):
            depth_increase += 1

    val = int(i)

print(depth_increase_p1)

# Part 2

depth_increase_p2 = 0
depths2 = []
window_a = 0
window_b = 0

for i in depths:
    depths2.append(i)
    
while len(depths2) > 3:
    window_a = int(depths2[0])
    window_b = int(depths2[3])
    if window_a < window_b:
        depth_increase_p2 += 1
    depths2 = depths2[1:]

print(depth_increase_p2)
