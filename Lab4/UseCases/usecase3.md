**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3
# Pressing the space key will clear the entire canvas.
# This means all pixels will be removed, and the entire canvas will be a solid color with the last color you have selected.
# (In other words, this fills the entire canvas with the last selected color)

<hr>

**Use Case**: Canvas Clear and Recolor

**Primary Actor**: User

**Goal in Context**: To clear the entire canvas and replace it with the last selected color

**Preconditions**: The program must be running and in a responsive state. 

**Trigger**: The pressing of the space key
  
**Scenario**: A user will press the space bar and the canvas will be cleared, removing all pixels, and the entire canvas will be a solid color of the last color that was selected. 
 
**Exceptions**: The program may be unresponsive, in that case the program can be restarted through the OS. 

**Priority**: High-Priority

**When available**: First release

**Channel to actor**: The primary actor would communicate through their keyboard. The system is responsible for reacting to the selection of the spacebar within a second. Additionally, it is responsible for clearing the screen and replacing it with pixels of the last selected color

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: There should be a way to undo the action. The spacebar is a large button, and it may accidentally be pressed. Ensuring there is a way to undo the screen clear is essential. 

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
