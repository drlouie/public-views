*********************** d i s c l a i m e r**************************
*                                                                   *
*   This flash-file was made by © 2000 Patrick Jansen Vormgeving.   *
*   It may be freely used for personal, educational or comercial    *
*   purposes.                                                       *
*                                                                   *
*********************************************************************

This system is developed to 'preload' external swf-files within your
main movie. It contains a simple preloader which checks to see if the
main movie is completely loaded, then it will continue to the exter-
nal swf-files preloader. 

The main movie preloader has a simple check to see if the frame with
label "end" has loaded, if so it will go on from label "continue".
This action remains within keyframe-label-"load"

If Frame Is Loaded ("end")
      Go to and Play ("continue")
End Frame Loaded

If "end" is not loaded yet, is is told to loop by a keyframe with 
action

Go to and Play ("load")

After frame/label "continue", it will go to frame/label "loadtext"
where the external swf-files will be loaded into th main movie. In 
my case it loads 4 swf's into 4 instances of movieclip "empty", 
instance names empty1 till empty4:

Load Movie ("external1.swf", "/empty1")
Load Movie ("external2.swf", "/empty2")
Load Movie ("external3.swf", "/empty3")
Load Movie ("external4.swf", "/empty4")

The next frame/label "check" has the actual external-files preloader.
It will check if the sizes of all MovieClip instances (in this case
empty1 till empty4)  are greater then 0, starting from empty1. If 
they are all greater then 0, it means all external files are loaded 
and it has the action to continue at label "go". 

NOTICE!: To avoid empty1,empty2 and so on continue playing while the 
rest has not been completely loaded, i added the action to stop each
one/empty-instance the moment it has loaded it's external swf.
If you don't do that, empty1 might already finish and return blank
before the last one loaded completely --> loop will never finish.

If (GetProperty("empty1",_width) > 0)
      Begin Tell Target ("/empty1")
            Go to and Stop (1)
      End Tell Target
      If (GetProperty("empty2",_width) > 0)
            Begin Tell Target ("/empty2")
                  Go to and Stop (1)
            End Tell Target
            If (GetProperty("empty3",_width) > 0)
                  Begin Tell Target ("/empty3")
                        Go to and Stop (1)
                  End Tell Target
                  If (GetProperty("empty4",_width) > 0)
                        Begin Tell Target ("/empty4")
                              Go to and Stop (1)
                        End Tell Target
                        Go to and Play ("go")
                  End If
            End If
      End If
End If

As long as all movies have not been loaded, it will loop between 
frame above and next keyframe with action

Go to and Play ("check")

When completely finished, it starts playing at frame/label "go"

-----------------------------------------------------------------

All instances of empty (1 to 4) are placed off-stage right-bottom
initialy to 'hide' them. the moment they should appear i created
a new keyframe and put it's position at x-y 0-0 and has the action
to start from befginning, e.g.;

Begin Tell Target ("/empty1")
      Go to and Play (1)
End Tell Target

Now you can apply tons of great effects on your imported swfs like
movement, alpha-tweening etc. (i used a fade-out in example)

PS1!! In minor 'bug' in SWFX is that in this system, you can not
stop the first letter from SWFX effects to start animating since
it's initiated already and a timeline of it's own. A small fix is
to simply add a space before your text (space as first letter) in 
SWFX.

PS2!! Free webspace sometimes turns out to have the flash mime type
configured wrongly (personal experience ;-). To be sure the preloader
does not 'hang', add to your source code the correct mime:
<EMBED src="moviename.swf" type=application/x-shockwave-flash >

good luck

Patrick Jansen
Graphic- Web- & flashdesigner
http://orbita.starmedia.com/~pjv/

