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
lowercase = animal.lower()
lowercase = list(lowercase)
random.shuffle(lowercase)
s = "-"
lowercase = s.join(lowercase)
uppercase = animal.upper()
uppercase = list(uppercase)
random.shuffle(uppercase)
uppercase = ' '.join(uppercase)
# convert to spongebob case: 
spongebob = list(animal) 
random.shuffle(spongebob) 
for i in range(len(spongebob)):
    if i % 2 == 0:  
        spongebob[i] = spongebob[i].upper()
    else:  
        spongebob[i] = spongebob[i].lower()
spongebob = ' '.join(spongebob)

print("\t\t\t\t\t\t\t\t"+lowercase)
print("\t\t\t\t\t\twho")
print("   a)s w(e loo)k")
print("  upnowgath")
print("\t\t\t\t\t\t"+uppercase)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\teringint(o-")
print("  aThe):l")
print("\t\t\t\teA")
print("\t\t\t\t\t!p:")
print("S                                                                        a")
print("\t\t\t\t\t\t\t\t\t(r")
print("  rIvInG                              ."+spongebob+")")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tto")
print("  rea(be)rran(com)gi(e)ngly")
print("  ,"+animal+";")
