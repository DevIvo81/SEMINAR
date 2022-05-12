import os
os.system("cls")

brojke = []

for i in range(120, 355, 5):
    brojke.append(i/10)
    
print(*brojke, sep=', ')