it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print("Print length of it_companies:")
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.add("Samsung")
it_companies.add("Intel")
it_companies.add("AMD")
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Facebook")
print(it_companies)

#Join A and B
C = A | B
print(C) 

#Find intersection of A and B
D = A & B
print(D)

#Joining A with B and B with A
E = A | B
F = B | A
print(E)
print(F)

#What is the symmetric difference between A and B
G = B - A
print(G)

#Delete the sets completely
A.clear()
B.clear()
print(A)
print(B)

#Convert the ages to a set and compare the length of the list and the set.
ageset = set(age)
print(len(age))
print(len(ageset))