init python:
    
    ga = Gallery()

    ga.button("Imagenes1")
    ga.condition("persistent.Imagenes1")
    ga.image("Scenas/Creador_feliz.png")
    ga.image("Scenas/Creador_indiferente.png")
    ga.image("Scenas/Creador_insano.png")
    ga.image("Scenas/Creador_insano(f).png")
    ga.image("Scenas/Creador_serio.png")
    ga.image("Creador_Glitch")

screen galeria:
    tag menu
    use game_menu(_("Galeria"), scroll="viewport"):
        hbox:
            frame:
                background None
                xpos 225
                grid 3 4:
                    spacing 20
                    add ga.make_button("Imagenes1","Scenas/Vista_Imagen_1.png", locked = "Scenas/image_locked.png")
                    add "Scenas/image_locked.png"
                    add "Scenas/image_locked.png"
                    add "Scenas/image_locked.png"
                    add "Scenas/image_locked.png"
