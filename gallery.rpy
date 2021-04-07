default persistent.galleryNameSet = False
default persistent.player_name = ""
label galleryNameChange:
    if persistent.galleryNameSet:
        pass
    else:
        if persistent.player_name == "":
            $ persistent.player_name = renpy.input("What's your name?").strip() or "Aiden"
        $ persistent.galleryNameSet = True
    return

label galleryRename:
    $ persistent.player_name = renpy.input("What's your name?").strip() or "Aiden"
    return

screen gallery():
    modal True
    add "#000"
    text "{size=80}Gallery Mod" xcenter 0.5
    vpgrid:
        cols 3
        scrollbars "vertical"
        draggable True
        mousewheel True
        xalign 1.0
        ypos 150
        xspacing 50
        yspacing 50
        imagebutton:
            idle Transform("lroombj1",zoom=0.3)
            hover Transform("lroombj1", zoom=0.3)
            action Replay("galleryscene1",scope={"name":persistent.player_name}, locked=False)
        imagebutton:
            idle Transform("sm", zoom=0.3)
            hover Transform("sm", zoom=0.3)
            action Replay("galleryscene2",scope={"name":persistent.player_name}, locked=False)
        imagebutton:
            idle Transform("d1", zoom=0.3)
            hover Transform("d1", zoom=0.3)
            action Replay("galleryscene3",scope={"name":persistent.player_name}, locked=False)
        imagebutton:
            idle Transform("lmf", zoom=0.3)
            hover Transform("lmf", zoom=0.3)
            action Replay("galleryscene4",scope={"name":persistent.player_name},locked=False)
        imagebutton:
            idle Transform("00581_17", zoom=0.3)
            hover Transform("00581_17", zoom=0.3)
            action Replay("galleryscene5",scope={"name":persistent.player_name}, locked=False)
        imagebutton:
            idle Transform("00782_", zoom=0.3)
            hover Transform("00782_", zoom=0.3)
            action Replay("galleryscene6",scope={"name":persistent.player_name},locked=False)


    textbutton "Return" action Hide("gallery") , Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
