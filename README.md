# JEN

## What is JEN?
Jen is a package which has a list of different types of assistants which can help you in virtual assistant projects.

## Sample Code

Code For making Simple Assistant

```python
from jen.assistant import SimpleAssistant
from jen.functions import display_cli_calendar

assistant=SimpleAssistant("Assistant")

command=input("What do you want the Assistant to Do :")

if "calendar" in command:
    year=int(input("Enter Year:"))
    assistant.display_response("Displaying the calendar for {}".format(year))
    display_cli_calendar(year)
```# JEN