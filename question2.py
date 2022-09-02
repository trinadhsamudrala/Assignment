# Create an empty dictionary called dog
print("Empty dictionary")
dog = {} #empty Dictionary
print(dog) #print dictionary
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Bruno'
dog['color'] = 'black'
dog['breed'] = 'Husky'
dog['legs'] = '4'
dog['age'] = '3'
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print("Empty student dictionary")
student = {}
student['first_name'] = 'James'
student['last_name'] = 'Maddison'
student['gender'] = 'M'
student['age'] = '40'
student['marital_status'] = 'Single'
student['skills'] = ['programming','basketball']
student['country'] = 'India'
student['city'] = 'New Delhi'
student['address'] = 'New Delhi'
print(student)

# Get the length of the student dictionary
print('Student Dictionary length') #length of the student dictionary
print(len(student))

print("value of skills and the data type, as a list")
print(type(student['skills']))

#Modify the skills values by adding one or two skills
print("adding skills values by adding skills") #adding skills values by adding one or two skills
student['skills'].append('Languages')
student['skills'].append('Athletics')
print(student['skills'])

#Dictionary keys as a list
print(student.keys())
 #Dictionary values as a list
print(student.values())
