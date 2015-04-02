#dnSim

The goal of this project is to creat a data-driven skill simulator for Eyedentity's game "Dragon Nest"

Use and files in this repository at your own risk.

Software is provided as is.

##How to use:

Select server, then select class.

Left click to rank up

Right click to rank down

shift-click to maximize, and minimize ranks

specialization selector on the right will allow you to see all classes, or classes individually.
This is so that smaller monitors (hopefully) don't have an issue. 

Ctrl-r to reset skill selection (sets all to minimum possible ranks)

##Commiting Changes

For instructions on how to contribute to the project look in the docs folder.

specifically how_to_commit.txt and format_descriptons.xml

##Installation

With the addition of skill icon support it seems that more than the standard windows binary for 3.4 needs to be installed. 
Anyways below is a list of things that need to be installed.

1. Python 3.4 and tkinter which is bundled together in the windows installer on [python website](https://www.python.org/).
2. you will need to install pillow (adds image support)  
It was quite easy to install for me. In the command line I ran 
`pip install Pillow`

##TODO:

* after 1 data set is complete get other people involved to finish data aquisition

* [skill,lvl]program in a conflict detection system (not enough sp, too low a level, etc)

* [partial]improve description box (cooldown, reqlevel, name, sp requirements, etc)

* add importing feature

*  make class selector use class name attribute in file

* Make the level set button propogate changes in max sp spent (hovering onto skills does this currently)

* generally make it look nicer

##Done

* finish data files for a complete class

* add in the handling for multiple skill sheets (either wide or pages)

* add in sp counting

* add in an option for pages instead of wide mode

* add in sp caps for lvl 80

* program in levels other than 80

* make shift-clicking max/min the number of ranks

*  make the skillrank/max thing in the skill button separate things within the button object.

* impliment icons for skills