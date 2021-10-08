#!/usr/bin/env python

"""
Nuovo algoritmo per una vita semplice:

simile a `easy_life_by_checking.py`, ma con l'importante differenza che
durante la giornata non perdiamo tempo a verificare ogni volta se avviene un evento.
È il sistema (la Natura nel nostro caso) che ci segnala l'evento che noi intercettiamo
terminando ciò che stiamo facendo `stop_what_I_am_doing`
"""

# Carica un modulo (libreria software) per la gestione dei segnali del sistema
import signal

# Alcuni pensieri/immagini nella tua memoria...
MEMORY = [ "fishing", "solve problem 1", "running", "make a call"]

# Imposta la variabile "end_flag" (o potevo chiamarla "finito") a False
end_flag = False

# Definisci una funzione "stop_what_I_am_doing"
def stop_what_I_am_doing(signum, frame):

    # Imposta la variabile "end_flag" (o "finito") a True
    global end_flag
    end_flag = True
    # Scrive un messaggio
    print(f"SIGHANDLER: Received termination signal ({signum})")


# Collega la ricezione degli eventi SIGTERM e SIGINT alla funzione "stop_what_I_am_doing"
# Quando il programma riceve quei segnali invoca la funzione
signal.signal(signal.SIGTERM, stop_what_I_am_doing)
signal.signal(signal.SIGINT, stop_what_I_am_doing)

# Per sempre
while True:

    # Scegli casualmente un elemento da ciò che hai in mente ora
    what_i_like_now = random.choice(MEMORY)

    
    # Imposta la variabile "end_flag" a False
    end_flag = False

    # Fintanto che "end_flag" rimane a False
    while not end_flag:

        # Fai uno step dell'elemento scelto
        end_flag = do_a_step(what_i_like_now)

        # Fai una pausa
        do_some_pause(bath/breathe/drink/eat/...)

    if end_flag:
        # Se l'attività è terminata => rimuovila dalla memoria
        MEMORY.remove(what_i_like_now)
