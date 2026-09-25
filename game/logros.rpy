screen logros:
    tag menu
    use game_menu(_("Logros")):
        default desc = ""

        if desc != "":
            timer 0.02 repeat True action SetVariable("posicion_mouse", renpy.get_mouse_pos())
        

        frame:
            background None
            fixed:
                xpos 0.15
                ypos 0.1
                grid 5 4:
                    spacing 40
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                    imagebutton auto "gui/locked_logro_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                
            
        if desc != "":
            frame:
                background Solid('#0008')  
                xpadding 10
                ypadding 5
                xpos posicion_mouse[0] -150  # un poco a la derecha del cursor
                ypos posicion_mouse[1] -155
                text desc color "#ffffff" size 24 xalign 0.0 yalign 0.0