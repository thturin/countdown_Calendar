"""Countdown Calendar"""

from tkinter import Tk, Canvas
from datetime import date,datetime

## in the Tkinter module, the canvas exists so that

def get_events():
    list_events = []
    with open('events.txt') as file: #opens text file
        for line in file: #runs  loop for each line in the text file
            line = line.rstrip('\n') #you must remove \n or else line will look like this ['Halloween','31/10/22\n']
            current_event =  line.split(',') #turn string line into an array with two string items
            event_date = datetime.strptime(current_event[1],'%d/%m/%y').date() #(string content, format)
            print(current_event[1])
            current_event[1]=event_date #second item in list is now an actual date (no longer just a string)
            print(current_event[1])

root = Tk() #Tkinter window
c = Canvas(root,width=800,height=800, bg='black')
c.pack() #Tkinter window
c.create_text(100,50, anchor='w', fill='orange', font='Arial 28 bold underline', text='My Countdown Calendar')
""" 
This line adds text onto the c canvas. The text starts at x=100 , y=50. 
The starting coordinate is at the left (west) of the text 
"""
get_events()
root.mainloop()






