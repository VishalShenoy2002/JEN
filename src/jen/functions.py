import pyautogui
import calendar
import datetime
import random
import subprocess
import time
import os
import webbrowser
import wikipedia




def day_today():
    ''' 
    The day_today() function as the name suggests tells you what day is it today. 
    It sees the system day and tells you.

    Example:
        Todays date is 1st January 2021. It will return Today is Friday.
    '''

    monday=calendar.MONDAY
    tuesday=calendar.TUESDAY
    wednesday=calendar.WEDNESDAY
    thursday=calendar.THURSDAY
    friday=calendar.FRIDAY
    saturday=calendar.SATURDAY
    sunday=calendar.SUNDAY
    today=datetime.date.today()

    if today.weekday()==monday:
        return "Today is Monday"

    elif today.weekday()==tuesday:
        return "Today is Tuesday"

    elif today.weekday()==wednesday:
        return "Today is Wednesday"

    elif today.weekday()==thursday:
        return "Today is Thursday"

    elif today.weekday()==friday:
        return "Today is Friday"

    elif today.weekday()==saturday:
        return "Today is Saturday"

    elif today.weekday()==sunday:
        return "Today is Sunday"
        
    else:
        return "Sorry!!"


def date_today():
    '''
    The date_today() function as the name suggests tells you what date is it today.
    It sees the system's day and tells you the date.

    Example:
        Today is Friday, and it is the first day of the year it will return 1 January 2021.

    '''

    return "Today's Date is {}".format(datetime.date.today())


def time_right_now():
    '''
    The time_right_now() function as the name suggests tells you what time is it right now.
    It sees the system timezone and then tells you the time.

    Example:

        Case 1:
            Lets Assume the time right now is 10:30 AM it will return "Right Now the time is 10:30".

        Case 2:
            Lets assume the time right now is 4:45 PM it will return "Right Now the time is 16:45".
    
    '''

    now=datetime.datetime.now().strftime("%H:%M")
    return "Right Now the time is {}".format(now)


def greet():
    '''
    The greet() function as the name suggests greets the user according to the time of the day.
    It sees the system time and then greets accordingly. It Considers 24 hour format.

    Example:

        Case 1:
            If the time is 6:00 AM then the function will return "Good Morning!"

        Case 2:
            If the time is 12:30 PM then the function will return "Good Afternoon!"    

        Case 3:
            If the time is 18:30 PM then the function will return "Good Evening!"    


    '''

    hour=datetime.datetime.now().time().hour
    
    if hour>=0 and hour<12:
        return "Good Morning!"

    elif hour>=12 and hour<15:
        return "Good Afternoon!"

    else:
        return "Good Evening!"


def display_cli_calendar(year):

    '''
    The display_cli_calendar() function as the name suggests displays the calendar.
    It prints it in the commond line interface.

    Param: year
    -----------
        This parameter take the year as the name suggests and displays the calendar
        accordingly.Example:you want to display 2015's calendar then the year parameter
        will be 2015.

    '''
    
    print(calendar.calendar(year))


def play_music(music_dir=None,shuffle=False):

    '''
    The play_muisc() function as the name suggests plays music from your computer.
    The music is played from the Music Directory provided.

    Param: music_dir
    -----------------
        The music_dir parameter takes a valid path of the music directory. Its default value is
        set to None. The function will play the first song in the provided directory.

    Param: shuffle
    --------------
        The shuffle parameter takes True or False as its value. If the value is set to False then it 
        plays the first song in the directory. If the value is set to True it picks a random song from 
        the given directory.

    '''

    music_list=os.listdir(music_dir)

    if  shuffle==True:
        selection=random.choice(music_list)
        os.startfile(os.path.join(music_dir,selection))
    
    else:

        for i in ['{}.{}'.format(index+1,song) for index,song in enumerate(music_list)]:
            print(i)
        option=int(input('\nEnter Song Number :'))
        os.startfile(os.path.join(music_dir,music_list[option-1]))


def open_google_maps(location=None):

    '''
    The open_google_maps() Function as the name suggests opens Google Maps on your default 
    web browser. It has one parameter that is location..

    Param: location
    ----------------
        The location parameter takes the location and opens the specified location on the Browser.
        The location by default is set to None. It the value is set to None the map opens with your 
        current location. If value is set to anything other than None it opens the specified location.

    '''

    if location is not None:
        webbrowser.open("https://www.google.co.in/maps/place/{}".format(location))
        

    else:
        webbrowser.open("https://www.google.co.in/maps/")


def write_into_files(auto_write=False,content=''):
    '''
    The write_into_files() function as the name suggests is used to write into files.
    It has two parameters they are auto_write and content. 

    Note:-
    ------
        Don't switch tabs until its done writing as it'll continue 
        writing and othe document you are writing won't be completed.


    Param: auto_write
    ------------------
        The auto_write parameter by default is set to False. If it is False it Opens Notepad.
        If the value is set to True it opens Notepad and starts to write the content on its own 
        in 3 seconds and prompts you to save it.

    Param: content
    ---------------
        The content parameter is related to the auto_write parameter. If the value of auto_write 
        is True then the value of content should be set. Else it is Not needed. 

    '''

    if auto_write==True:
        subprocess.Popen(["notepad.exe"])
        time.sleep(3)
        print('Starting in 3 seconds...')
        pyautogui.typewrite(content,interval=0.125)
        pyautogui.hotkey('ctrl','s')

    else:
        subprocess.Popen(['notepad.exe'])


def search_wikipedia(topic=None,lines=3):
    '''
    The search_wikipedia() function as the name suggests does a wikipedia search on wikipedia.
    It takes 2 parameters that is topic and lines. It will return the search results.


    Param: topic
    -------------
        This parameter take the topic for the search. Its default value is set to None.
        It won't search anything unless you provide a topic.

    Param: lines
    ------------
        This parameter takes the number of lines you want from the search result. The default number of 
        lines is set to 3.

    '''

    return wikipedia.summary(topic,sentences=lines)


def open_google():

    '''
    The open_google() function as the name suggests opens google in your default web browser.
    It has no parameters.
    '''

    webbrowser.open('https://www.google.com/')






