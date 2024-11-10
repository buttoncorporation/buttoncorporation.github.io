def CalculateExpectedValue(SlotPattern,Spins=60/1.9*10): #Defaults to 10 minutes
	Value=0
	CurrentSpins=0
	for x in SlotPattern:
		for y in SlotPattern:
			for z in SlotPattern:
				if x==y and y==z:
					#Regular win
					Value+=1
				if x==0 and y==0 and z==0:
					#Peepo win
					Value+=99
				CurrentSpins+=1
	return Value*Spins/CurrentSpins

print("Regular value over 10 minutes:")
print(CalculateExpectedValue([0,1,1,1,2,2,2,3,3,3]))
print("Peepo2x value over 10 minutes:")
print(CalculateExpectedValue([0,0,1,1,1,2,2,2,3,3,3]))