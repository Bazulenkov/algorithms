#%%
with open('input.txt') as f:
    m = f.readline().strip()
    massiv = f.readline().split()
massiv = list(map(int, massiv))
m = int(m)

#%%

def func(massiv):
    class Best:
        def __init__(self):
            self.pos = 0
            self.sdvig = 0

        def __repr__(self):
            return {'pos':self.pos, 'sdvig':self.sdvig}

        def __str__(self):
            return 'Best(pos='+self.pos+' sdvig='+self.sdvig+')'


    best_elem = Best()
    high_i = 0
    while best_elem.sdvig + high_i < len(massiv):
        low_i = high_i + 1
        high_i = best_elem.pos + massiv[best_elem.pos]
        if low_i > high_i:
            return False

        best_elem = Best()

        for i in range(low_i, high_i+1):
            sdvig = massiv[i] + i - high_i
            if best_elem.sdvig < sdvig:
                best_elem.sdvig = sdvig
                best_elem.pos = i
                if best_elem.sdvig + high_i >= len(massiv):
                    break
    return True

print(func(massiv))
