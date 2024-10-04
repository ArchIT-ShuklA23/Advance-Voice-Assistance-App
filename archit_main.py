import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime as dt
import wikipedia #pip install wikipedia
import webbrowser 
import os
import smtplib
import random as r2
import sys
import wolframalpha
import sqlite3 as sq
import random
import requests
from threading import *
import cv2  # Add this line for OpenCV


from tkinter import *
win=Tk()
win.title('Gideon AI')
win.geometry('630x700')
win.config(background="black")
win.attributes('-fullscreen', True)


conn = sq.connect('database.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS maildat(U_Name TEXT,email_id TEXT,password TEXT);''')
eid=cursor.execute('''SELECT email_id FROM maildat WHERE U_Name='Rana';''')
eid=str(cursor.fetchone())
eid=eid[2:(len(eid)-3):1]
enc=cursor.execute('''SELECT password FROM maildat WHERE U_Name='Rana';''')
enc=str(cursor.fetchone())
enc=enc[2:(len(enc)-3):1]

usertext=StringVar()
comtext=StringVar()

command_history = []

def new_GUI():


    # Create the main window
    root = Tk()

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size
    width = 650
    height = 700

    # Calculate the x and y coordinates to center the window
    #x = (screen_width // 2) - (width // 2)
    #y = (screen_height // 2) - (height // 2)
    # Set the y coordinate to a small value to position it near the top
    x = 150
    y = 15  # 50 pixels from the top

    # Set the window geometry
    root.geometry(f'{width}x{height}+{x}+{y}')  # Width x Height + Xoffset + Yoffset
    # Set the window size and position it on the leftmost side
    #root.geometry('650x700+0+0')  # Width x Height + Xoffset + Yoffset

    # Set the title
    root.title('Commands List')

    # Make the window transparent
    root.wm_attributes('-alpha', 0.7)  # Set transparency (0.0 is fully transparent, 1.0 is fully opaque)

    # Close the window when it is clicked
    root.bind('<Button-1>', lambda event: root.destroy())

    # Optionally, you can make the window without a border
    root.overrideredirect(True)  # Removes the window decorations

   
    # Run the main loop
   # root.mainloop()

    #root = Tk()
   # root.geometry('650x700')
    #root.title('Commands List')

    cmds="""                 

    1) Search Google keyword
        example: search google python or search google AI assistant
                
    2)Search Wikipedia keyword
        example: search Wikipedia python or search Wikipedia AI

    3)Google maps keyword
        example: google map delhi

    4)Open Code-> To open Microsoft Visual Code

    5)Open C Drive-> To Open C Drive   

    6)Open D drive-> To Open D Drive

    7)Play music-> To play Music

    8)Play video-> To play Video

    9)Search Youtube keyword
        example: search youtube python or search youtube AI assistant

    10)Open google-> To open google on browser

    11)Open Youtube-> To open youtube on browser

    12)Go Offline/Nothing/Bye-> To close Application

    13)Shutdown-> To shutdown the Operating System 

    14) Write Notepad -> To open Notepad and write a message.
    example: write notepad how are you? 

    15) play quiz game with me

    16) Wether in "City_name" -> For wether information

    17)API services-> WOLF-RAM-ALPHA, openweathermap
    """
 # Create a Text widget to display the commands #062b06
    # text_area = Text(root, bg='#228B22', fg='White', font=('Arial', 12), wrap='word')
    text_area = Text(root,  bg='#062b06',fg='#02fafa', font=('Arial', 12), wrap='word')
    text_area.insert('1.0', cmds)  # Insert the command text
    text_area.config(state='disabled')  # Make the text area read-only
    text_area.pack(expand=True, fill='both')
    '''
    hpframe=LabelFrame(
        root,
        text="Commands:- ",
        font=('Black ops one',12,'bold'),
        highlightthickness=3)
    hpframe.pack(fill='both',expand='yes')

    hpmsg=Message(
        hpframe,
        text=cmds,
        bg='black',
        fg='#7adb1e'
        )
    hpmsg.config(font=('Comic Sans MS',10,'bold'),justify="left")
    hpmsg.pack(fill='both',expand='no')


    exitbtn = Button(
        root, 
        text='EXIT', 
        font=('#7adb1e', 11, 'bold'), 
        bg='red', 
        fg='white',
        borderwidth=5,
        command=root.destroy).pack(fill='x', expand='no')
'''
    root.mainloop()


