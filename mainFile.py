import PySimpleGUI as sg
from window2 import *


##############################################

sg.theme('DarkTeal9')


layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Current Location', size=(15,1)), sg.Combo(['FCSE', 'FES', 'AcademicBlock','FME','FMCE','Library','BrabersBuilding','Tuc','H1','H2','H3','H4','H5','H6','GirlsHostel','H8','H9','H10','H11','H12','SportsComplex','Admin','Logik','MedicalCentre','Auditorium','Gate','GuestHouse','SportsGround','TransportOffice','FacultyClub','Mosque'], key='Current_Location')],
    [sg.Text('Desired Location', size=(15,1)), sg.Combo(['FCSE', 'FES', 'AcademicBlock','FME','FMCE','Library','BrabersBuilding','Tuc','H1','H2','H3','H4','H5','H6','GirlsHostel','H8','H9','H10','H11','H12','SportsComplex','Admin','Logik','MedicalCentre','Auditorium','Gate','GuestHouse','SportsGround','TransportOffice','FacultyClub','Mosque'], key='Desired_Location')],
    [sg.Text('Display: '),sg.Text(size=(15,1), justification='left',key='Display')],
    [sg.Submit(),sg.Exit()],
    ] #layout is defined in double list format and then passed to window argument which automatically recognizes the format

window = sg.Window("GIKI NAVIGATOR",layout,size = (350,150)) #(length,height)


while True:
    event, values = window.read() #read all events and input values on window canva

    if event == sg.WIN_CLOSED or event == 'Exit': #in case we cross the program or use exit button break
        break
    if event == 'Submit': #in case we use submit button we print event and values
        current_l = values['Current_Location'] #data is stored in dictionary format, we needed the values to pass onto the function in c++
        desired_l = values['Desired_Location']
        
        if (current_l == desired_l): #checking exception
            window['Display'].update('Invalid Input!') #update value of specified key in dictionary
        elif(current_l == ''):
            window['Display'].update('Invalid Input!') #update value of specified key in dictionary
        elif(desired_l == ''):
            window['Display'].update('Invalid Input!') #update value of specified key in dictionary
        elif(current_l == '' and desired_l == ''):
            window['Display'].update('Invalid Input!') #update value of specified key in dictionary
        else:

            window['Display'].update('Valid Input!')

            windownum2(current_l,desired_l)
        
        
window.close()

