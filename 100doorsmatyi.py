door = ["0"] * 100
open=" "

for i in range(len(door)):
    
    for j in range(i, len(door), i+1):
        if door[j] == "0":
            door[j] = "1"
        
        elif door[j] == "1":
                door[j] = "0"

for i in range(len(door)):
    
    if door[i] == "1":
            open += (" " + str(i+1))

print("The following doors are open:", open)