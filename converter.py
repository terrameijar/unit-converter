print ("\t\tThis is a python converter")

"""step one, determine what conversion to perform
step two get user input on what conversions they want
step three convert and display to ouput"""

#How many pounds are in a kilogram?
#How many miles is 1km?
# what is xMbps in KB/s?

def prompt(weight,dist,band_w):
    """this function prompts the user which type of conversion they want to make"""
    pass

def weight():
    """Converts weights between pounds and kilogrammes"""
    #prompt()
    def kg_pounds(kg):
        pounds = kg / 0.45
        return pounds
    
    def pounds_kg(pounds):
        # 1 pound = 0.45kg
        kg = pounds * 0.45
        return kg
    
    
    try:
        weight_var = raw_input("1. Kg to Pounds \n2. Pounds to Kg\n3. Back to main menu\n")
        if (weight_var == "1"):
            print(str(kg_pounds(float(raw_input("Enter number of Kgs to convert__>")))) + "pounds")
            #Consider simplifying the above function
            weight()
            
        elif (weight_var == "2"):
            #pounds_kg()
            print(str(pounds_kg(float(raw_input("Enter number of Pounds to convert__>")))) + "Kgs")
            weight()
            
        elif (weight_var == "3"):
            main_loop()
            
        
        else:
            print("Please enter either 1,2 or 3")
            weight()
    
    except ValueError as err:
        print("Please enter valid digits")
        weight()


def km_to_mile():
    # 1 km = 0.621371mi1
    mile_const = 0.621371
    km = int(input("enter distance in km: "))
    km_to_mi = km * mile_const
    print (str(km) + "km in miles is: " + str(km_to_mi) + "miles")


def mile_to_km():
    #1mi = 1.60934km
    km_const = 1.60934
    mi = int(input("enter distance in miles: "))
    mi_to_km = mi * km_const
    print (str(mi) + " miles in kilometers is: " + str(mi_to_km) + "km")
                
    
def data_trans():


    def mbps_KBps(mbps=0,KBps=0):
        """Converts given bandwidth value to either Mbps or to KB/s"""
        # 1KB/s 0.0078125Mbps
        # 1Mbps = 128KB/s

        if mbps == 0 and not(KBps ==0):
            mbps = KBps * 0.0078125
            print( str(KBps) + " KB/s is equal to " + str(mbps) + " mbps")
        
        elif KBps == 0 and not (mbps == 0):
            KBps = 128 * mbps
            print( str(mbps) + " Mbps is equal to " + str(KBps) + " KB/s")

    #1Mbps = 128KB/s
    #Determine what exactly the user wants to convert:
    conv = raw_input(" 1. Mbps to KB/s \n 2. KB/s to Mbps \n 3. Back To Main Menu \n")

    try:
        if (conv == "1"):
            mbps = float(raw_input("Mbps to convert to KB/s: \n Value__>"))
            mbps_KBps(mbps)
            
            if not (mbps):
                print ("\n Please enter some data to convert \n")
                data_trans()
            #else:
            
        elif (conv =="2"):
            KBps = int(raw_input("\n KB/s to convert to Mbps: \n Value__>"))
            mbps_KBps(0,KBps)  
            
        elif (conv == "3"):
            main_loop()
         
    except ValueError as err:
        print("Please enter a valid response: Error code \n " + str(err))
        data_trans()    
        #if (KBps == 0):
        #    print ("Please enter some data to convert")
        #    data_trans()
        #else:
  
 
def main_loop():
    """Main program runner loop"""
    finished = False
    while (not finished):
        print ("\n\n\t\tHello and welcome to the conversion app")
        print "\n"
        c_type = raw_input("What would you like to convert?\n1: Distance \n2: Weight \n3: Bandwidth \nPress \"x\" to quit\n >__")
        
        if ("1") in c_type:
            print ("Distance")
            print("What would you like to convert? \n1: Kilometers to Miles \n2: Miles to Kilometers? \n3: Back to main menu\n")
            dist = raw_input(">__")
            if "1" in dist:
                km_to_mile()

            elif "2" in dist:
                mile_to_km()

            else:
                continue


        elif ("2") in c_type:
            print ("Weight")
            weight()
            
        elif ("3") in c_type:
            data_trans()

        elif ("x") in c_type:
            print("goodbye")
            finished = True
            break

        else:
            print ("Please enter 1,2,3 or x to quit")


main_loop()



