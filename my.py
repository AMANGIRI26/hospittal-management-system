import pandas as pd
import numpy as np
from csv import writer


print("********************************************************************")
print("*                                                                  *")
print("*                        Hospital Management System                *")
print("*                                                                  *")
print("*                                           Designed by Aman Giri  *")
print("*                                           Reg. No    11908192    *")
print("********************************************************************")


hospital_data = pd.read_csv("hospital_patient.csv")



print("-----------------------------------------")
print("|Enter 1 for Doctor 			|\n|Enter 2 for Patient mode		|	|")
print("-----------------------------------------")
Admin_user_mode = input("Enter your mode : ") 

if Admin_user_mode == "1":
    Doc_name = input("Enter the official Nanme ")
    pa = input("Enter the Password ")

    print("welcome Sir")
    doctor_choice = input("Press 1 for Patients List \n")
    if(doctor_choice=="1"):
        a = hospital_data.head(20)
        print(a)

elif Admin_user_mode == "2":
    print("Patient Mode")
    print("-----------------------------------------")
    print("|To book an appointment Enter 1         |")
    print("|To cancel an appointment Enter 2      |")
    print("-----------------------------------------")
    patient_choice= input("Enter your mode : ")
    if patient_choice == "1":
        name = input("Enter the name   : ")
        age  = input("Enter the Age   : ")
        Gender    =input("Enter patient gender  : ")
        Address   =input("Enter patient address : ")
        final_details = [name, age, Gender, Address]
        print("Your Details are " , final_details)
        hospital_data = hospital_data.append({'name':name ,'age' :age,'gender':Gender ,"address": Address }, ignore_index = True)
        hospital_data.to_csv("hospital_patient.csv")

    elif patient_choice == "2":
        print(hospital_data.head(10))
        token = int(input(" Please Enter the correct Token Number "))
        hospital_data.drop(token)



