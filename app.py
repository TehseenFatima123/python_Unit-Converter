
import streamlit as st

def Convert_units(value: float, unit_from:str, unit_to:str):
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters"and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "centimeters"and unit_to == "meters":
        return value * 0.01 
    elif unit_from == "meters" and unit_to == "centimeters":
        return value * 100
    else:
        return "conversion is not possible"

#result1 = Convert_units(1.5, "kilometers", "meters")
#print ("The value in meter is :", result1)
#result2 = Convert_units(1.0, "meters", "centimeters")
#print ("The value in meter is :", result2)

def main():
    st.title("Unit Converter")
    st.write("*Welcome To Unit Converter*")
    value =  st.number_input("Enter the value:", min_value=0.0)
    unit_from = st.text_input("Enter the unit you want to convert from (e.g. meters, kilometers, centimeters:")
    unit_to = st.text_input ("Enter the value you want to convert in (e.g. meters, centimeters, kilometers):")
   # print ("value", value)
    #print ("unit_from", unit_from)
   # print ("unit_to", unit_to)
    if st.button("Convert"):
        result = Convert_units(value, unit_from, unit_to)
        st.write("Converted value is:", result)
main()

