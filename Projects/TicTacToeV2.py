print(". . .")
print(". . .")
print(". . .")

next_pos_upd = input("Type here you want to set your figure: ")
if(next_pos_upd == "1"):
    print("x . .")
    print(". . .")
    print(". . .")

    next_pos_upd = input("Type here you want to set your figure: ")

    if(next_pos_upd == "1"): 
        print("Can't. Already blocked")
    elif(next_pos_upd == "2"):
        print("x o .")
        print(". . .")
        print(". . .")
        next_pos_upd = input("Type here you want to set your figure: ")
        if(next_pos_upd == "1"):
            print("You can't move here: ")
        elif(next_pos_upd == "2"):
            print("You can't move here: ")
        elif(next_pos_upd == "3"):
            print("x o x")
            print(". . .")
            print(". . .")
            next_pos_upd = input("Type here you want to set your figure: ")
            if(next_pos_upd == "1"):
                print("You can't move here.")
            elif(next_pos_upd == "2"):
                print("You can't move here.")
            elif(next_pos_upd == "3"):
                print("You can't move here.")
            elif(next_pos_upd == "4"):
                print("x o x")
                print("o . .")
                print(". . .")
            elif(next_pos_upd == "5"):
                print("x o x")
                print(". o .")
                print(". . .")
            elif(next_pos_upd == "6"):
                print("x o x")
                print(". . o")
                print(". . .")
            elif(next_pos_upd == "7"):
                print("x o x")
                print(". . .")
                print("o . .")
            elif(next_pos_upd == "8"):
                print("x o x")
                print(". . .")
                print(". o .")
            elif(next_pos_upd == "9"):
                print("x o x")
                print(". . .")
                print(". . o")
        elif(next_pos_upd == "4"):
            print("x o .")
            print("x . .")
            print(". . .")
        elif(next_pos_upd == "5"):
            print("x o .")
            print(". x .")
            print(". . .")
        elif(next_pos_upd == "6"):
            print("x o .")
            print(". . x")
            print(". . .")
        elif(next_pos_upd == "7"):
            print("x o .")
            print(". . .")
            print("x . .")
        elif(next_pos_upd == "8"):
            print("x o .")
            print(". . .")
            print(". x .")
        elif(next_pos_upd == "9"):
            print("x o .")
            print(". . .")
            print(". . x")
        
    elif(next_pos_upd == "3"):
        print("x . o")
        print(". . .")
        print(". . .")
    elif(next_pos_upd == "4"):
        print("x . .")
        print("o . .")
        print(". . .")
    elif(next_pos_upd == "5"):
        print("x . .")
        print(". o .")
        print(". . .")
    elif(next_pos_upd == "6"):
        print("x . .")
        print(". . o")
        print(". . .")
    elif(next_pos_upd == "7"):
        print("x . .")
        print(". . .")
        print("o . .")
    elif(next_pos_upd == "8"):
        print("x . .")
        print(". . .")
        print(". o .")
    elif(next_pos_upd == "9"):
        print("x . .")
        print(". . .")
        print(". . o")
elif(next_pos_upd == "2"):
    print(". x .")
    print(". . .")
    print(". . .")
elif(next_pos_upd == "3"):
    print(". . x")
    print(". . .")
    print(". . .")
elif(next_pos_upd == "3"):
    print(". . .")
    print("x . .")
    print(". . .")
elif(next_pos_upd == "4"):
    print(". . .")
    print(". x .")
    print(". . .")
elif(next_pos_upd == "5"):
    print(". . .")
    print(". . x")
    print(". . .")
elif(next_pos_upd == "6"):
    print(". . .")
    print(". . .")
    print("x . .")
elif(next_pos_upd == "7"):
    print(". . .")
    print(". . .")
    print(". x .")
elif(next_pos_upd == "8"):
    print(". . .")
    print(". . .")
    print(". . x")