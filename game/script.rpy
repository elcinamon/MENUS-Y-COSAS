# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define g = Character(" ", window_background="gui/textbox_gula.png", namebox_background="gui/namebox_gula.png", what_color = "#281324ff")
define p = Character("Pereza", color="#a29cd9ff", window_background="gui/textbox_pereza.png",namebox_background="gui/namebox_pereza.png")
screen bienvenida:
    text "Hello {glitch=50} my friend {/glitch}" xalign 0.5 yalign 0.5
    dismiss action Return()

screen hola_gula:
    frame:
        xalign 0.0
        yalign 0.1
        ysize 100
        background Solid("#454545ff")
        text "{color=ffffffff}Gula se ha unido a la fiesta{/color}" yalign 0.5

init:
    $ P = 0
    $ gu = 250
    $ gula_conocido = False
    $ cita = 0;

    
image gula_feliz = "Gula_Feliz.png"
image pereza_normal = "Pereza_Normal_R.png"
image ira_normal = "Ira_Normal.png"
image Fondo = "Scenas/Fondo_escena.png"
image Creador = "Scenas/Creador_sin_glitch.png"
image Creador_Glitch:
    "Creador"
    pause 1
    glitch("Creador")
    pause 0.2
    glitch("Creador", offset=60, randomkey=None) 
    pause 0.2
    "Creador"
    pause 0.1
    glitch("Creador")
    pause 0.1
    glitch("Creador", offset=60, randomkey=None) 
    pause 0.1
    "Creador"
    pause 1
    repeat

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    

    scene bg room

    call screen bienvenida

    call introducir_texto

    "Buenas"

    scene Fondo
    show Creador_Glitch

    " "

    hide Creador_Glitch with dissolve
    scene bg room

    $ gula_conocido = True 
    $ persistent.Imagenes1 = True
    show gula_feliz
    g "Holi"

    show screen hola_gula with moveinleft
    pause 1
    hide screen hola_gula with dissolve


    
    show gula_feliz at left
    with moveinleft

    show pereza_normal with dissolve
    show pereza_normal at right
    with moveinright

    p "..."

    hide gula_feliz
    hide pereza_normal

    "¿Deseas salir un rato?"
    menu:
        "Sí":
            jump citas
        "No":
            p "Mejor ire a dormir"
    

return

label introducir_texto:
    python:
            escrito = renpy.input("Escribe algo", length=32)
            escrito = escrito.strip()

    if escrito.strip() == 'Puto' or escrito.strip() == 'puto':
        "porque escribes eso??"

        jump introducir_texto
    else:
        "Hola, tu escribiste [escrito]"
        return

return

label citas:
    $ cita= renpy.random.randint(1,2)
    if cita == 1:
        jump ira
    elif cita == 2:
        jump gula
    elif cita == 3:
        "Soberbia"
    elif cita == 4:
        "Avaricia"
    elif cita == 5:
        "Lujuria"
    elif cita == 6:
        "Envidia"
return

