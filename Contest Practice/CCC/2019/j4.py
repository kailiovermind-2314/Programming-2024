from itertools import groupby

def hflip(l):
    return([l[2], l[3], l[0], l[1]])
def vflip(l):
    return([l[1], l[0], l[3], l[2]])

image = [1, 2, 3, 4]
flips = [''.join(group) for _, group in groupby(input())]
for flip in flips:
    if flip[0] == 'H':
        if (len(flip) % 2 != 0):
            image = hflip(image)
    else:
        if (len(flip) % 2 != 0):
            image = vflip(image)

print(image[0], image[1])
print(image[2], image[3])