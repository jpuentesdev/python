#https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
def get_sum(a,b):
    if a == b:
        return a
    small, big = sorted ([a,b])
    return sum ([i for i in range(small, big + 1) ])
        
print(get_sum(-21,-88))



#Hecho por pro
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(-21,-88))