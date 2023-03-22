simbolo = '*'
print(simbolo)
for i in range(5):
   simbolo += "*"
   print(simbolo)


for i in range(10):
    j=0
    print(i, end='')
    
    while (j<=i):
        print("* ", end="")
        j +=1
    print()

print("\n\n")