## 3. Namnrymder och namngivning
"""
Med en ständigt ökande ström av paket så är det ofrånkomligt ett problem att en
del funktioner kommer att ha samma namn. Lösningen kallas för namnrymder (namespace).
Det här har dels att göra med scopes som vi lärde oss om i funktioner. Lokala
variabler kan sägas existera i en egen namnrymd, men det är också något som
görs vid import. I den här övningen ska vi undersöka hur det fungerar med
två moduler som har samma namn på olika funktioner, i det här fallet gör de
motsvarande saker, men den en för komplexa tal, den andra för vanliga.

Uppgifter:
    1. Gör ett program där du importerar hela modulerna math och cmath genom att skriva

    import math
    import cmath

    2. Skriv ut resultaten för de olika metoderna math.sin(1) och cmath.sin(1)
    3. Notera skillnaden i resultat. (tips använd "type()")
    4. Gör ett nytt program med samma innehåll, där du importerar följande:

    from math import sin
    from cmath import sin

    5. Skriv ut resultatet av sin(1)
    6. Gör ett till likadant program, men byt ordning på importsatserna.
       Vad blir det för skillnad i resultaten? Varför?
    7. Skapa ytterliggare ett program men importera istället så här:

    from math import sin
    from cmath import sin as csin

    8. Skriv ut värden för både sin(1) och csin(1)

"""

import math
import cmath

print(math.sin(1))
print(cmath.sin(1))
