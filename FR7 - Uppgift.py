# Uppgifter import
## 1. Installera paket med PIP

""" 

Inledning
Pakethanterare är ett väldigt viktigt verktyg för en programmeringshanterare,
och PIP är det vanligaste när det gäller Python. I den här övningen installerar
vi två paket, numpy och pandas, som är väldigt användbara i många olika lägen.

Uppgifter
    1. Kör ett kommando för att uppgradera pip "python -m pip install --upgrade pip"
    2. Kontrollera om du redan har numpy och panda, tips "pip list", "pip show <paketnamn>"
"""

## 2. Virtuell miljö
"""
Bygg upp en virtuell miljö för övningarna: https://docs.python.org/3/library/venv.html

Uppgifter:
    1. Kör kommandot "pip list" vad händer? varför?
    2. Använd pakethanteraren pip för att installera numpy och pandas (tips pip install)
"""

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

## 4. Att använda färdiga paket
"""
I python är det väldigt vanligt att använda olika paket, och det går inte att
lära ut alla av dem. Däremot går det att lära ut metoder för att hantera dem
ändå. En viktig del av detta är att söka på nätet. Den här övningen är därför
tänkt att delvis vara en lektion i pandas och numpy, men mest i att söka egen
information.

Uppgifter:

Skriv ett program som låter användaren mata in 12 tal. Gör dessa till
tre numpy arrays med fyra tal i varje, sätter samman dessa till en pandas
dataframe och slutligen skriver ut dataframen.

Specifikation:
1. Skriv ett program som importerar pandas som pd och numpy som np.
2. Ta input på tolv stycken tal. Försök att låta användaren förstå vad det är hen matar in.
3. Dela upp de inmatade talen i listor
4. Konvertera listorna till numpy-arrays
5. Kombinera dessa numpy-arrayer till en dataframe.
6. Skriv ut dataframen på skärmen.


Kommentarer
Det här är ett vanligt arbetssätt, att hitta något paket som löser ens uppgift, och
därefter söka efter dokumentation på nätet. En risk är att när man möter den
här typen av motstånd, så jobbar man mer med att få det att över huvud taget
fungera, än att få koden snygg och prydlig. Det här är också en demonstration
av hur pandas hjälper till med formatering av utskrifter
"""

# Att läsa andra människors kod
"""
Det är inte bara när man hämtar paket som är färdiga som man använder
andra människors kod. Ganska ofta får man ärva en existerande kod för att
göra ändringar i. Den här uppgiften går ut på att prova på vilka utmaningar
och förtjänster det har att ta över någon annans kod.

4.2 Uppgift
1. Lägg upp din kod från förra övningen i github.

    # Ta hem lektionens repository
    git clone https://github.com/robert-alfwar/lektion7.git

    # Gå till foldern
    cd lektion7

    # Öppna vscode
    code .

    # Skapa en folder med ditt github användarnamn, där lägger din kod
    mkdir "ditt användarnamn" eller via vscode knappen

    # Skapa en branch (VIKTIG)
    git branch "ditt användarnamn"
    git checkout "ditt användarnamn"

    # Kontrollera du är på rätt branch med
    git branch

    # lägg till filer
    git add "dina filer"

    # Kontrollera rätt filer är tillagda
    git status

    # Committa filer
    git commit -m "meddelande"

    # Pusha filer
    git push (Läs felmedelandet och sätt upstream enligt instruktion)

    # Gå till github och verifiera din branch finns och koden är korrekt.

2. Hitta någon annans upplagda kod (Finns där ingen, så gör lite extra
övningar tills det gör det)

3. Modifiera den koden så att:
(a) Pandas skriver ut årtalen 2017-2019 som rubrik för varje array
(b) Pandas skriver ut Q1, Q2, Q3 och Q4 som rubrik för varje element i
arrayerna
(c) Användaren vid inmatning får information om vad hen skriver in.

4.3 Utförande
Det här är svårt att beskriva, då det beror mycket på hur koden du får se ut.
Men börja med att läsa igenom den och fundera på vad som är vad. Börja med
den ändring du tycker verkar lättast.

4.4 Kommentarer
Det här är en ganska svår övning, eftersom olika människor har olika stil. Men
det brukar vara när man läser andras kod som man förstår varför den ska vara
lättläst, samt vad som är det.
"""
