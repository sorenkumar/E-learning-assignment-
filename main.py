import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

GGAds='https://1drv.ms/b/s!AsZ_NqQCVV7-g7IXbD6_Lk6DzzuH0Q?e=V484fE'
ubersuggest='https://neilpatel.com/ubersuggest/'
canva='https://www.canva.com/'
fbEventpage='https://www.youtube.com/watch?v=XGYgzjoRPrA'
invPPLKFB='https://www.youtube.com/watch?v=8rL1wUZXQBI'
FBadsmanage='https://www.youtube.com/watch?v=Hr5CNXanieg'
FBPgRole='https://www.youtube.com/watch?v=dD-mH6FZPVA'
AdsPostFB='https://www.youtube.com/watch?v=TXtheWTnQx8'



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            command = command.lower()
            if 'Alen' in command:
                command = command.replace('Alen', '')
                print(command)
    except:
        pass
    return command

def run_hello():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('I am playing the song'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('the current time is' + time)

    elif 'who is' in command:
        person =command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'Page name' in command:
        talk('Step 1 Click “Edit Page Info” While viewing your page as an admin, click Edit Page Info on the left side of the page, under the Manage Page section')
        print('Step 1 Click “Edit Page Info” While viewing your page as an admin, click Edit Page Info on the left side of the page, under the Manage Page section')

        talk('Step 2 Type it. once you clicked into the name box, type in your page new name ')
        print('Step 2 Type it. once you clicked into the name box, type in your page new name')

        talk('step 3 Submit it')
        print('step 3 Submit it')

        talk('Wait for approval, which usually a few days')
        print('Wait for approval, which usually a few days')

    elif 'create facebook page' in command:
        talk('To create facebook page ')
        print('To create a facebook page')

        talk('Step 1 Go to facebook.com/page/create')
        print('Step 1 Go to facebook.com/page/create')

        talk('Step 2 Fill out the required information')
        print('Step 2 Fill out the required information')

        talk('Step 3 Click Create Page')
        print('Step 3 Click Create Page')

        talk('Step 4 Add an optional profile or cover photo, then click Save')
        print('Step 4 Add an optional profile or cover photo, then click Save')

    elif 'google ads account' in command:

        talk("You may download the tutorial and follow the steps")
        print("You may download the tutorial and follow the steps")

        webbrowser.open(GGAds, new=1)

    elif 'keyword research tools' in command:

        talk('you may try google keyword planner and ubersuggest')
        print('you may try google keyword planner and ubersuggest')

        webbrowser.open(ubersuggest, new=1)

    elif 'graphic desing tool'in command:

        talk('you may try Canva.com')
        print('You may try Canva.com')
        webbrowser.open(canva, new=1)

    elif 'poster desing tool' in command:
        talk('you may try Canva.com')
        print('You may try Canva.com')
        webbrowser.open(canva, new=1)



    elif 'event on facebook page' in command:
        talk('you may watch the tutorial video and follow the steps by using the youtube link')
        print('you may watch the tutorial video and follow the steps by using the youtube link')
        print('https://www.youtube.com/watch?v=XGYgzjoRPrA')
        webbrowser.open(fbEventpage, new=1)

    elif 'like facebook page invitation' in command:
        talk('you may watch the tutorial video and follow the step by using the youtube link')
        print('you may watch the tutorial video and follow the step by using the youtube link')
        print('https://www.youtube.com/watch?v=8rL1wUZXQBI')
        webbrowser.open(invPPLKFB, new=1)

    elif 'invite people like facebook page' in command:
        talk('you may watch the tutorial video and follow the step by using the youtube link')
        print('you may watch the tutorial video and follow the step by using the youtube link')
        print('https://www.youtube.com/watch?v=8rL1wUZXQBI')
        webbrowser.open(invPPLKFB, new=1)

    elif 'facebook ads manager account' in command:
        talk('you may watch the tutorial video and follow the step by using the youtube link')
        print('you may watch the tutorial video and follow the step by using the youtube link')
        print('https://www.youtube.com/watch?v=Hr5CNXanieg')
        webbrowser.open(FBadsmanage, new=1)

    elif 'add page role' in command:
        talk('you may watch the tutorial video and follow the step by using the youtube link')
        print('you may watch the tutorial video and follow the step by using the youtube link')
        print('https://www.youtube.com/watch?v=dD-mH6FZPVA')
        webbrowser.open(FBPgRole, new=1)
    elif 'facebook page role' in command:
        talk('you may watch the tutorial video and follow the step by using the youtube link')
        print('you may watch the tutorial video and follow the step by using the youtube link')
        print('https://www.youtube.com/watch?v=dD-mH6FZPVA')
        webbrowser.open(FBPgRole, new=1)
    elif 'ads posting in facebook' in command:
        talk('You may watch the tutorial video and follow the steps by using the YouTube link')
        print('You may watch the tutorial video and follow the steps by using the YouTube link')
        print('https://www.youtube.com/watch?v=TXtheWTnQx8')
        webbrowser.open(AdsPostFB, new=1)

    elif 'add admin in facebook' in command:
        talk('You may watch the tutorial video and follow the steps by using the YouTube link ')
        print('You may watch the tutorial video and follow the steps by using the YouTube link ')
        print('https://www.youtube.com/watch?v=-iLGr5olDlQ')

    else :
        talk('your command is not in the list will help you search in google')
        pywhatkit.search(command)
run_hello()