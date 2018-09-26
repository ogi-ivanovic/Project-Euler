nums = []
trii = 1
tri = []
while (trii * (trii + 1))/2 < 10000:
    if (trii * (trii + 1))/2 >= 1000:
        tri.append(int((trii * (trii + 1))/2))
    trii += 1
sqri = 1
sqr = []
while sqri * sqri < 10000:
    if sqri * sqri >= 1000:
        sqr.append(int(sqri * sqri))
    sqri += 1
peni = 0
pen = []
while (peni * (3*peni - 1))/2 < 10000:
    if (peni * (3*peni - 1))/2 >= 1000:
        pen.append(int((peni * (3*peni - 1))/2))
    peni += 1
hexi = 1
hex = []
while hexi * (2*hexi - 1) < 10000:
    if hexi * (2*hexi - 1) >= 1000:
        hex.append(int(hexi * (2*hexi - 1)))
    hexi += 1
hepi = 1
hep = []
while (hepi * (5*hepi - 3))/2 < 10000:
    if (hepi * (5*hepi - 3))/2 >= 1000:
        hep.append(int((hepi * (5*hepi - 3))/2))
    hepi += 1
octi = 19
oct = []
while octi * (3*octi - 2) < 10000:
    oct.append(int(octi * (3*octi - 2)))
    octi += 1
nums = tri + sqr + pen + hex + hep + oct
nums = list(set(nums))
nums.sort()

cycles = []

def createCycle(cycle, round):
    if round == 6:
        if str(cycle[-1])[2:4] == str(cycle[0])[0:2]:
            cycles.append(cycle)
            return True
        return False
    possibleNextList = []
    for i in nums:
        if str(cycle[-1])[2:4] == str(i)[0:2]:
            possibleNextList.append(i)
    for possibility in possibleNextList:
        createCycle(cycle + [possibility], round + 1)

for i in nums:
    createCycle([i], 1)

def removeDuplicates(lst):
  length = len(lst)
  i = 1
  while i <= length:
    lst = lst[:i] + list(filter(lambda x: x != lst[i-1], lst[i:]))
    i += 1
    length = len(lst)
  return lst


def test(cycle):
    indices = []
    tris = [0]*6
    for i in range(6):
        if cycle[i] in tri:
            tris[i] = 1
    sqrs = [0]*6
    for i in range(6):
        if cycle[i] in sqr:
            sqrs[i] = 1
    pens = [0]*6
    for i in range(6):
        if cycle[i] in pen:
            pens[i] = 1
    hexs = [0]*6
    for i in range(6):
        if cycle[i] in hex:
            hexs[i] = 1
    heps = [0]*6
    for i in range(6):
        if cycle[i] in hep:
            heps[i] = 1
    octs = [0]*6
    for i in range(6):
        if cycle[i] in oct:
            octs[i] = 1
    for i in range(6):
        if sum(tris) == 0 or sum(sqrs) == 0 or sum(pens) == 0 or sum(hexs) == 0 or sum(heps) == 0 or sum(octs) == 0:
            return False
        if tris[i] == 0 and sqrs[i] == 0 and pens[i] == 0 and hexs[i] == 0 and heps[i] == 0 and octs[i] == 0:
            return False
        if len(removeDuplicates([tris, sqrs, pens, hexs, heps, octs])) != 6:
          return False
    return cycle

for i in cycles:
    cycle = test(i)
    if cycle != False:
        print(sum(cycle))
        break
