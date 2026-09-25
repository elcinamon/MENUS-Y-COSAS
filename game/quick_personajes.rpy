
default posicion_mouse = (0, 0)
screen iconos_personajes:
    tag menu
    default desc = ""
    add "17539.jpg"

    if desc != "":
        timer 0.02 repeat True action SetVariable("posicion_mouse", renpy.get_mouse_pos())
    

    frame:
        background None
        fixed:
            xpos 0.05
            ypos 0.1
            grid 4 4:
                spacing 15
                imagebutton auto "icono_pereza_%s.png" hovered SetScreenVariable("desc", "Pereza") unhovered SetScreenVariable("desc", "") action ShowMenu("pereza")
                if gula_conocido == True:
                    imagebutton auto "icono_gula_%s.png" hovered SetScreenVariable("desc", "Gula") unhovered SetScreenVariable("desc", "") action ShowMenu("gula")
                else:
                    imagebutton auto "locked_character_devil_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_devil_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_devil_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_devil_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_angel_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_angel_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_angel_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_fallangel_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_fallangel_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
                imagebutton auto "locked_character_fallangel_%s.png" hovered SetScreenVariable("desc", "Bloqueado") unhovered SetScreenVariable("desc", "") action NullAction()
            
        
    if desc != "":
        frame:
            background Solid('#0008')  
            xpadding 10
            ypadding 5
            xpos posicion_mouse[0] + 60  # un poco a la derecha del cursor
            ypos posicion_mouse[1] + 35
            text desc color "#ffffff" size 24 xalign 0.0 yalign 0.0
    textbutton _("Volver") action Return() xpos 0.03 ypos 0.9

        

screen pereza:
    tag menu
    use iconos_personajes
    vbox:
        xpos 0.55
        ypos 0.1
        grid 4 4:
            spacing 15
            imagebutton idle "locked_logro.png" hover "locked_logro.png" focus_mask None action None
            imagebutton idle "locked_logro.png" hover "locked_logro.png"  focus_mask None action None
            imagebutton idle "locked_logro.png" hover "locked_logro.png"  focus_mask None action None
            imagebutton idle "locked_logro.png" hover "locked_logro.png"  focus_mask None action None

screen gula:
    tag menu
    use iconos_personajes
    frame:
        background Solid("#7b517d")
        xpos 0.55
        ypos 0.1
        add "Gula_Feliz.png" zoom 0.55
    vbox:
        xalign 0.98
        yalign 0.1
        text "{size=80}{color=40183fff}{b}Gula{/b}{/size}" xalign 0.4
        text "{b}Anillo:{/b} Gula \n\n{b}Estado:{/b} vivo \n\n{b}Descripción:{/b}\nUn demonio glotón \nque si no se \nle presta atención \nen mucho tiempo \ncausa problemas.\n\n{b}Notas:{/b}Nada inusual \npor el momento" xalign 0.6

    text "{size=80}{b}Afinidad{/b}{/size}" xalign 0.83 yalign 0.7
    bar:
        range 500
        value gu
        xysize (800, 30)
        xalign 0.95
        yalign 0.8
        left_bar "#b964c4" 
        right_bar "#40244f" 
    if gu >= 150 and gu <= 350:
        text "Neutral" xalign 0.78 yalign 0.9
    elif gu<150:
        text "Mala" xalign 0.7 yalign 0.9
    elif gu>350:
        text "Buena" xalign 0.7 yalign 0.9
        