compframe=LabelFrame(
    win,
    text="Gideon ",
    font=('Lucida',10,'bold'),
    highlightthickness=2)
compframe.pack(fill='both',expand='yes')

left2=Message(
    compframe,
    textvariable=comtext,
    bg='#7adb1e',
    fg='black',
    justify='left'
    )

left2.config(font=('Lucida',12,'bold'),aspect=250)
left2.pack(fill='both',expand='yes')

userframe=LabelFrame(
    win,
    text="User",
    font=('Lucida',10,'bold'),
    highlightthickness=2,)
    
userframe.pack(fill='both',expand='yes')

left1=Message(
    userframe,
    textvariable=usertext,
    bg='black',
    fg='#7adb1e',
    justify='left'
    )
left1.config(font=('Lucida',12,'bold'),aspect=250)
left1.pack(fill='both',expand='yes')




engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('497K74-LQ93WJ8229')

voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
comtext.set("""Hello! 
I am your Personal Assistant Gideon 

Click on Start button to give your Commands"""
            )
usertext.set(' ')

def printo(shan):
    global comtext
    comtext.set(shan)
    
 
def speak(audio):
    
    printo(audio+"\n")
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! " +name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon! " +name)   

    else:
        speak("Good Evening! " +name)
        
    speak("""Hello {} 
How can I help you?""".format(name))
    #speak("Click start speaking button to give Commands")
    usertext.set('''  Click start speaking button to give Commands''')


