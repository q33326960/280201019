m = eval(input("Mesafe ? (km) "))
v1 = eval(input("Velocity 1 (km/h) ? "))
v2 = eval(input("Velocity 2 (km/h) ? "))
y = eval(input("Arada kalan mesafe (km) ? "))
t = (m-y) / (v1 + v2) *60
print("Geçen süre", t , "dakika")
# Enter 490, 70, 80, 150 and you should get 136.0 #
