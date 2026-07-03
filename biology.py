# Program to determine the type of an animal
# Mutshidzi Nemalili
# 02 March 2024

print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")
type_of_skeleton = input('The skeleton is(internal/external)?\n')
if type_of_skeleton == "internal":
    fertilisation = input('The fertilisation of eggs occurs (within the body/outside the body)?\n')
    if fertilisation == "within the body":
        offspring_type = input('Young produced by (waterproof eggs/live birth)?\n')
        if offspring_type == "waterproof eggs": 
            skin_type = input('The skin is covered (scales/feathers)?\n')
            if skin_type == "scales":
                print('Type of animal: Reptile')
            else:
                print('Type of animal: Bird')
    
        else:
            print('Type of animal: Mammal')
    else:  
        shelter = input('The habitat of the eggs is (in water/near water)?\n')
        if shelter == "in water":
            print('Type of animal: Fish')
        else:
            print('Type of animal: Amphibian')            
      

if type_of_skeleton == "external":
    print('Type of animal: Arthropod')
    
  