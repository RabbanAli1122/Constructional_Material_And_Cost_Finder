print("\n\n-------------------------------------------------"
        "-----------------------------------------------------------\n"
        "Select the thing you want to calculate:\n"
        "1:finding the number of bricks,cement,cost and sand of a wall\n"
        "2:finding the cost,cement and sand of palastering a wall\n"
        "Enter the number beside your selection:\n-------------------------------------------------"
        "-----------------------------------------------------------\n")
o=int(input())
print("-------------------------------------------------"
        "-----------------------------------------------------------")
if o == 1:
    brick_length=float(input("\n\n--------------------------------------------------"
                         "------------------------------\nEnter the standard length of the bricks in"
                         " your area.\nNote:\nEnter your measurement in inches:\n------------------"
                         "---------------------------------------------------------------\n"))
    brick_width=float(input("\n\n--------------------------------------------------------------------"
                        "------------\nEnter the standard width of the bricks in your area.\nNote"
                        ":\nEnter your measurement in inches:\n------------------------------------"
                        "---------------------------------------------\n"))
    unit=int(input("\n\n------------------------------------------------------------------------------"
               "--\nIn which unit are you going to enter the measurements of your wall:"
            "\n1:feets\n2:meter\n3:inches\n4:centimeters\n5:milimeters. \nEnter the number beside the "
               "unit that you "
            "want to enter:\n------------------------------------------------------------------------"
               "---------\n"))
    if unit==1:
        length = float(input("\n\n-----------------------------------------------------------------------"
                         "---------\nEnter the length of your wall.\nNote:\nEnter your measurement in "
                         "feets:\n----------------------------------------------------------------------"
                         "-----------\n"))
        hight = float(input("\n\n----------------------------------------------------------------------------"
                        "----\nEnter the hight of your wall.\nNote:\nEnter your measurement in feets:\n-----"
                        "----------------------------------------------------------------------------\n"))
    elif unit==2:
        length = float(input("\n\n---------------------------------------------------------------------------"
                         "-----\nEnter the length of your wall.\nNote:\nEnter your measurement in meters:\n-"
                         "--------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n-----------------------------------------------------------------------------"
                        "---\nEnter the hight of your wall.\nNote:\nEnter your measurement in meters:\n------"
                        "---------------------------------------------------------------------------\n"))
    elif unit==3:
        length = float(input("\n\n-----------------------------------------------------------------------------"
                         "---\nEnter the length of your wall.\nNote:\nEnter your measurement in inches:\n---"
                         "------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n----------------------------------------------------------------------------"
                        "----\nEnter the hight of your wall.\nNote:\nEnter your measurement in inches:\n--"
                        "-------------------------------------------------------------------------------\n"))
    elif unit==4:
        length = float(input("\n\n----------------------------------------------------------------------------"
                         "----\nEnter the length of your wall.\nNote:\nEnter your measurement in centimeters"
                         ":\n---------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n-----------------------------------------------------------------------------"
                        "---\nEnter the hight of your wall.\nNote:\nEnter your measurement in feets:\n----"
                        "-----------------------------------------------------------------------------\n"))
    elif unit==5:
        length = float(input("\n\n-----------------------------------------------------------------------------"
                         "---\nEnter the length of your wall.\nNote:\nEnter your measurement in milimeters:\n"
                         "---------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n--------------------------------------------------------------------------------"
                        "\nEnter the hight of your wall.\nNote:\nEnter your measurement in milimeters:\n----"
                        "-----------------------------------------------------------------------------\n"))
    true_or_false=input("\n\n--------------------------------------------------------------------------------\nDoes"
                    " wall includes the base? Enter 'no' or 'yes':\n--------------------------------------------"
                    "-------------------------------------\n")
    if true_or_false == "yes" and unit ==1:
        hight_of_base_wall=float(input("\n\n---------------------------------------------------------------------"
                                    "-----------\nEnter the hight of your base wall.\nNote:\nEnter your measurement"
                                   " in feets:\n-----------------------------------------------------------------"
                                   "----------------\n"))
        p = length * 12 / brick_length+hight_of_base_wall
        o = hight * 12 / brick_width
        i = p * o
        y = round(i, 2)
        m = 3.5 / 1000
        o = m * y
        sand = 30 / 1000
        sandi = sand * y
        io=round(o,2)
        isandi=round(sandi,2)
        print("\n\n--------------------------------------------------------------------------------\nNumber of"
          " bricks required for this wall is equal to:", y, "\nQuantity of cement for this wall:",io, "bags\n"
        "Quantity of sand:",isandi,"cubic ft.\n---------------------------------------------------------------"
                                 "------------------\n")
    elif unit== 1 and true_or_false == "no" :
        p=length*12/brick_length
        o=hight*12/brick_width
        i=p*o
        y=round(i,2)
        m = 3.5 / 1000
        o=m*y
        sand=30/1000
        sandi=sand*y
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:",y,"\nQuantity of cement for this wall:",o,"bags\n"
      "Quantity of sand:",sandi,"cubic ft.\n------------------------------------------------------------------"
                                "---------------\n")
    elif true_or_false ==  "yes" and unit ==2:
        hight_of_base_wall=float(input("\n\n----------------------------------------------------------------------"
                                   "----------\nEnter the hight of your base wall.\nNote:\nEnter your measurement"
                                   " in feets:\n-----------------------------------------------------------------"
                                   "----------------\n"))
        p = length * 39.3 / brick_length+hight_of_base_wall
        o = hight * 39.3 / brick_width
        i = p * o
        y = round(i, 2)
        m = 3.5 / 1000
        o = m * y
        sand = 30 / 1000
        sandi = sand * y
        io=round(o,2)
        isandi=round(sandi,2)
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:", y, "\nQuantity of cement for this wall:",io, "bags\n"
        "Quantity of sand:",isandi,"cubic ft.\n--------------------------------------------------------------------"
                                 "-------------\n")
    elif unit== 2 and true_or_false =="no" :
        p=length*39.3/brick_length
        o=hight*39.3/brick_width
        i=p*o
        y=round(i,2)
        m = 3.5 / 1000
        o=m*y
        sand=30/1000
        sandi=sand*y
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:",y,"\nQuantity of cement for this wall:",o,"bags\n"
        "Quantity of sand:",sandi,"cubic ft.\n-------------------------------------------------------------------"
                                "--------------\n")
    elif true_or_false == "yes" and unit ==3:
        hight_of_base_wall=float(input("\n\n-----------------------------------------------------------------------"
                                   "---------\nEnter the hight of your base wall.\nNote:\nEnter your measurement"
                                   " in feets:\n-----------------------------------------------------------------"
                                   "----------------\n"))
        p = length / brick_length+hight_of_base_wall
        o = hight / brick_width
        i = p * o
        y = round(i, 2)
        m = 3.5 / 1000
        o = m * y
        sand = 30 / 1000
        sandi = sand * y
        io=round(o,2)
        isandi=round(sandi,2)
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:", y, "\nQuantity of cement for this wall:",io, "bags\n"
        "Quantity of sand:",isandi,"cubic ft.\n------------------------------------------------------------------"
                                 "---------------\n")
    elif unit== 3 and true_or_false =="no":
        p=length/brick_length
        o=hight/brick_width
        i=p*o
        y=round(i,2)
        m = 3.5 / 1000
        o=m*y
        sand=30/1000
        sandi=sand*y
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:",y,"\nQuantity of cement for this wall:",o,"bags\n"
        "Quantity of sand:",sandi,"cubic ft.\n--------------------------------------------------------------------"
                                "-------------\n")
    elif true_or_false ==  "yes" and unit ==4:
        hight_of_base_wall=float(input("\n\n------------------------------------------------------------------------"
                                   "--------\nEnter the hight of your base wall.\nNote:\nEnter your measurement in"
                                   " feets:\n--------------------------------------------------------------------"
                                   "-------------\n"))
        p = length * 39.3 / brick_length+hight_of_base_wall
        o = hight * 39.3 / brick_width
        i = p * o
        y = round(i, 2)
        m = 3.5 / 1000
        o = m * y
        sand = 30 / 1000
        sandi = sand * y
        io=round(o,2)
        isandi=round(sandi,2)
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:", y, "\nQuantity of cement for this wall:",io, "bags\n"
        "Quantity of sand:",isandi,"cubic ft.\n------------------------------------------------------------------"
                                 "---------------\n")
    elif true_or_false == "no"  and unit== 4:
        p=length*39.3/brick_length
        o=hight*39.3/brick_width
        i=p*o
        y=round(i,2)
        m = 3.5 / 1000
        o=m*y
        sand=30/1000
        sandi=sand*y
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:",y,"\nQuantity of cement for this wall:",o,"bags\n"
        "Quantity of sand:",sandi,"cubic ft.\n-------------------------------------------------------------------"
                                "--------------\n")
    elif true_or_false ==  "yes" and unit ==5:
        hight_of_base_wall=float(input("\n\n------------------------------------------------------------------------"
                                   "--"
                                   "------\nEnter the hight of your base wall.\nNote:\nEnter your measurement in "
                                   "feets:\n-------------------------------------------------------------------"
                                   "--------------\n"))
        p = length /2.54/ brick_length+hight_of_base_wall
        o = hight /2.54 / brick_width
        i = p * o
        y = round(i, 2)
        m = 3.5 / 1000
        o = m * y
        sand = 30 / 1000
        sandi = sand * y
        io=round(o,2)
        isandi=round(sandi,2)
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:", y, "\nQuantity of cement for this wall:",io, "bags\n"
        "Quantity of sand:",isandi,"cubic ft.\n---------------------------------------------------------------"
                                 "------------------\n")
    elif true_or_false == "no"   and unit== 5:
        p=length/2.54/brick_length
        o=hight/2.54/brick_width
        i=p*o
        y=round(i,2)
        m = 3.5 / 1000
        o=m*y
        sand=30/1000
        sandi=sand*y
        print("\n\n--------------------------------------------------------------------------------\nNumber of bricks"
          " required for this wall is equal to:",y,"\nQuantity of cement for this wall:",o,"bags\n"
            "Quantity of sand:",sandi,"cubic ft.\n--------------------------------------------------------------------"
                "-------------\n")
