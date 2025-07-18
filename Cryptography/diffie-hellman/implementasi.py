p = 2089
g= 2

#one people
a = a
A = pow(g, a , p)
print(f"kunci orang pertama adalah : {A}\n")

#second people
b = 15
B = pow(g, b , p)
print(f"kunci orang kedua adalah : {B}\n")

#process shared key
OnePeopleKey = pow (B, a ,p)
SecondPeopleKey = pow (A, b, p)
print(f"shared key orang pertama adalah {OnePeopleKey} dan shared key orang kedua {SecondPeopleKey} \n")
