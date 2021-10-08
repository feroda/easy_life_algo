#!/usr/bin/env python


# Durante il giorno
while True:

    # Scegli casualmente un elemento dalla tua lista di cose da fare
    what_i_like_now = random.choice(... set of items in my todo list…)

    # Imposta una variabile di nome "end", avremo potuto chiamarla "finito" a False
    end = False

    # Fintanto che rimane False
    while not end:

        # Fai uno step dell'elemento scelto
        end = do_a_step(what_i_like_now)

        # Se "end" (o "finito") è vera, oppure se avviene un evento
        if end or there_is(an_interrupt):

            # esci da questo ciclo
            # (prosegue dall'istruzione "what_i_like_now = ...")
            break
