import sys

if len(sys.argv) != 3:
    print("Usage: python healthy_herb.py color place")
    exit()

print(sys.argv)

color = sys.argv[1]
place = sys.argv[2]
print("color: {}\nplace: {}".format(color, place))
