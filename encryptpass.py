import threading
import socket
import rsa
import random
from cryptography.fernet import Fernet


key = Fernet.generate_key()
fernet = Fernet(key)

def start():

  choice = str(
      input(
          "What do you want to do? E: Enter another password. V: View your current passwords. G: Generate a password. "))

  if choice == "E" or choice == "e":
    store = str(input("Enter name of website or store: "))
    password = str(input("Enter your password for: " + store + ", "))
    encriptpass(password, store)
  if choice == "G" or choice == "g":
    store = str(input("Enter name of website or store: "))
    randpass(store)
  if choice == "v" or choice == "V":
    store = str(input("Enter Name of store or website you looking for: "))
    lookfor(store)
  else:
    pass
    #DONE


def encriptpass(password, store):


  crypto = fernet.encrypt(password.encode())

  with open("passwords", "ab") as text_file:
    text_file.write((crypto))

  text_file = open("passwords", "a")
  text_file.write(str(store + "\n"))
  text_file.close()

  store = store.lower()
  text_file = open("store", "a")
  text_file.write(str(store + "\n"))
  text_file.close()
  #DONE


def de(crtpto):

  message = fernet.decrypt(crtpto).decode()
  return message


def randpass(store, lenofpass):
  uppercaseL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercaseL = uppercaseL.lower()
  nums = "012345689"
  syms = "!@#$%&*+-_"
  randlist = []
  password = ' '
  choices = [uppercaseL, lowercaseL, nums, syms]
  for i in range(0, int(lenofpass)):
    randchoices = random.choice(choices)
    randchoice = random.choice(randchoices)
    randlist.append(randchoice)
  for x in randlist:
    password += x
  encriptpass(password, store)
  #DONE


def lookfor(store):
  file_data = []
  text_file = open('store', "r")
  pass_file = open('passwords', "rb")
  lcv = 0
  palcv = 0
  for word in text_file.read().split():
    lcv += 1

    if word == store:
      for paword in pass_file.read().split():
        palcv += 1
        if palcv == lcv:
          lcv -= 1
          return de(paword)
  text_file.close()
  text_file.close()

