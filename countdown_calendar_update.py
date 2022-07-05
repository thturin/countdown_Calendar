"""Countdown Calendar

Hacks and Tweaks
sort it!
    sort by the date list.sort(key=lambda x: x[1]
    lambda function is a small anonymous function
    lambda arguments: expression
    x = lambda a : a + 10
    print(x(5)) _> OUTPUT 15
restyle the text
    make it look pretty
set reminders

"""

from tkinter import Tk, Canvas
from datetime import date,datetime

"""make sure students use the proper format for %d/%m/%y' there can be no spaces and year must be 2 digits not 4"""
def get_events():
    list_events = []
    with open('events.txt') as file: #opens text file
        for line in file: #runs  loop for each line in the text file
            line = line.rstrip('\n') #you must remove \n or else line will look like this ['Halloween','31/10/22\n']
            current_event =line.split(',') #turn string line into an array with two string items
            event_date = datetime.strptime(current_event[1],'%d/%m/%y').date() #(string content, format)
       #     print(current_event[1])
            current_event[1]=event_date #second item in list is now an actual date (not a string anymore)
            print(current_event[1])
            list_events.append(current_event) #this is will add the formated date of event to our list
    return list_events #returns a 2d list [['Halloween,date],[christmas, date],...]

def days_between_dates(date1,date2): #function that counts the number of days between two dates
    time_between = str(date1-date2) #variable stores difference of dates as a string
    #if a Hallowen is 27 days away, the string in time_between -> '27 days, 0:00:00 h:m:s all we need is the 27
    number_of_days = time_between.split(' ')
    return number_of_days[0]



root = Tk() #Tkinter window
c = Canvas(root,width=800,height=800, bg='green')
c.pack() #Tkinter window
c.create_text(100,50, anchor='w', fill='pink', font='Courier 36 bold underline', text='Ms.T\'s Calendar')
""" 
This line adds text onto the c canvas. The text starts at x=100 , y=50. 
The starting coordinate is at the left (west) of the text 
now we want to loop through every special event in our txt list and calculate how many days away we are
"""
events = get_events()
today = date.today()

events.sort(key=lambda x: x[1]) #use the second item in the list (date) to sort function

vertical_space = 100 #moves the y coordinate so eevery date is on its own line
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1],today)

    if int(days_until) <= 7:
        text_color = 'red'
    else:
        text_color = 'black'

    display = 'It is %s days until %s' % (days_until, event_name)
    c.create_text(100,vertical_space,anchor='w',fill=text_color, font='Arial 28 bold', text=display)
    vertical_space +=30

root.mainloop()






