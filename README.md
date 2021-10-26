# JenAssistant

## What is JenAssistant?
Jen is a package which has a list of different types of assistants which can help you in virtual assistant projects.

## Sample Code

This is the code for making a Simple Assistant. Here it checks if the word calendar is there in the command you have provided and accordingly displays the calendar for the given year

```python
from jen.assistant import SimpleAssistant
from jen.functions import display_cli_calendar

assistant=SimpleAssistant("Assistant")

command=input("What do you want the Assistant to Do :")

if "calendar" in command:
    year=int(input("Enter Year:"))
    assistant.display_response("Displaying the calendar for {}".format(year))
    display_cli_calendar(year)
```

This is the code for making a Speech Recognising Assistant. This can recognise your speech and display the output accordingly.

```python
from jen.assistant import SpeechRecognisingAssistant
from jen.functions import display_cli_calendar

assistant=SpeechRecognisingAssistant('Bot')
command=assistant.listen_to_the_user()

if "calendar" in command:
    year=assistant.take_input("Enter Year :")
    display_cli_calendar(int(year))
```

## Error Handling

Here if we get a PyAudio Error then import the configure module

```python
from jen import configure

configure.configure_pyaudio()
```
