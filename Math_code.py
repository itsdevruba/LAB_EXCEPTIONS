def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError as error:
    print("the name is not defined:", error)
else:
    print("the operation is successful")