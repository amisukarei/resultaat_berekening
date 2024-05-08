'''definier een functie die breuken die resultaten voorstellen, gescheiden door spaties
    herkent en de teller en noemer splitst en dan deze bij totaal_noemer en totaal_teller voegt om
    het totale resulaat met totaal_teller/totaal_noemer te doen'''
    
    
def berekenen_resultaten(prompt, categorie):
  
 totaal_teller = 0
 totaal_noemer = 0
 
 resultaten_rij = input(prompt)

 for resultaat in resultaten_rij.split():
   
   try:
     
      teller, noemer = resultaat.split('/')
      teller = float(teller)
      noemer = float(noemer)
      
      if noemer <= 0 or teller <=0 : 
        
       print("Noemers en tellers  moeten groter zijn dan 0")  
       continue
     
   except ValueError:
       
     print("Foute Invoer. Probeer opnieuw of typ 'stop' om te stoppen")
     continue
    
   totaal_teller += teller
   totaal_noemer += noemer
   

 if totaal_noemer != 0:
   
      verhouding =  (round(totaal_teller/totaal_noemer * 100, 1))
      print("Je resultaat voor je", categorie,"is:",verhouding, "%")
      
      return verhouding
    
 else:
   
     print("Er zijn geen resultaten ingevoerd.")  
     return 0