def Name():
    #It takes microphone input from the user and returns string output
    global r,source,audio,query,name
    name=" "
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your name")
        printo("Please tell me Your name\n")
        printo("Listening...\n")
        #r.pause_threshold = 1 #bolne a time ruk gaye to 2 sec ruk kar execute karega taki pura phrase complete hojaye
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")    
        name = r.recognize_google(audio, language='en-in') #voice recognize hogi isme english-india mai
        #print(f"User said: {name}\n") #fstring use kiya hai
        

    except Exception as e:
        printo(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Name() 
        return None
    return name
    wishMe()

def Commands():
    global r, source, audio, query, usertext, command_history
    r = sr.Recognizer()
    r.energy_threshold = 2500
    with sr.Microphone() as source:
        printo("Listening...\n")
        r.pause_threshold = 1  # Adjust the pause threshold for recognizing speech
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')  # Recognize the user's voice input
        command_history.append("User said: " + query + "\n")  # Append the recognized command to the history
        usertext.set("".join(command_history))  # Display the entire command history
        print("User said: " + query)

    except Exception as e:
        printo("Say that again please...\n")
        speak("Say that again please...")
        Commands()  # Recurse to allow the user to try again if speech isn't recognized
        return query
    return query


def srch_google():
    #speak("Seaching on Google.....\n")
    #printo("Seaching on Google.....\n")
    #audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        keywords=(text.split(" "))
        printo(keywords)
        del keywords[0]
        del keywords[0]
        printo(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        printo("You said : {}\n".format(keyword))
        url='https://www.google.co.in/search?q='
        search_url=f'https://www.google.co.in/search?q='+keyword
        speak('searching on google' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")

def srch_google_map():
    #speak(" Searching on Google Map.....")
    #printo("Searching on Google Map.....\n")
    #audio=r.listen(source)
    try:
        text2=r.recognize_google(audio)
        #text="gooe map Taj mahal"
        keywords=(text2.split(" "))
        print(keywords)
        del keywords[0]
        del keywords[0]
        #del keywords[0]
        print(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        print("You said : {}\n".format(keyword))
        #url='https://www.google.com/maps/place/?'
        search_url=f'http://maps.google.com/?q='+keyword
        speak('searching on google map' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")


def search_yt():
    #speak("searching on youtube.....\n")
    #printo("searching on youtube.....\n")
    try:
        text=r.recognize_google(audio)
        key=(text.split(" "))
        #print(keywords)
        del key[0]
        del key[0]
        #print(keywords)
        
        def lis(s):
            str1=" "
            new=str1.join(s)
            return new
    
        key=lis(key)

        print("You said : {}".format(key))
        url='http://www.youtube.com/results?search_query='
        search_url=f'http://www.youtube.com/results?search_query='+key
        speak('searching on youtube ' +" "+ key)
        webbrowser.open(search_url)
    except:
        print("Can't recognize")

def sendEmail(to, content):
    global eid,enc
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(eid,enc)
    server.sendmail('your email', to, content)
    server.close()

    

def mainfn():
    global query
    if __name__ == "__main__":
        Name()
        wishMe()
    # while True: #while use kiya taki vo jabtak command nahi samjhe tabtak bar bar chale say that again vala
    # if 1:
# Define quiz questions and answers
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "Who wrote 'Hamlet'?", "answer": "shakespeare"},
    {"question": "What is the smallest planet in our solar system?", "answer": "mercury"},
    {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
    {"question": "Who developed the theory of relativity?", "answer": "einstein"},
]

def quiz_game():
    # Select a random question
    question = random.choice(quiz_questions)
    speak(f"OK {name}, let's play a quiz game! Here's your question:")
    speak(question["question"])
    
    # Listen to the user's answer
    user_answer = Commands().lower()  # Get user's answer
    
    # Check if the answer is correct
    if question["answer"] in user_answer:
        speak(f"Congratulations, {name}! That's the correct answer! 🎉")
    else:
        speak(f"Oops, {name}! The correct answer is {question['answer']}. Better luck next time!")
    
    # Ask if the user wants to continue 
    speak("Do you want to continue the quiz game? (say please continue or please stop the game)")
    response = Commands().lower()
    
    # Normalize the response checking
    if response in ['yes', 'y', 'yeah', 'sure', 'absolutely', 'please continue']:
        quiz_game()  # Recursively start a new round of the quiz
    else: 
        # response in ['no', 'n', 'nah', 'nope', 'please stop the game']:
        speak("Okay, let's stop the quiz game. Let me know if you want to play again!")
    # else:
    #     speak("I didn't understand that. Please respond with 'please continue' or 'please stop the game'.")
    #     quiz_game()  # Prompt again if the input is unclear
        
def get_weather(city):
    # city = "rajkot"
    api_key = "b1adeb43d88add8d493f1b5bc31eba19"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] != 200:
            speak("City not found.")
            return
        
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]

        weather_info = f"The weather in {city} is {weather_desc} with a temperature of {temperature} degrees Celsius."
        speak(weather_info)
        printo(weather_info)

    except Exception as e:
        printo(e)
        speak("Sorry, I couldn't retrieve the weather information.")        
        '''''' 
def capture_photo():
    cap = cv2.VideoCapture(0)  # Open the default camera
    ret, frame = cap.read()  # Read a frame from the camera
    if ret:
        cv2.imwrite("captured_photo.jpg", frame)  # Save the frame as a JPEG file
        speak("Photo captured successfully!")
    else:
        speak("Could not capture photo.")
    cap.release()  # Release the camera

def capture_video(duration=5):
    cap = cv2.VideoCapture(0)  # Open the default camera
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec
    out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (640,  480))  # Create a VideoWriter object
    speak(f"Recording video for {duration} seconds.")
    
    start_time = dt.datetime.now()
    while (dt.datetime.now() - start_time).seconds < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)  # Write the frame to the video file
            cv2.imshow('Recording', frame)  # Show the frame in a window
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop recording if 'q' is pressed
                break
        else:
            break

    cap.release()  # Release the camera
    out.release()  # Release the VideoWriter
    cv2.destroyAllWindows()  # Close all OpenCV windows
    speak("Video recorded successfully!")


