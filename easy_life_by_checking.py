#!/usr/bin/env python


# Some stuff in your memory
MEMORY = [ "fishing", "solve problem 1", "running", "make a call"]

# Durante il giorno
while True:

    # Scegli casualmente un elemento da ciò che hai in mente ora
    what_i_like_now = random.choice(MEMORY)

    # Imposta una variabile di nome "end", avremo potuto chiamarla "finito" a False
    end = False

    # Fintanto che rimane False
    while not end:

        # Fai uno step dell'elemento scelto
        end = do_a_step(what_i_like_now)

        # Se "end" (o "finito") è vera, oppure se avviene un evento che interrompe
        if end or there_is(an_event):

            # esci da questo ciclo
            # (prosegue dall'istruzione "what_i_like_now = ...")
            break

    if end:
        # Se l'attività è terminata => rimuovila dalla memoria
        MEMORY.remove(what_i_like_now)
    else:
        MEMORY.insert(stuff_regarding_the_event)
