screen extras:
    tag menu
    use game_menu(_("Extras"), scroll="viewport"):
   
        vbox:
            grid 1 7:
                xpos 150
                spacing 20
                imagebutton auto "Extra_1_%s.png" focus_mask None action Start("extra1")
                imagebutton auto "Bloqueado_%s.png" action NullAction()
                imagebutton auto "Bloqueado_%s.png" action NullAction()
                imagebutton auto "Bloqueado_%s.png" action NullAction()
                imagebutton auto "Bloqueado_%s.png" action NullAction()
                imagebutton auto "Bloqueado_%s.png" action NullAction()
                imagebutton auto "Bloqueado_%s.png" action NullAction()
        
            textbutton _("Volver") action Return() xpos 0.03 ypos 0.9