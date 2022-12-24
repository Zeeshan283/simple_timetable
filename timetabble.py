# TIme Table for CUI Sahiwal Campus Mechnical deaprtment

import pandas as pd

print(" Time Table for CUI Sahiwal Mechinical Department")
print("")
# Batch Selection
print("Select your Batch")
print("1. FA19-BSME-B15-B")
print("2. FA19-BSME-B15-A")
print("3. FA20-BSME-B16-A")
print("4. FA21-BSME-B17-A")
print("5. FA22-BSME-B18-A")
print("")
# Day of which you want to view Time Table 
Batch = int((input("Select Your Batch From the Following : "))) 
print("")
print("Monday")
print("Tuesday")
print("Wednesday")
print("Thursday")
print("Friday")
print("")
# match used for day selection

day = input("Enter Day to see Time Table : ").lower()
print("")
match day:
    case "monday":
        if(Batch == 1):
            print("Time Table")
            timetable = [["CAD CAM(1hr)", "Mr. Khawar Hussain" , "A2.1"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 2):
            print("Time Table")
            timetable = [["CAD CAM (1hr)", "ME Mr. Khawar Hussain" , "B3"],
                         ["Mechanical Vibrations", "ME Mr. Khawar Hussain" , "A3"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 3):
            print("Time Table")
            timetable = [["Numerical Computations", "ME Dr. Tauqeer Anwar" , "A1.2"],
                         ["Engineering Fluid Mechanics", "ME Mr. Muhammad Nawaz" , "Fluid Mechanics Lab"],
                         ["Electric Machines", "ME Ms. Saba Gull" , "Electric Machines Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 4):
            print("Time Table")
            timetable = [["Pakistan Studies", "ME Mr. Naveed Ahmad" , "W4"],
                         ["Differential Equations", "MT Dr Hameed Ullah" , "W2"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 5):
            print("Time Table")
            timetable = [["Calculus I", "MT Dr Asma" , "C2"],
                         ["ICT", "ME Ms. Saba Gull" , "CAD CAM Lab"],
                         ["ECC", "CVE Saima Batool" , "A3"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)

    case "tuesday":
        if(Batch == 1):
            print("Time Table")
            timetable = [["MMV", "MS. Sara Batool" , "Vibration Lab"],
                         ["MMV", "MS. Sara Batool" , "Vibration Lab"],
                         ["MMV", "MS. Sara Batool" , "Vibration Lab"],
                         ["ACR" , "MR. HAfeex Ahmad" , "A1.2" ]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 2):
            print("Time Table")
            timetable = [["Mechanical Vibrations", "ME Mr. Khawar Hussain" , "A2.1"],
                         ["ACR", "ME Mr. Hafeez Ahmad" , "A3"],
                         ["CAD CAM", "ME Mr. Ali Zahid" , "CAD CAM Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 3):
            print("Time Table")
            timetable = [["Electric Machines", "ME Mr. Muzammil" , "A1.3"],
                         ["Numerical Computations", "ME Mr. Aamir Shehzad" , "CAD CAM Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 4):
            print("Time Table")
            timetable = [["Engineering Mechanics", "ME Ms. Sara Batool" , "Mechanics Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 5):
            print("Time Table")
            timetable = [["ECC", "CVE Saima Batool" , "A1.2"],
                         ["APME", "ME Dr. Muhammad Abid" , "A2.8"],
                         ["EDG(1hr)", "ME Mr. Hassan Iqbal" , "A1.2"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        

    case "wednesday":
        if(Batch == 1):
            print("Time Table")
            timetable = [["CAD CAM (1hr)", "ME Mr. Khawar Hussain" , "A1.2"],
                         ["Mechanical Vibrations", "ME Mr. Khawar Hussain" , "A1.3"],
                         ["Renewable Energy Technology", "ME Dr. Muneeb Qasim" , "A1.1"],
                         ["ACR" , "ME Mr. Hafeez Ahmad" , "A1.3"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 2):
            print("Time Table")
            timetable = [["MMV", "ME Ms. Sara Batool" , "Vibrations Lab"],
                         ["Advanced Material Processing", "ME Dr. Rafi Raza" , "HMT Lab"],
                         ["CAD CAM (1hr)", "ME Mr. Khawar Hussain" , "A2.1"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 3):
            print("Time Table")
            timetable = [["EFM II", "ME Mr. Hassan Iqbal" , "A1.2"],
                         ["EME", "ME Dr. Salman Mustafa" , "W3"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 4):
            print("Time Table")
            timetable = [["Pakistan Studies", "ME Mr. Naveed Ahmad" , "A2.1"],
                         ["Mechanics of Materials I", "ME Mr. Salman Nawaz" , "Fluid Mechanics Lab"],
                         ["Thermodynamics II", "ME Mr. Hassan Iqbal" , "A3"],
                         ["Engineering Dynamics", "ME Mr. Muzammil", "A2.1"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 5):
            print("Time Table")
            timetable = [["APME", "ME Dr. Muhammad Abid" , "A2.8"],
                        ["APME", "ME Mr. Jawad Abid " , "PhyLab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
    
    case "thrusday":
        if(Batch == 1):
            print("Time Table")
            timetable = [["CAD CAM", "ME Mr. Ali Zahid" , "CAD CAM Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 2):
            print("Time Table")
            timetable = [["ACR", "ME Mr. Hafeez Ahmad" , "A3"],
                         ["Heat Transfer and HVAC", "ME Mr. Muhammad Naveed" , "HMT Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 3):
            print("Time Table")
            timetable = [["Mechanics of Machines I", "ME Mr. Salman Nawaz" , "Vibrations Lab"],
                         ["EFM", "ME Mr. Hassan Iqbal" , "A1.2"],
                         ["Numerical Computations", "ME Dr. Tauqeer Anwar" , "W1"],
                         ["EME" , "ME Dr. Salman Mustafa" , "W3"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 4):
            print("Time Table")
            timetable = [["Differential Equations", "MT Dr Hameed Ullah" , "C3"],
                         ["Thermodynamics II", "ME Mr. Hassan Iqbal" , "Vibrations Lab"],
                         ["Engineering Dynamics", "ME Mr. Muzammil" , "A1.2"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 5):
            print("Time Table")
            timetable = [["ICT", "ME Dr. Muhammad Abid" , "A1.2"],
                         ["Calculus I", "MT Dr Asma" , "A1.1"],
                         ["ICT", "ME Dr. Muhammad Abid" , "A1.2"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)

    case "friday":
        if(Batch == 1):
            print("Time Table")
            timetable = [["Renewable Energy Technology", "ME Dr. Muneeb Qasim" , "W2"],
                         ["Heat Transfer and HVAC", "ME Mr. Yasir Raza" , "HMT LAB"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 2):
            print("Time Table")
            timetable = [["Advanced Material Processing", "ME Dr. Rafi Raza" , "W3"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 3):
            print("Time Table")
            timetable = [["Electric Machines", "ME Mr. Muzammil" , "W4"],
                         ["Mechanics of Machines I", "ME Mr. Salman Nawaz" , "Vibrations Lab"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print()
        elif(Batch == 4):
            print("Time Table")
            timetable = [["Thermodynamics", "ME Mr. Zafar Farooq" , "Thermo Lab"],
                         ["Mechanics of Materials I", "ME Mr. Salman Nawaz" , "Fluid Mechanics Lab"],
                         ["Subject3", "Teacher" , "cr"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
        elif(Batch == 5):
            print("Time Table")
            timetable = [["EDG", "ME Mr. Ghulam Mustafa" , "DRAWING HALL"]]
            df = pd.DataFrame(timetable, columns = ['Subject', 'Teacher' , 'Room' ])
            print(df)
    case _:
        print("Invalid input please input again")