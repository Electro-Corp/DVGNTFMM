print("calculator moment...")
MolarMass = int(input("Molar Mass of element 1: "))
MMS = int(input("Molar Mass of element 2: "))
MolarMass3 = int(input("Molar mass of product: "))
GramsOf1 = int(input("Grams of element 1: "))
GramsOf2 = int(input("Grams of element 2: "))


b = int(input("Balancer 1 (ex: the 2 in 2H3): "))
b2 = int(input("Balancer 2 (ex: the 2 in 2H3): "))
b3 = int(input("Balancer 3 (ex: the 2 in 2H3): "))
c3 = GramsOf1/MolarMass
c23 = GramsOf2/MMS

print("here ye are:")
if (c3*b)<(c23*b2):
  print(((c3*b3)*MolarMass3)/b)
else:
  print(((c23*b3)*MolarMass3)/b2)
  