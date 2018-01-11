import cs50

while True:
    print ("Height: ", end="")
    height = cs50.get_int()
    if height>=0 and height<23:
        break

length=2*height-1

print ("icreadible pyramide")

for i in range (height):
    spaces=length-2*i-1
    s=int(spaces/2)
    hashes=length-spaces
    print(" " * s, end="")
    print("#" * hashes, end="")
    print(" " * s, end="")
    print()