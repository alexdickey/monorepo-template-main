**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4
# When the mouse is pressed and a user left-clicks (i.e. on the pressed event, not released) a pixel color will change wherever the mouse is located. This should allow me to drag and draw over the canvas like a pencil on a piece of paper.

<hr>

**Use Case**: Drawing on the Canvas

**Primary Actor**: User

**Goal in Context**: To allow the user to change the color of the pixel on the screen where they are selecting with their mouse

**Preconditions**: The system must be responsinve and running and the user must have a working mouse. 

**Trigger**: The user left clicks with their mouse within the canvas window in the drawable area. 
  
**Scenario 1**: By pressing the left click, but not dragging, a single pixel will be drawn

**Scenario 2**: By pressing the left click, and dragging along the screen, a series of pixels will be drawn, tracing the path that the mouse has been moved while being held down. 
 
**Exceptions**: The program may be unresponsive.

**Priority**: High-priority

**When available**: First release

**Channel to actor**: The user would communicate to the system through their mouse. They would initiate the communication by left-clicking, indicating that they would like to begin their 'drawing' and this drawing should continue as they drag their mouse until the mouse is released

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We would have to handle the case in which the user continues to draw off of the screen and comes back, should the drawing persist or stop? what if they resize the screen, should the proportions of the drawings change?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
