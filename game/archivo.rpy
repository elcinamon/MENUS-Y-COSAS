screen archivo:
    tag menu
    add "17538.jpg"
    add "gui/archivo.png"
    imagebutton auto "gui/Iconos/Saltar_%s.png" action ShowMenu("archivo_pag2") xpos 0.9 ypos 0.5
    textbutton _("Volver") action Return() xpos 0.03 ypos 0.9

screen archivo_pag2:
    tag menu
    add "17538.jpg"
    add "gui/archivo_pag2.png"
    imagebutton auto "gui/Iconos/Atras_%s.png" action ShowMenu("archivo") xpos 0.02 ypos 0.5
    imagebutton auto "gui/Iconos/Saltar_%s.png" action ShowMenu("archivo_pag3") xpos 0.9 ypos 0.5
    textbutton _("Volver") action Return() xpos 0.03 ypos 0.9

screen archivo_pag3:
    tag menu 
    add "17538.jpg"
    add "gui/archivo_pag3.png"
    imagebutton auto "gui/Iconos/Atras_%s.png" action ShowMenu("archivo_pag2") xpos 0.02 ypos 0.5
    textbutton _("Volver") action Return() xpos 0.03 ypos 0.9