def reco():
    while True:  # Continuously listens for voice commands
        query = Commands().lower()  # Get the user's voice command and convert to lowercase
        print(query)  # Print the recognized command in the console for debugging

        # Update the UI to show the recognized command in the "User" section
        usertext.set("".join(command_history))  # Display the command on the screen
        if 'play quiz game with me' in query:
            quiz_game()
        elif 'weather in' in query:
            city = query.replace("weather in", "").strip()  # Extract city name from command
            get_weather(city)
        # Logic for executing tasks based on query
        elif 'capture photo' in query:
            capture_photo()

        elif 'record video' in query:
            speak("How long should I record the video? Please say the duration in seconds.")
            duration = Commands()
            try:
                duration = int(duration)
                capture_video(duration)
            except ValueError:
                speak("Please provide a valid number for the duration.")
        elif 'search google' in query:
            srch_google()

        elif 'search youtube' in query:
            search_yt()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            printo(results + "\n")
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube ")
            url = 'http://www.youtube.com/results?search_query='
            webbrowser.open(url)

        elif 'google map' in query:
            srch_google_map()

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'go offline' in query or 'stop' in query or 'nothing' in query:
            speak('Okay ' + name)
            speak('Goodbye ' + name)
            quit()
            win.destroy()
            break  # Exit the listening loop

        elif 'shutdown' in query:
            speak('okay')
            os.system('shutdown -s')
            break  # Shutdown the system and exit the loop

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(r2.choice(stMsgs))

        elif 'play music' in query:
            # Path to the specific music file
            music_path = r"C:\Users\Archit\Downloads\Y2meta.app - etxrnall - your love is my drug (8bit slowed) (320 kbps).mp3"
            
            # Play the music file
            os.system(f'start "" "{music_path}"')
            
            # Notify the user
            speak('Okay, here is your music! Enjoy!')


        elif 'play video' in query:
            # Path to the specific video
            video_path = "C:\\Users\\Archit\\Videos\\Captures\\Major_project - Apache NetBeans IDE 16 2023-04-07 00-25-26.mp4"
            
            # Play the video
            os.system(f'start "" "{video_path}"')
            
            # Notify the user
            speak('Okay, here is your video! Enjoy!')


        elif 'open code' in query:
            # codePath = "C:\\Users\\Archit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"  # Path to the VS Code executable
            codePath = "C:\\Users\\Archit\\Desktop\\Visual Studio Code.lnk"
            try:
                os.startfile(codePath)
            except FileNotFoundError:
                print(f"File not found: {codePath}")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif 'open c drive' in query:
            cdrive = "C:"
            speak("opening C Drive....")
            os.startfile(cdrive)

        elif 'open d drive' in query:
            ddrive = "D:"
            speak("opening D Drive....")
            os.startfile(ddrive)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = Commands()
                to = "recipient_email@example.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                printo("Email has been sent!\n")
            except Exception as e:
                printo(e)
                speak("Sorry! I am unable to send your message at this moment!\n")

        elif 'hello' in query:
            speak('Hello ' + name)

        elif 'bye' in query:
            speak('Bye ' + name + ', have a good day.')
            win.destroy()
            break

        elif 'write notepad' in query:
            speak("What should I write in the notepad?")
            content = Commands()  # Get the content from the user
            with open("temp.txt", "w") as f:  # Create a temporary text file
                f.write(content)  # Write the content to the file
            os.startfile("temp.txt")  # Open the file in Notepad
            speak("I have written your message in Notepad.")


        else:
            try:
                speak('Searching in API...')
                res = client.query(query)
                results = next(res.results).text
                speak('API says - ')
                speak('please wait.')
                speak(results)

            except Exception as e:
                speak("I can't recognize your command. Should I open Google for you?")
                ans = Commands()
                if 'yes' in str(ans) or 'yeah' in str(ans):
                    webbrowser.open('www.google.com')
                elif 'no' in str(ans) or 'nah' in str(ans):
                    speak("Okay, disconnecting.")
                    sys.exit()
                else:
                    speak("No response. I am disconnecting.")
                    sys.exit()



def exit():
    win.destroy()
    sys.exit()
    #pass

def start():
    Thread(target=mainfn).start()

def speakingbtn():
    Thread(target=reco).start()
def stop_assistant():
    # Logic to stop the assistant
    sys.exit()
btn = Button(
    win, 
    text='Start!', 
    font=('#7adb1e', 11, 'bold'), 
    bg='black', 
    fg='#7adb1e',
    borderwidth=5,
    command=start).pack(fill='x', expand='no')
btn1 = Button(
    win, 
    text='Start Speaking!', 
    font=('#7adb1e', 11, 'bold'), 
    bg='black', fg='#7adb1e',
    borderwidth=5,
    command=speakingbtn).pack(fill='x', expand='no')
btn2 = Button(
    win, text='Command List', 
    font=('#7adb1e', 11, 'bold'), 
    bg='black', fg='#7adb1e',
    borderwidth=5,
    command=new_GUI).pack(fill='x', expand='no')
btn3 = Button(
    win, 
    text='EXIT', 
    font=('#7adb1e', 11, 'bold'), 
    bg='red', 
    fg='white',
    borderwidth=5,
    command=exit).pack(fill='x', expand='no')


win.mainloop()