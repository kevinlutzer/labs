file = open("input.txt","r")
lines = file.readlines()
ans = 0

for line in lines:
    gameValid = True
    line = line.replace(";"," ")
    line = line.replace(","," ")
    words = line.split()
    
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    
    numberOfCubes = 0
    for word in words:
        if word.isnumeric():
            numberOfCubes = int(word)
        
        elif word in ["red","green","blue"]:
            if word == "red" and maxRed < numberOfCubes:
                maxRed = numberOfCubes
                
            elif word == "green" and maxGreen < numberOfCubes:
                maxGreen = numberOfCubes
                
            elif word == "blue" and maxBlue < numberOfCubes:
                maxBlue = numberOfCubes

    power = maxRed * maxGreen * maxBlue
    print(power)
    ans += power
    
file.close()
print(ans)

# Bro part 2 was so fucking easy compared to part 1