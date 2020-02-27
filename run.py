from threading import Thread
import os

def roll():
    try:
        os.system('python roll.py')
    except:
        roll()
    
def convert():
    try:
        os.system('python convert.py')
    except:
        convert()

Thread(target = roll).start() 
Thread(target = convert).start()