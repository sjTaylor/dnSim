#dnSim

The goal of this project is to creat a data-driven skill simulator for Eyedentity's game "Dragon Nest"

Use and files in this repository at your own risk.

Software is provided as is.

##How to use:

Select server, then select class.

Left click to rank up

Right click to rank down

shift-click to maximize, and minimize ranks

specialization selector on the left will allow you to see all classes, or classes individually.
This is so that smaller monitors (hopefully) don't have an issue. 

Ctrl-r to reset skill selection (sets all to minimum possible ranks)

##Commiting Changes

I recommend you take a look at [this guide](https://guides.github.com/activities/forking/index.html) since making pull requests is probably going to be most common way to contribute to the project. There are also [some other guides](https://guides.github.com/) on the github website which you might find useful.

It is also possible to edit files in your browser on the github website. If you want to do this I recommend you make the changes on your computer so you can test to see if they work and do what you want them to, and then just copy and paste into the browser.

##Installation

With the addition of skill icon support it seems that more than the standard windows binary for 3.4 needs to be installed. 
Anyways below is a list of things that need to be installed.

1. Python 3.4 and tkinter which is bundled together in the windows installer on [python website](https://www.python.org/).
2. you will need to install pillow (adds image support)  
It was quite easy to install for me. In the command line I ran 
`pip install Pillow`  
If that doesn't work you can [look here](https://pip.pypa.io/en/latest/installing.html) for  information on installing pip.  
Note: on my windows 8 machine I had pip installed, but it didn't seem to be part of my path variable. So I used `/cygdrive/c/Python34/Scripts/pip.exe install Pillow` in cygwin or  
`C:\Python34\Scripts\pip.exe install Pillow`  
in the standard windows command prompt to install Pillow with pip

##TODO:

* after 1 data set is complete get other people involved to finish data aquisition

* [skill,lvl]program in a conflict detection system (not enough sp, too low a level, etc)

* [partial]improve description box (cooldown, reqlevel, name, sp requirements, etc)

* add importing feature

*  make class selector use class name attribute in file

* generally make it look nicer

##Done

* Make the level set button propogate changes in max sp spent (hovering onto skills does this currently)

* finish data files for a complete class

* add in the handling for multiple skill sheets (either wide or pages)

* add in sp counting

* add in an option for pages instead of wide mode

* add in sp caps for lvl 80

* program in levels other than 80

* make shift-clicking max/min the number of ranks

*  make the skillrank/max thing in the skill button separate things within the button object.

* impliment icons for skills