"""
Program : Weather bot 3000
purpose : Give sample lifestyle adviced based on tempture and rain.
Author : Navneet das
Date : 03-08-2026
"""

def validiate_number(variable):
    #checking for the symbol C and °
    if variable[-1]=="C" or variable[-1]=="c":
        variable = variable[:-1]
        if variable[-1]=="°":
            variable = variable[:-1]

    # removing the whitespaces
    variable = variable.strip()

    
    #checking for the digit input
    if(not variable.isdigit()):
        raise ValueError("The given number is not a number")
    return int(variable)


#-------------------------main program----------------------------
print("Welcome to your AI climate Assistant")

#step 1: taking temperature as input
temperature = input("Please enter Current Temprature in Celsius:")

#step 2: calling a function to validiate and convert the input
temperature = validiate_number(temperature)

#step 3: decision logic based on temeprature
if temperature>=30:
    print("It's hot! AI suggests turning on AC")
elif temperature<=15:
    print("Chilly! AI suggests a jacket")
else:
    print("temperature is potimal. Enjoy your Day!")

#step 4: combined logic (bouns feature)
rain_check=input("is it raining?")
if "yes" in rain_check.lower():
    print("AI suggests to carry a umbrella")
    
