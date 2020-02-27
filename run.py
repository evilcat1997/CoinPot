from threading import Thread
import os

def roll(): 
    os.system('python roll.py')
    
def convert():
    os.system('python convert.py')

Thread(target = roll).start() 
Thread(target = convert).start()