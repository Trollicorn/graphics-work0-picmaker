import math

pix = "P3 500 500 255\n"

for r in range(500):
    for c in range(500):
        pix += str(r*c % 255) + " " + str(r * r * int(100*math.cos(c)) % 255) + " " + str((r^2+c^3) % 255) + " "
    pix += "\n"

pic = open("art.ppm","w")
pic.write(pix)
pic.close()
