# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min_age = min(ages)
print("Minimum age:",min_age)

# Add the min age and the max age again to the list
max_age = max(ages)

print("Maximum age:",max_age)

#Adding the min age and the max age again to the list
print("Adding max and min ages to list")
ages.insert(0, 19)
ages.insert(11, 26)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
print("Median Age is:",(ages[6]-ages[5])/2+ages[5])

#Find the average age (sum of all items divided by their number)
print("The Average age is",sum(ages)/len(ages))

#Find the range of the ages (max minus min)
print("Range of ages is",ages[11]-ages[0])