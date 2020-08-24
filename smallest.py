def smallest(smallist):
    smallnumber = smallist[0]
    for x in smallist:
        if x <= smallnumber:
            smallnumber = x
    return smallnumber

print(smallest([88, 99, 43, 123, 149]))

def largest(largelist):
    largenumber = largelist[0]
    for x in largelist:
        if x >= largenumber:
            largenumber = x
    return largenumber

print(largest([99,74,2182, 132453, 122, 1]))

def shortest(stringlist):
    shortstring = ""
    for x in stringlist:
        if not shortstring or len(x) <= len(shortstring):
            shortstring = x
    return shortstring

print(shortest(["duck", "fowl", "barnyard", "owlbear", "oi vei"]))

def longest(stringlist):
    longstring = ""
    for x in stringlist:
        if len(x) >= len(longstring):
          longstring = x
    return longstring

print(longest(["quesadilla", "police brutality", "chimerism", "groupthink", "spider"]))