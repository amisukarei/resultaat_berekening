from def_totaalberekening import berekenen_resultaten # type: ignore

#Vraag gebruiker of deze het totaal al heeft of nog moet berekenen
keuze_totaal_DW1 = input("Heb je het totaal van DW1 al? ") 
if keuze_totaal_DW1 == 'ja':
     totaal_DW1 = float(input("Voer je totaal voor DW1 in "))
     print("Je totaal voor DW1 is:",totaal_DW1,"%")
     
elif keuze_totaal_DW1 == 'nee':
     
     keuze_taak1 = input("Heb je het totaal van je taken (sem 1) al? (ja/nee): ") 
      
          #Als 'ja' werd geantwoord geef resultaat_taken1 deze waarde
          
     if keuze_taak1.lower() == 'ja':  
            
      resultaat_taken1 = float(input("Voer het totaal van je taken in decimaal getal: " ))
      print("Je totaal voor je taken (sem 1) is",resultaat_taken1,"%")

        #als 'nee' werd geantwoord dan word de waarde berekent en toegekent aan resultaat_taken1
     
     elif keuze_taak1  == 'nee':
    
      resultaat_taken1 = berekenen_resultaten("Voer de resulaten van je taken in breuk vorm in gescheiden door spaties: ", "taken (sem 1)")
    
     keuze_DW1 = input("Heb je het totaal van je toetsen (sem1) al? (ja/nee): ")
      
     if keuze_DW1.lower() == 'ja':
    
        resultaat_DW1 = float(input("Voer het totaal van je toetsen in een decimaal getal: "))
        print("Je totaal voor je toetsen (sem 1) is", resultaat_DW1 ,"%")

     elif keuze_DW1.lower() == 'nee':
    
        resultaat_DW1 = berekenen_resultaten("Voer de resulaten van je toetsen in breuk vorm in gescheiden door spaties: ", "toetsen (sem1)")


resultaat_TEX1 = float(input("Voer het totaal van je examen in een decimaal getal: "))
print("Je totaal voor examen 1 is",resultaat_TEX1,"%")



keuze_totaal_DW2 = input("Heb je het totaal van DW2 al? ") 
if keuze_totaal_DW2 == 'ja':
     totaal_DW2 = float(input("Voer je totaal voor DW2 in "))
     print("Je totaal voor DW2 is:",totaal_DW2,"%")
     
elif keuze_totaal_DW2 == 'nee':
     
     keuze_taak2 = input("Heb je het totaal van je taken (sem 2) al? (ja/nee): ") 
      
          #Als 'ja' werd geantwoord geef resultaat_taken1 deze waarde
          
     if keuze_taak2.lower() == 'ja':  
            
      resultaat_taken2 = float(input("Voer het totaal van je taken in decimaal getal: " ))

        #als 'nee' werd geantwoord dan word de waarde berekent en toegekent aan resultaat_taken1
     
     elif keuze_taak2  == 'nee':
         
         resultaat_taken2 = berekenen_resultaten("Voer de resultaten van je taken(sem2) in breukvorm in gescheiden door spaties: ", "taken (sem 2)") 
      
     keuze_DW2 = input("Heb je het totaal van je toetsen (sem2) al? (ja/nee): ")
      
     if keuze_DW2.lower() == 'ja':
    
        resultaat_DW2 = float(input("Voer het totaal van je toetsen in een decimaal getal: "))
        print("Je totaal voor je toetsen (sem 2) is", resultaat_DW2 ,"%")
        totaal_DW2 = 0.9 * resultaat_DW2 + 0.1 * resultaat_taken2

     elif keuze_DW2.lower() == 'nee':
    
         resultaat_DW2 = berekenen_resultaten("Voer de resultaten van je toetsen (sem2) in breukvorm in gescheiden door spaties: ", "toetsen (sem 2)")
         
         totaal_DW2 = 0.1 * resultaat_taken2 + 0.9 * resultaat_DW2  

resultaat_TEX2 = float(input("Voer het totaal van je examen2 in een decimaal getal: "))
print("Je totaal voor examen 2 is",resultaat_TEX2,"%")


totaal_DW  = 0.4 * totaal_DW1 + totaal_DW2 * 0.6
totaal_TEX = 0.4 * resultaat_TEX1 + resultaat_TEX2 * 0.6

totaal =round(0.3 * totaal_DW + totaal_TEX * 0.7, 1)

print("Je totaal dit jaar is: ",totaal,"%")



