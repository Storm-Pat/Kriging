def switch():
    print("What type of kriging do you want to use?")
    print("1:Linear")
    print("2:Power")
    print("3:Spherical")
    print("4:Exponential")
    print("5:Gaussian")
    while True:
        args = input()
        if args == "1" or args == "2" or args == "3" or args == "4" or args == "5":
            args = int(args)
            break
        else:
            print("Enter a valid integer")
    if args == 1:
        print("Selected Linear Kriging")
        return "linear"
    if args == 2:
        print("Selected Power Kriging")
        return "power"
    if args == 3:
        print("Selected Spherical Kriging")
        return "spherical"
    if args == 4:
        print("Selected Exponential Kriging")
        return "exponential"
    if args == 5:
        print("Selected Exponential Kriging")
        return "gaussian"
