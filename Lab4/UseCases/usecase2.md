**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2
# Pressing the number keys 1 through 8 allows you to draw in a different color.
# 1 = Black
# 2 = White
# 3 = Red
# 4 = Green
# 5 = Blue
# 6 = Yellow
# 7 = Magenta
# 8 = Cyan

<hr>

**Use Case**: Color Selection

**Primary Actor**: User

**Goal in Context**: To change the color in which the user is able to draw in 

**Preconditions**: The program must be running and in a responsive state, additionally the user must have the ability to select numbers on their keyboard

**Trigger**: Selecting a number key (1-8) on the keyboard
  
**Scenario**: A user will select a number key (1-8) that will coorespond to a different color (Black, White, Red, Green, Blue, Yellow, Magenta, Cyan). In response to this, the color in which the user will be able to draw in will change
 
**Exceptions**: If the user does not have a working keyboard, perhaps there should be an alternate option/color selector feature. 

**Priority**: Medium-Priority

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard. The system is responsible for maintaining focus of the window when the user selects their keyboard, and should be responsible for changing the drawing color within 1 second of any keyboard event. The user is responsible for all other input. 

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: An additional method to changing color may need to be implemented in the future, such as a drop down selector that can be navigated without the need of a functioning keyboard

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
