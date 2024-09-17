#sidewalk = input("tell me a place: ")
#street = input("tell me a related place: ")
#print("There is a place where the "+sidewalk+" ends")
#print("And before the "+street+" begins,")
#print("And there the grass grows soft and white,")
#print("And there the sun burns crimson bright,")

#bird = input("name a bird:  ")

#print("I saw a "+bird+" fly down the street last week")

'''
I heard a Fly buzz -- when I died --
The Stillness in the Room
Was like the Stillness in the Air --
Between the Heaves of Storm --

The Eyes around -- had wrung them dry --
And Breaths were gathering firm
For that last Onset -- when the King
Be witnessed -- in the Room --

I willed my Keepsakes -- Signed away
What portion of me be
Assignable -- and then it was
There interposed a Fly --

With Blue -- uncertain stumbling Buzz --
Between the light -- and me --
And then the Windows failed -- and then
I could not see to see --
'''
import random

animal = input("Name an Animal:    ")
lowercase = []
for i in range(len(animal)):
    animal = animal.lower()
    lowercase.append(animal[i])
uppercase = []
for i in range(len(animal)): 
    animal = animal.upper()
    uppercase.append(animal[i])
    
an1 = random.shuffle(lowercase)
an2 = random.shuffle(uppercase)
#an3 = random.shuffle(spongebobcase)

# convert to spongebob case: 
for letter in animal: 
    an3 = []
    if letter.index() % 2 == 0: # first bug here.
        an3.append(letter.upper())
    else: an3.append(letter.lower())
print(an3)
print("\t\t\t\t\t\t\t\tr-p-o-p-h-e-s-s-a-g-r")
print("\t\t\t\t\t\twho")
print("   a)s w(e loo)k")
print("  upnowgath")
print("\t\t\t\t\t\tPPEGORHRASS")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\teringint(o-")
print("  aThe):l")
print("\t\t\t\teA")
print("\t\t\t\t\t!p:")
print("S                                                                        a")
print("\t\t\t\t\t\t\t\t\t(r")
print("  rIvInG                              .gRrEaPsPhOs)")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tto")
print("  rea(be)rran(com)gi(e)ngly")
print("  ,"+animal+";")




