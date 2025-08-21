import math

no = 1
yes = 2
total = no+yes

entropy = -(yes/total*math.log2(yes/total) + no/total*math.log2(no/total))

print(entropy)

# e = 0.9402
# g = e - (1 + 0.9182 + 0.8112)
# print(g)