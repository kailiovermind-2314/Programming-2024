delivered = int(input())
collisions = int(input())
points = delivered * 50 - collisions * 10 

print(points + 500 if delivered > collisions else points)