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
import numpy
import pandas

# count och de 3 tomma listorna, count används för separera listorna
count=0
nump_array1 = []
nump_array2 = []
nump_array3 = []

# Listorna separeras i while-loopen via count som överstigen ett visst antal tex första listan har 4 tal i sig innan counter<=3 och den skriver andra listan.
while count<12:
    if count <=3:
        num = input(f'Ange tal för år 2017: ')
        nump_array1.append(num)
    elif count>3 and count<=7:
        num = input(f'Ange tal för år 2018: ')
        nump_array2.append(num)
    else :
        num = input(f'Ange tal för år 2019: ')
        nump_array3.append(num)
    count= count + 1

# listorna ändras till numpy arrays som sedan skrivs in i pandas DataFrame med årtal som kolumner och kvartal som rader
nump_array1 = numpy.array(nump_array1)
nump_array2 = numpy.array(nump_array2)
nump_array3 = numpy.array(nump_array3)
temp_set = [nump_array1,nump_array2,nump_array3]
nump_set = numpy.array(temp_set)
dataset = pandas.DataFrame(data=nump_set,index=['2017:','2018:','2019:'],columns=['Q1','Q2','Q3','Q4'])

# Kommenterade bort prints för varje lista som användes för testa output
# print(nump_array1)
# print(nump_array2)
# print(nump_array3)
print(dataset)