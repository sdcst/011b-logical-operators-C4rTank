#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")

i = ('Guile') or ("Blanka") or ("Christine") or ("Carol") or ("Richard") or ("Daniel") or ("Chun-Li")

name = str(input("Please input a name: "))

if name == "Guile":
   print('Hi Guile! You are a VIP!')

elif name == "Blanka":
    print('Hi Blanka! You are a VIP!')

elif name == "Christine":
    print('Hi Christine! You are a VIP!')

elif name == "Carol":
    print('Hi Carol! You are a VIP!')

elif name == "Richard":
    print('Hi Richard! You are a VIP!')

elif name == "Daniel":
    print('Hi Daniel! You are a VIP!')

elif name == "Chun-Li":
    print('Hi Chun-Li! You are a VIP!')

else:
    print("You are not a VIP.")

#done
