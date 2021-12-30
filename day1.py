with open("./input.txt", "r") as f:
  depths = [int(i) for i in f.readlines()]

increases = 0
for i in range(len(depths) - 1):
  inc = depths[i+1] - depths[i]
  if inc > 0:
    increases += 1

print(increases)
