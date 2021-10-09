# Easy life algorithm

Questo progetto è un gioco, e come ogni gioco è anche una sfida.
La sfida di definire "una splendida giornata". 
Una giornata in cui la felicità finale sia maggiore di quella iniziale.

Una giornata vissuta da guerrieri della Luce.

E voi come implementereste l'algoritmo più semplice per una vita semplice,
verso la felicità?

Per la prima volta ho pubblicato pseudocodice e code su Facebook,
nella mia pagina "Io Scrivo Software Libero"
https://www.facebook.com/ferodafabriano/posts/121869523527451

ed ecco qui lo pseudocodice, la traccia dell'algoritmo:

```
1. Parti da zero: sgombra al mente, avvio del sistema 
2. Per sempre 
    a. scegli ciò che ti piace fare ora
    b. inizia a farlo
    c. finché non termini
        i. se ti appare qualcos’altro
              1. ritorna al punto "a."
```

## easy_life_by_checking.py

In questo file è presente l'implementazione Python dell'algoritmo.

Durante una giornata il processo (umano :-)) sceglie ciò che gli piace fare, 
fa un passo in quella direzione,
poi si ferma per una **verifica**:
se l'attività c'è un evento, allora interrompe il flusso
e riparte con la scelta casuale di un'attività, inclusa quella prodotta dall'evento.

Se l'attività è conclusa, rimuove l'attività dalla memoria.

## easy_life_by_signals.py

Questa implementazione è simile alla precedente, ma si differenzia per un aspetto:
l'interpretazione dei segni. O dei segnali in questo caso ;-)

È più attinente alla realtà in quanto i segnali o gli eventi nella nostra vita
avvegnono indipendentemente da quando noi ci fermiamo nella **fase di verifica**.

Per questo viene definita la funzione `stop_what_I_am_doing` come "handler", 
ossia gestore dei segnali inviati dal sistema (Natura) in questo caso si chiamano SIGTERM e SIGINT, ma potrebbero essere altri.

Ne consegue che l'essere umano di vita facile, si appoggia alla Natura per le proprie decisioni:

1. sceglie una tra le attività che ha nel suo contesto ora (chiamiamolo MEMORY)
2. e la fa, prendendosi delle pause, finché non la finisce e ne sceglierà un'altra

Se indipendentemente dalla sua volontà arrivano dei segni,

3. Ferma quello che sta facendo e riparte dal punto 1.

Da notare che alla ripartenza il contesto di scelta sarà cambiato, perché includerà anche le ragioni per cui lui o lei hanno percepito l'interruzione.

## Conclusioni

Questo è un gioco, ma se aiuta a vivere meglio, più felici, più costruttivi e più collaborativi, allora è anche educazione e autoeducazione per chi raccoglie la sfida.

I concetti qui espressi sono talmente semplici che chiamo amichevolmente:
**"Il segreto di ciuffichetto"**, e mi chiedo:

forse a qualcuno, come a me, piace giocare su questi aspetti, immaginare e 
raccogliere con la felicità dello stupore che al di là di tutte le apparenze,
la realtà può essere interpretata in modo veramente semplice ed esiste 
un'unica potente, determinata, bellissima, simpatica e "femminile" forza 
che ci presenta sempre ciò che è giusto e bello per noi.

In un unico stupendo istante definito dai grandi maestri come:

- L'eterno ritorno dell'identico;
- Ichinen Sanzen: tremila regni in un singolo istante di vita;
- Adesso;
- Axé.
