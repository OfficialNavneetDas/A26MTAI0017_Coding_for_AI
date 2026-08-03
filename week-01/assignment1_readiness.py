"""
Program : Temporal Profile Analyzer
Purpose : Computes an AI Era Readiness Score from user metadata.
Author  : Navneet Das 
Date : 29-07-2026
"""

from datetime import datetime

def byte_counter(name):
    symbols=["@","#","$","!","?","%","^","*","+","-","*","/"]
    new_name= name.strip().title()
    byte_count=len(new_name)
    if byte_count<=0:
        raise ValueError("name can not be empty / whitespaces")
    if any(i in new_name for i in symbols):
        raise ValueError(f"name can not have symbols {symbols}")
    return(byte_count)

def age_finder_and_validater(age):
    if(not age.isdigit()):
        raise ValueError("Error NOT a Number")
    age = int(age)
    if(age<=0 or age >=99):
        raise ValueError("Invalid age!")
    age = age+(2045-datetime.now().year)
    return(age)

#=====================================main code=====================================================
try:
    print("\t\t\tTemporal Profile Analyzer")
    print("-"*70)

    name=input("Enter your full name:")
    byteCount = byte_counter(name)
    age=input("Enter your current age:")
    projected_age = age_finder_and_validater(age)

    Score = ((byteCount*10)+projected_age)/2

    print(f"\n\n\n|-{"-"*50}-|")
    print(f"\tName : {name.strip().title()} | Byte-count: {byteCount}")
    print(f"\tAge  : {projected_age}")
    print(f"\tThe AI Readiness Formula is {Score:.2f}")
    print(f"|-{"-"*50}-|")
except ValueError as ve:
    print(ve)
finally:
    input("\n\n\n\n\nPress Enter to Exit....")
