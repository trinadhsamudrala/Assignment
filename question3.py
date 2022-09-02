#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Ryan", "Billy")
print("brothers:",brothers)
sisters = ("Nicole", "Ashley")
print("sisters:",sisters)

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("siblings:",siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Jerry", "Mona")
print(" Whole Family names:",family_members)