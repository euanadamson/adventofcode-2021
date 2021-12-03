input_file = open("day3_input.txt", "r")
nums = input_file.read().splitlines()

# Part 1

length = len(nums[0])

gamma = ""
for i in range(length):
    col = "".join(num[i] for num in nums)
    if col.count("0") > col.count("1"):
        gamma += "0"
    else:
        gamma += "1"
        
epsilon = gamma.replace('0', 'x').replace('1', '0').replace('x', '1')
gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

pwr = gamma_int * epsilon_int
print(pwr)

# Part 2

length = len(nums[0])

o2 = set(nums)
for i in range(length):
    col = "".join(num[i] for num in o2)
    if col.count("0") <= col.count("1"):
        bit = "1"
    else:
        bit = "0"

    o2 = o2 - set(num for num in o2 if num[i] == bit)
    if len(o2) == 1:
        o2 = int(max(o2), 2)
        break

co2 = set(nums)
for i in range(length):
    col = "".join(num[i] for num in co2)
    if col.count("0") > col.count("1"):
        bit = "1"
    else:
        bit = "0"

    co2 = co2 - set(num for num in co2 if num[i] == bit)
    if len(co2) == 1:
        co2 = int(max(co2), 2)
        break

print(o2*co2)
