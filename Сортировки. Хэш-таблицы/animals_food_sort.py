def feedAnimals(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in range (len(food)):
        if food[f] >= animals[count]:
            count=count+1
        if count == len(animals):
            break
    return count

animals = [8,2,3,2]
food = [1,4,3,8]
print(feedAnimals(animals, food))