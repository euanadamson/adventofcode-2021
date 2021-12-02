input_file = open("day2_input.txt", "r")
movements = input_file.read().splitlines()

horizontal = 0
vertical = 0

for i in movements:
    if i[0] == 'f':
        horizontal += int(i[-1])
    elif i[0] == 'd':
        vertical += int(i[-1])
    elif i[0] == 'u':
        vertical -= int(i[-1])
    else:
        pass

final_pos = horizontal * vertical
print(final_pos)

horizontal = 0
vertical = 0
aim = 0
  
for i in movements:
    if i[0] == 'f':
        horizontal += int(i[-1])
        vertical += aim * int(i[-1])
    elif i[0] == 'd':
        aim += int(i[-1])
    elif i[0] == 'u':
        aim -= int(i[-1])
    else:
        pass
    
final_pos = horizontal * vertical
print(final_pos)
