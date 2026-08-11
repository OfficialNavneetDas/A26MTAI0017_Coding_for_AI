# Validators
def temperature_validator(temp):
    is_negtive = False
    if temp.startswith("-"):
        is_negtive = True
        temp = temp[1:]

        
    if not temp.isdigit():
        if temp[-1] == "C" or temp[-1] == "c":
            temp = temp[:-1].strip()
            if temp[-1] == "°":
                temp = temp[:-1].strip()
    temp =  float(temp)


    # checking for negative and absolute zero
    if is_negtive == True:
        temp = -temp
    if temp>=-273.15:
        return(temp)
    else:
        print("Temperature cant be less then absolute zero(-273.15°C)")
        raise ValueError("Invalid input")

def humudity_validator(humidity):
    if not humidity.isdigit():
        if humidity[-1] == "%":
            humidity = humidity[:-1]
            humidity = float(humidity)    
    else:
        humidity = float(humidity)

    # checking for set bounds
    if 0 <= humidity <= 100:
        return(humidity)
    else:
        print("humidity out of range")
        raise ValueError("Invalid input")

    
# Heuristic logic
def Heuristic_logic(temperature,humidity):
    HSI = temperature + (0.5 * humidity)
    if(HSI > 45):
        return("CRITICAL")
    if(wind_str := input("wind (km/h):").strip()):
        wind_float = float(wind_str)
    if(30 <= HSI <= 45 and wind_float<5):
        return("CAUTIONARY")
    else:
        print("ye chal raha h kya")
        return("OPERATIONAL")
    

# output render
def render_output(Tier):
    print("\n\n\nOUTPUT:")
    print(f"+{"="*40}+")
    print(f"+\tSafety level:{Tier}")
    print(f"+{"="*40}+")

#======================: Main Engine :=====================
# tempreture
try:
    if(temperature_str := input("Temprature (C):").strip()):
        temperature_float = temperature_validator(temperature_str)
        if temperature_float<0:
            render_output("FREEZE ALERT")
        elif(humidity_str := input("humidity (%):").strip()):
            humidity_float = humudity_validator(humidity_str)
            tiers = Heuristic_logic(temperature_float,humidity_float)
            render_output(tiers)
    else:
        raise ValueError("Invalid input")
except:
    render_output("Unknown!!")
finally:
    getch=input("press enter to exit....")
