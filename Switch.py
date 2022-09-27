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
    match args:
        case 1:
            return "linear"
        case 2:
            return "power"
        case 3:
            return "spherical"
        case 4:
            return "exponential"
        case 5:
            return "gaussian"