elif o == 2:
    unit = int(input("\n\n------------------------------------------------------------------------------"
                     "--\nIn which unit are you going to enter the measurements of your wall:"
                     "\n1:feets\n2:meter\n3:inches\n4:centimeters\n5:milimeters. \nEnter the number beside the "
                     "unit that you "
                     "want to enter:\n------------------------------------------------------------------------"
                     "---------\n"))
    if unit==1:
        length = float(input("\n\n-----------------------------------------------------------------------"
                         "---------\nEnter the length of your wall.\nNote:\nEnter your measurement in "
                         "feets:\n----------------------------------------------------------------------"
                         "-----------\n"))
        hight = float(input("\n\n----------------------------------------------------------------------------"
                        "----\nEnter the hight of your wall.\nNote:\nEnter your measurement in feets:\n-----"
                        "----------------------------------------------------------------------------\n"))
        thickness = float(input(
            "\n\n------------------------------------------------------------------------------------------------------------\n"
            "Enter the thickness of your plaster\n(suggested 12mm for inner plaster and 18mm for outter plaster)."
            "\nNote:\n"
            "Enter this measurement in feets:"
            "\n------------------------------------------------------------------------------------------------------------\n"))
    elif unit==2:
        length = float(input("\n\n---------------------------------------------------------------------------"
                         "-----\nEnter the length of your wall.\nNote:\nEnter your measurement in meters:\n-"
                         "--------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n-----------------------------------------------------------------------------"
                        "---\nEnter the hight of your wall.\nNote:\nEnter your measurement in meters:\n------"
                        "---------------------------------------------------------------------------\n"))
        thickness = float(input(
            "\n\n------------------------------------------------------------------------------------------------------------\n"
            "Enter the thickness of your plaster\n(suggested 12mm for inner plaster and 18mm for outter plaster)."
            "\nNote:\n"
            "Enter this measurement in feets:"
            "\n------------------------------------------------------------------------------------------------------------\n"))
    elif unit==3:
        length = float(input("\n\n-----------------------------------------------------------------------------"
                         "---\nEnter the length of your wall.\nNote:\nEnter your measurement in inches:\n---"
                         "------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n----------------------------------------------------------------------------"
                        "----\nEnter the hight of your wall.\nNote:\nEnter your measurement in inches:\n--"
                        "-------------------------------------------------------------------------------\n"))
        thickness = float(input(
            "\n\n------------------------------------------------------------------------------------------------------------\n"
            "Enter the thickness of your plaster\n(suggested 12mm for inner plaster and 18mm for outter plaster)."
            "\nNote:\n"
            "Enter this measurement in feets:"
            "\n------------------------------------------------------------------------------------------------------------\n"))
    elif unit==4:
        length = float(input("\n\n----------------------------------------------------------------------------"
                         "----\nEnter the length of your wall.\nNote:\nEnter your measurement in centimeters"
                         ":\n---------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n-----------------------------------------------------------------------------"
                        "---\nEnter the hight of your wall.\nNote:\nEnter your measurement in feets:\n----"
                        "-----------------------------------------------------------------------------\n"))
        thickness = float(input(
            "\n\n------------------------------------------------------------------------------------------------------------\n"
            "Enter the thickness of your plaster\n(suggested 12mm for inner plaster and 18mm for outter plaster)."
            "\nNote:\n"
            "Enter this measurement in feets:"
            "\n------------------------------------------------------------------------------------------------------------\n"))
    elif unit==5:
        length = float(input("\n\n-----------------------------------------------------------------------------"
                         "---\nEnter the length of your wall.\nNote:\nEnter your measurement in milimeters:\n"
                         "---------------------------------------------------------------------------------\n"))
        hight = float(input("\n\n--------------------------------------------------------------------------------"
                        "\nEnter the hight of your wall.\nNote:\nEnter your measurement in milimeters:\n----"
                        "-----------------------------------------------------------------------------\n"))
        thickness = float(input(
            "\n\n------------------------------------------------------------------------------------------------------------\n"
            "Enter the thickness of your plaster\n(suggested 12mm for inner plaster and 18mm for outter plaster)."
            "\nNote:\n"
            "Enter this measurement in feets:"
            "\n------------------------------------------------------------------------------------------------------------\n"))
    i = thickness / 1000
    volume_of_palster = length/ 3.28 * hight / 3.28 * i
    volume = volume_of_palster * 1.27
    quntity_of_cement = 1 / 5 * volume
    two_quntity_of_cement = quntity_of_cement / 0.035 - 0.1
    sand = 4 / 5 * volume
    two_sand = sand * 35.3 - 0.3
    ij = round(two_quntity_of_cement, 2)
    ji = round(two_sand)
    print("cement:", ij)
    print("sand:", ji)
