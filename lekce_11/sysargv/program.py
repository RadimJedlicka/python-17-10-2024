import sys

print("Jméno spuštěného programu:", sys.argv[0])
if len(sys.argv) > 1:
    print("Byl předán argument:", sys.argv[1])
else:
    print("Nebyl předán žádný argument.")