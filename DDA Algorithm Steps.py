# DDA Algorithm Steps
print("-DDA Algorithm-")

x1 = float(input("Enter value for x1: "))
y1 = float(input("Enter value for y1: "))
x2 = float(input("Enter value for x2: "))
y2 = float(input("Enter value for y2: "))

i = 0

arry=[]
arrx=[]
arrResult=[]
arrPlot=[]


dx = x2 - x1
dy = y2 - y1

if dx > dy:
    length = dx
else:
    length = dy

dx = dx / length
dy = dy / length

x = x1 + 0.5
y = y1 + 0.5


while i <= length:
    arrx.append(round(x,2))
    arry.append(round(y,2))
    arrResult.append((round(x, 2), round(y, 2)))
    arrPlot.append((int(x),int(y)))

    # Update x, y, and i
    x = x + dx
    y = y + dy
    i = i + 1
print("Length :",length)
print("X :",arrx)
print("Y :",arry)
print("Result :",arrResult)
print("Plot :",arrPlot)