import math
zone = '''
1. Local Within Chennai
2. Tamil Nadu
3. Kerala, Karnataka, Andhra Pradesh and Telangana (Except Hyderabad and Secunderabad)
4. Hyderabad and Secunderabad
5. Mumbai, New Delhi and Kolkata
6. North, East, West
7. Kashmir, Assam, Nagaland, Manipur, Tripura, Mizoram, Megalaya, Sikkim and Arunachal Pradesh
8. Andaman

Enter which zone: '''

mode = '''
1. Surface Mode
2. Express Mode
Enter which mode: '''
rate = 0
while(True):
    inp = int(input(zone))
    weight = float(input("Enter the Weight (in KG): "))
    if (inp == 1):
        if (weight <= 0.25):
            rate = 16.50
        elif (weight <= 0.5):
            rate = 19.80
        elif (weight < 3):
            rate = 19.80 + 11 * math.ceil(weight - 0.5)
        elif (weight > 3):
            rate = 13.20 * math.ceil(weight)
    elif (inp == 2):
        if (weight <= 0.25):
            rate = 33
        elif (weight <= 0.5):
            rate = 44
        elif (weight < 3):
            rate = 44 + 16.5 * math.ceil(weight - 0.5)
        elif (weight > 3):
            rate = 22 * math.ceil(weight)
    elif (inp == 3):
        if (weight <= 0.25):
            rate = 38.5
        elif (weight <= 0.5):
            rate = 49.5
        elif (weight < 3):
            rate = 49.5 + 22 * math.ceil(weight - 0.5)
        elif (weight > 3):
            rate = 27.5 * math.ceil(weight)
    elif (inp == 4):
        m = int(input(mode))
        if (m == 2):
            if (weight <= 0.25):
                rate = 44
            elif (weight <= 0.5):
                rate = 60.5
            elif (weight < 3):
                rate = 60.5 + 38.5 * math.ceil(weight - 0.5)
            elif (weight > 3):
                rate = 71.5 * math.ceil(weight)
        if (m == 1):
            rate = 33 * math.ceil(weight)
    elif (inp == 5):
        m = int(input(mode))
        if (m == 2):
            if (weight <= 0.25):
                rate = 49.5
            elif (weight <= 0.5):
                rate = 71.5
            elif (weight < 3):
                rate = 71.5 + 44 * math.ceil(weight - 0.5)
            elif (weight > 3):
                rate = 82.5 * math.ceil(weight)
        if (m == 1 and weight >= 1):
            rate = 38.5 * math.ceil(weight)
    elif (inp == 6):
        m = int(input(mode))
        if (m == 2):
            if (weight <= 0.25):
                rate = 55
            elif (weight <= 0.5):
                rate = 77
            elif (weight < 3):
                rate = 77 + 44 * math.ceil(weight - 0.5)
            elif (weight > 3):
                rate = 88 * math.ceil(weight)
        if (m == 1 and weight >= 1):
            rate = 38.5 * math.ceil(weight)
    elif (inp == 7):
        if (weight <= 0.5):
            rate = 82.5
        elif (weight < 3):
            rate = 82.5 + 49.5 * math.ceil(weight - 0.5)
        elif (weight > 3):
            rate = 93.5 * math.ceil(weight)
    elif (inp == 8):
        if (weight <= 0.25):
            rate = 60.50
        elif (weight <= 0.5):
            rate = 82.5
        elif (weight < 3):
            rate = 82.5 + 49.5 * math.ceil(weight - 0.5)
        elif (weight > 3):
            rate = 93.5 * math.ceil(weight)
    print()
    print("Rate: Rs.     ", rate)
    print("Fuel: Rs.     ", 0.25 * rate)
    print("With GST: Rs. ", (rate + 0.25 * rate)*0.18)
    print("----------------------")
    print("Total: Rs.", (rate + 0.25 * rate) + (rate + 0.25 * rate)*0.18)
    print("----------------------")
