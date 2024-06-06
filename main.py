import PySimpleGUI as sg
from encryptpass import *

def passwordwind(password, store):
  layout = [ [sg.Text('Password for ' + store + ' is ' + password)],
    [sg.Button('Exit')] ]
  window = sg.Window("  Passwords Viewer", layout, modal=True)
  
  while True:
    event, values = window.read()
  
    if event == 'Exit':
      window.close()
      main()
      break
  


def openwind():
  layout = [ [sg.Text('Enter name of the store'),     sg.InputText(do_not_clear=False)],
    [sg.Button('Ok '),sg.Button('Exit')] ]
  window = sg.Window("  Passwords lookfor", layout, modal=True)
  choice = None
  while True:
    event, values = window.read()
    
    if event == 'Ok ':
      window.close()
      password11 = lookfor(values[0])
      passwordwind(password11, values[0])
      break

    if event == 'Exit':
      window.close()
      main()
      break
      
    

def randpasswind():  
  layout = [ [sg.Text('Enter name of the store'),     sg.InputText(do_not_clear=False)],
    [sg.Text('Enter length of password'), sg.InputText(do_not_clear=False)],
    [sg.Button('Ok'), sg.Button('See Passwords'), sg.Button('Cancel')] ]

  window = sg.Window("      Random password genortor", layout)

  while True:
    event, values = window.read()

    if event == 'Cancel' or event == sg.WIN_CLOSED:
      window.close()
      main()
      break
    if event == 'See Passwords':
      window.close()
      openwind()
      break
    if event == 'Ok': 
      print(values[0])
      randpass(values[0], values[1])


def main():
  
  layout = [ [sg.Text('Enter name of the store'),     sg.InputText(do_not_clear=False)],
  [sg.Text('Enter your password'), sg.InputText(do_not_clear=False)],
  [sg.Button('Ok'), sg.Button('Make random password'), sg.Button('See Passwords'), sg.Button('Cancel')] ]

  window = sg.Window('       Password Management', layout)
  while True:
    event, values = window.read()
  
    if event == 'Cancel':
      break

    
    if event == 'See Passwords':
      window.close()
      openwind()
      break
    if event == 'Make random password':
      window.close()
      randpasswind()
      break
    if event == 'Ok': 
      encriptpass(values[1], values[0])
      





main()       