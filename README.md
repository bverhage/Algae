# Algae
Modeleren

Model dat gebruik maakt van classes zodat variabelen handig over te dragen zijn naar verschillende files. 

Naast het basismodel, zijn stroming en en diffusie meegenomen. 

Inmiddels werken diffusie en stroming redelijk. Wel is er nog een probleem met ophoping bij stroming naar de randen. Het opleggen van een constante (Dirichelet) rand leidt tot gekke compensatie respons in het systeem. Een idee geopperd door prof. Heemink is een periodiek systeem introduceren (dus eind gaat helemaal terug naar begin).

Alpha implementatie werkt nog niet als gewenst, waarschijnlijk omdat naar de class gerefereerd moet worden ( transfer.Func(...) i.p.v. enkel Func(...) )
