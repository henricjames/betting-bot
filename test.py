import uiautomator2 as u2
d = u2.connect()
print(d)

cordinates={"andar":[0.338, 0.54],"bahar":[0.696, 0.56]}

amount_cordinates={10:[0.292, 0.907],50:[0.384, 0.918],100:[0.48, 0.914],500:[0.572, 0.914],1000:[0.662, 0.918]}

def  bet_10(side):
    d.click(0.32, 0.908)
    d.click(cordinates[side][0],cordinates[side][1])

def  bet_20(side):
    d.click(0.32, 0.908)
    d.click(cordinates[side][0],cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def  bet_40(side):
    d.click(0.32, 0.908)
    d.click(cordinates[side][0],cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

print(amount_cordinates[10][0])

