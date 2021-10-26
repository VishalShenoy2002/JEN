import pyttsx3
import speech_recognition as sr


class SimpleAssistant:

    '''
    The SimpleAssistant class as the name suggests is a simple assistant 
    with only text response that is printed on the screen.
    '''

    def __init__(self,name_of_assistant):

        self.name_of_assistant=name_of_assistant
        print("Hi I am {} How may I help you".format(self.name_of_assistant))


    def take_input(self,prompt):
        '''
        The take_input function as the name suggests will take the input from the user.
        it thats one parameter that is prompt. It return the input while will be in 
        string datatype (str).

        Param: prompt
        --------------
            The prompt parameter as the name suggests is to display the prompt message 
            to the user.For Example: if you want to prompt "Enter Your Name:" then the prompt 
            parameter should be set to the value.
        '''

        return input('{}'.format(prompt))

    def display_response(self,response):

        '''
        The display_response function is used to show the response of the Assistant.
        It will display what ever display message you want. 

        Param: response
        ----------------
            This is the parameter which take what response you want to give.
            Example: you want to set reponse as "This is very good!" Then you need pass
            the response as "This is very good!".
        
        '''

        print("{} : {}".format(self.name_of_assistant,response))


class TalkbackAssistant:

    '''
    The TalkbackAssistant class as the name suggests has a talkback feature in it.
    It can do three things:
        1.Take the Input
        2. Display the Response
        3. Speak the Response
        4. Speak and Display the Response
    '''

    def __init__(self,name_of_assistant):

        self.name_of_assistant=name_of_assistant
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voices',self.voices[0].id)

    def take_input(self,prompt):
        '''
        The take_input function as the name suggests will take the input from the user.
        it thats one parameter that is prompt. It return the input while will be in 
        string datatype (str).

        Param: prompt
        --------------
            The prompt parameter as the name suggests is to display the prompt message 
            to the user.For Example: if you want to prompt "Enter Your Name:" then the prompt 
            parameter should be set to the value.
        '''

        return input('{}'.format(prompt))

    def display_response(self,response):

            '''
            The display_response function is used to show the response of the Assistant.
            It will display what ever display message you want. 

            Param: response
            ----------------
                This is the parameter which take what response you want to give.
                Example: you want to set reponse as "This is very good!" Then you need pass
                the response as "This is very good!".
            
            '''

            print("{} : {}".format(self.name_of_assistant,response))

    

    def speak_response(self,response):

        '''
        The speak_response function only speaks the response and doesn't display it.

        Param: response
        ----------------
            This is the parameter which take what response you want to give. 
            This will be spoken by the Assistant. Example: you want the assistant to speak
            "This is very good!" Then you need to set the response to "This is very good!".

        '''
        self.engine.say(response)
        self.engine.runAndWait()


    def speak_and_display_response(self,response):

        '''
        The speak_and_display_response function speaks the response display it.

        Param: response
        ----------------
            This is the parameter which take what response you want to give. 
            This will be spoken and displayed by the Assistant. Example: you want the assistant to speak
            "This is very good!" Then you need to set the response to "This is very good!".

        '''

        print("{} : {}".format(self.name_of_assistant,response))
        self.engine.say(response)
        self.engine.runAndWait()


class SpeechRecognisingAssistant:

    '''
    The SpeechRecognisingAssistant class as the name suggests has speech recognition in it. 
    It can recognise what the user wants and displays the response using text only.
    '''
    
    def __init__(self,name_of_assistant):
        self.name_of_assistant=name_of_assistant
        self.recognizer=sr.Recognizer()

    def take_input(self,prompt):
        '''
        The take_input function as the name suggests will take the input from the user.
        it thats one parameter that is prompt. It return the input while will be in 
        string datatype (str).

        Param: prompt
        --------------
            The prompt parameter as the name suggests is to display the prompt message 
            to the user.For Example: if you want to prompt "Enter Your Name:" then the prompt 
            parameter should be set to the value.
        '''

        return input('{}'.format(prompt))

    def listen_to_the_user(self):

        '''
        The listen_to_the_user() function has no parameters but it uses the 
        computers microphone to listen to the user. It returns what it has heard.
        '''

        with sr.Microphone() as source:

            print("Listening...")
            self.recognizer.pause_threshold=0.5
            audio=self.recognizer.listen(source)

        try:

            query=self.recognizer.recognize_google(audio,language='en-in')
            print('Did you say : {}'.format(query))

        except Exception :

            print('Say it Again')
            query='None'

        return query 

    def display_response(self,response):

            '''
            The display_response function is used to show the response of the Assistant.
            It will display what ever display message you want. 

            Param: response
            ----------------
                This is the parameter which take what response you want to give.
                Example: you want to set reponse as "This is very good!" Then you need pass
                the response as "This is very good!".
            
            '''

            print("{} : {}".format(self.name_of_assistant,response))


class TBSRAssistant:
    '''
    The TBSRAssistant (Talkback and Speech Recognising Assistant) class  as the name suggests has both the 
    talkback features and the speech recognition feature.It can do the following:
        1.Listen to your Voice
        2.Display the Response
        3.Speak the Response
        4.Display and Speak the Response 

    '''
    def __init__(self,name_of_assistant):

        self.name_of_assistant=name_of_assistant
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voices',self.voices[0].id)
        self.recognizer=sr.Recognizer()

    def take_input(self,prompt):
        '''
        The take_input function as the name suggests will take the input from the user.
        it thats one parameter that is prompt. It return the input while will be in 
        string datatype (str).

        Param: prompt
        --------------
            The prompt parameter as the name suggests is to display the prompt message 
            to the user.For Example: if you want to prompt "Enter Your Name:" then the prompt 
            parameter should be set to the value.
        '''

        return input('{}'.format(prompt))


    def display_response(self,response):

        '''
        The display_response function is used to show the response of the Assistant.
        It will display what ever display message you want. 

        Param: response
        ----------------
            This is the parameter which take what response you want to give.
            Example: you want to set reponse as "This is very good!" Then you need pass
            the response as "This is very good!".
        
        '''

        print("{} : {}".format(self.name_of_assistant,response))
   

    def speak_response(self,response):

        '''
        The speak_response function only speaks the response and doesn't display it.

        Param: response
        ----------------
            This is the parameter which take what response you want to give. 
            This will be spoken by the Assistant. Example: you want the assistant to speak
            "This is very good!" Then you need to set the response to "This is very good!".

        '''
        self.engine.say(response)
        self.engine.runAndWait()


    def speak_and_display_response(self,response):

        '''
        The speak_and_display_response function speaks the response display it.

        Param: response
        ----------------
            This is the parameter which take what response you want to give. 
            This will be spoken and displayed by the Assistant. Example: you want the assistant to speak
            "This is very good!" Then you need to set the response to "This is very good!".

        '''

        print("{} : {}".format(self.name_of_assistant,response))
        self.engine.say(response)
        self.engine.runAndWait()


    def listen_to_the_user(self):

            '''
            The listen_to_the_user() function has no parameters but it uses the 
            computers microphone to listen to the user. It returns what it has heard.
            '''

            with sr.Microphone() as source:

                print("Listening...")
                self.recognizer.pause_threshold=0.5
                audio=self.recognizer.listen(source)

            try:

                query=self.recognizer.recognize_google(audio,language='en-in')
                print('Did you say : {}'.format(query))

            except Exception :

                print('Say it Again')
                query='None'

            return query

        