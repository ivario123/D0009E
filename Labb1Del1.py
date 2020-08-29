def recept(antal):
    print("\nRecept för : {} personer : \n".format(antal))
    import math
    faktor = antal/4
    #///////////////////////////////////////////////////////////////////////////////////////
    #----------Eftersom att det går åt en form till 4 pers går det två till 8 osv----------
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #region till formen
    print("\nTill formen:")
    print("Smör : {}g".format(math.ceil(faktor)*10))
    print("Ströbröd : {}dl\n".format(math.ceil(faktor)*0.75))
    #endregion
    #region till sockerkakan
    print("Sockerkakan:")
    print("Ägg : {}st".format(round(faktor*3)))
    print("Strösocker : {}dl".format(faktor*3))
    print("Vaniljsocker : {}tsk".format(faktor*2))
    print("Bakpulver : {}tsk".format(faktor*2))
    print("Vetemjöl : {}dl".format(faktor*3))
    print("Smör : {}g".format(75*faktor))
    print("Vatten : {}dl\n".format(faktor))
    
    #endregion
#///////////////////////////////////////////////////////////////////////////////////////
#--------Anänder lambda istället för vanliga funktioner tycker att det är snyggare-----
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
tidblanda = lambda antal:10+antal
tidgradda = lambda antal:30+3*antal  
sockerkaka = lambda antal : [recept(antal),print("Tillagningstid : {}min".format(tidblanda(antal)+tidgradda(antal)))]
if __name__ == "__main__":
    sockerkaka(4)
    sockerkaka(7)
    