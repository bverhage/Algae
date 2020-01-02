# Modelleren Algae - Groep A3
## Model

Model dat gebruik maakt van classes zodat variabelen handig over te dragen zijn naar verschillende files. Naast het basismodel, zijn *stroming* en en *diffusie* meegenomen. Moleculair diffusie vindt niet plaats op dezelfde manier voor fytoplankton, maar op grotere schaal kunnen we de uitweiding van concencreerde benaderen met dezelfde soort vergelijkingen (met weliswaar diffusieconstanten met andere orde van grootte). De parameters die hier een rol in spelen moeten nog worden gecalibreerd/gefit of in ieder geval onderbouwd.

Er zijn drie verschillende randvoorwaarden geimplementeerd:
1. Dirichelet
2. Neumann
3. Periodiek

#### Dirichelet (D)
Hier leggen we een constante rand op aan het systeem. Deze constante rand leidt tot gekke compensatie respons in het systeem waardoor het zeker niet fysisch oogt. 

#### Periodiek (P)
Een idee geopperd door prof. Heemink is een periodiek systeem introduceren (dus eind gaat helemaal terug naar begin), nu ook geïmplementeerd. Hierin gaan we ervanuit dat de linker rand en de rechter rand aan elkaar geplakt zijn, vergelijk een lijn over de oceaan die rond de aarde gaat, of een circulair aquarium. Geen gekke respons, maar toepassing is uiteraard beperkt.

#### Neumann (N)
Daarnaast is er nog een Neumann boundary gemaakt met zero flux, deze leidt tot het meest fysische (ogende) resultaat. We gaan er hier bij uit de concentraties net buiten het reservoir gelijk is aan die op de randen van het reservoir.

## Presentatie 
Groep A3 

Woensdagmiddag 8 januari, om 15:00 in Pulse Hall 7

[Link](https://1drv.ms/p/s!AkjAOw2lgIH1mGkt4jHmnD_oNIBQ?e=SyhyR4)

Voor de presentaties zijn ongeveer 12 minuten beschikbaar met daarna nog 3 minuten voor vragen. Er wordt verwacht dat iedereen die op 8 januari een presentatie geeft ook alle andere presentaties op die dag bijwoont, de eerste start om 13:45
