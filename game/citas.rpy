label ira:
    "Ira"
    if persistent.cita_ira == 0:
        "Esta es la cita 1"
        show Ira_Normal
        $ persistent.cita_ira += 1;
    elif persistent.cita_ira == 1:
        "Esta es la cita 2"
        $ persistent.cita_ira += 1;
    elif persistent.cita_ira == 2:
        "Esta es la cita 3"
    elif persistent.cita_ira >=3:
        "Ya has acompletado las citas de Ira"
        jump citas

return

label gula:
    "Gula"
    if persistent.cita_gula == 0:
        "Esta es la cita 1"
        $ persistent.cita_gula += 1;
    elif persistent.cita_gula == 1:
        "Esta es la cita 2"
        $ persistent.cita_gula += 1;
    elif persistent.cita_gula == 2:
        "Esta es la cita 3"
        $ persistent.cita_gula += 1;
    elif persistent.cita_gula >=3:
        "Ya has acompletado las citas de gula"
        jump citas

return