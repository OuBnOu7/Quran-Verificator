import ply.yacc as yacc
from lexer import tokens
from pyarabic import *
from lexer import data

#Fonction Pour Recuperer L'expression sour fromat String
def toString(x):
    y=""
    for i in range(1, len(x)):
        y=y+str(x[i])
    return y    
     

#Source
def p_s(p):
    '''s : aya
        | sourat'''

#Input Type

def p_aya(p):
    '''aya : aya_1_1 
        | aya_2_1 
        | aya_3_1 
        | aya_4_1 
        | aya_5_1 
        | aya_6_1 
        | aya_1_114 
        | aya_2_114 
        | aya_3_114 
        | aya_4_114 
        | aya_5_114 
        | aya_6_114
        | aya_1_113 
        | aya_2_113 
        | aya_3_113 
        | aya_4_113 
        | aya_5_113
        | aya_1_111 
        | aya_2_111 
        | aya_3_111 
        | aya_4_111 
        | aya_5_111'''

def p_sourat(p):
    '''sourat : sourat_alnass 
        | sourat_alfatiha
        | sourat_alfalak
        | sourat_almassad'''
    print("----------------")

#Sourat List
def p_sourat_alfatiha(p):
    'sourat_alfatiha : aya_1_1 aya_2_1 aya_3_1 aya_4_1 aya_5_1 aya_6_1'
    print("Sourat Al-Fatiha")

def p_sourat_alnass(p):
    'sourat_alnass : aya_1_114 aya_2_114 aya_3_114 aya_4_114 aya_5_114 aya_6_114'
    print("Sourat Al-Nass")

def p_sourat_alfalak(p):
    'sourat_alfalak : aya_1_113 aya_2_113 aya_3_113 aya_4_113 aya_5_113'
    print("Sourat Al-Falak")

def p_sourat_almassad(p):
    'sourat_almassad : aya_1_111 aya_2_111 aya_3_111 aya_4_111 aya_5_111'
    print("Sourat Al-Massad")    


#-----------------------------------------------------#
#Sourat Al-Fatiha 1
# "الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين إياك نعبد وإياك نستعين اهدنا الصراط المستقيم صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين"


def p_aya_1_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_1 : nom particule Ism_Jalala nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 1 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "الحمد لله رب العالمين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("الحمد لله رب العالمين","\n") 
        print("Praise be to Allah, the Cherisher and Sustainer of the worlds;","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("الحمد لله رب العالمين","\n")

def p_aya_2_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_1 : Ism_Jalala Ism_Jalala' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "الرحمن الرحيم".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("الرحمن الرحيم","\n") 
        print("Most Gracious, Most Merciful;","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("الرحمن الرحيم","\n")

def p_aya_3_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_1 : nom nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "مالك يوم الدين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("مالك يوم الدين","\n") 
        print("Master of the Day of Judgment.","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("مالك يوم الدين","\n")

def p_aya_4_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_1 : nom verbe_present particule nom verbe_passe' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "إياك نعبد وإياك نستعين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("إياك نعبد وإياك نستعين","\n") 
        print("Thee do we worship, and Thine aid we seek.","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("إياك نعبد وإياك نستعين","\n")

def p_aya_5_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_1 : verbe_amr nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "اهدنا الصراط المستقيم".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("اهدنا الصراط المستقيم","\n") 
        print("Show us the straight way,","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("اهدنا الصراط المستقيم","\n")

def p_aya_6_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_6_1 : nom nom verbe_passe particule pronom nom nom particule pronom particule nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 6 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين","\n") 
        print("The way of those on whom Thou hast bestowed Thy Grace, those whose (portion) is not wrath, and who go not astray.","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين","\n")

#-----------------------------------------------------#
#Sourat Al-Nass 114
#"قل أعوذ برب الناس ملك الناس إله الناس من شر الوسواس الخناس الذي يوسوس في صدور الناس من الجنة والناس"

def p_aya_1_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_114 : verbe_amr verbe_passe particule nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 114 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "قل أعوذ برب الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("قل أعوذ برب الناس","\n") 
        print("Say: I seek refuge with the Lord and Cherisher of Mankind,","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("قل أعوذ برب الناس","\n")

def p_aya_2_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_114 : nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ملك الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ملك الناس","\n") 
        print("The King (or Ruler) of Mankind,","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("ملك الناس","\n")

def p_aya_3_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_114 : Ism_Jalala nom'
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "إله الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("إله الناس","\n") 
        print("The god (or judge) of Mankind,-","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("إله الناس","\n")

def p_aya_4_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_114 : particule nom nom nom ' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "من شر الوسواس الخناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("من شر الوسواس الخناس","\n") 
        print("From the mischief of the Whisperer (of Evil), who withdraws (after his whisper),-","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("من شر الوسواس الخناس","\n")   

def p_aya_5_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_114 : pronom_r verbe_passe particule nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "الذي يوسوس في صدور الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("الذي يوسوس في صدور الناس","\n") 
        print("(The same) who whispers into the hearts of Mankind,-","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("الذي يوسوس في صدور الناس","\n")          

def p_aya_6_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_6_114 : particule nom particule nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 6 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "من الجنة والناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("من الجنة والناس","\n")     
        print("Among Jinns and among men.","\n")     
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("من الجنة والناس","\n")  

#-----------------------------------------------------#
#Sourat Al-Falak 113
#"قل أعوذ برب الفلق من شر ما خلق ومن شر غاسق إذا وقب ومن شر النفاثات في العقد ومن شر حاسد إذا حسد"
    
def p_aya_1_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_113 : verbe_amr verbe_passe particule nom nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 113 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "قل أعوذ برب الفلق".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("قل أعوذ برب الفلق","\n")  
        print("Say: I seek refuge with the Lord of the Dawn","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("قل أعوذ برب الفلق","\n")    

def p_aya_2_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_113 : particule nom negation verbe_passe' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "من شر ما خلق".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("من شر ما خلق","\n")  
        print("From the mischief of created things;","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("من شر ما خلق","\n")    

def p_aya_3_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_113 : particule particule nom nom nom verbe_passe'
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ومن شر غاسق إذا وقب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ومن شر غاسق إذا وقب","\n")  
        print("From the mischief of Darkness as it overspreads;","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("ومن شر غاسق إذا وقب","\n")    

def p_aya_4_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_113 : particule particule nom nom particule nom ' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ومن شر النفاثات في العقد".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ومن شر النفاثات في العقد","\n")  
        print("From the mischief of those who practise secret arts;","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("ومن شر النفاثات في العقد","\n")    

def p_aya_5_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_113 : particule particule nom nom nom verbe_passe' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ومن شر حاسد إذا حسد".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ومن شر حاسد إذا حسد","\n")  
        print("And from the mischief of the envious one as he practises envy.","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("ومن شر حاسد إذا حسد","\n")     

#-----------------------------------------------------#
#Sourat Al-Massad 111
#"تبت يدا أبي لهب وتب ما أغنى عنه ماله وما كسب سيصلى نارا ذات لهب وامرأته حمالة الحطب في جيدها حبل من مسد"    

def p_aya_1_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_111 : verbe_passe nom nom nom particule verbe_passe' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 111 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "تبت يدا أبي لهب وتب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("تبت يدا أبي لهب وتب","\n")  
        print("Perish the hands of the Father of Flame! Perish he!","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("تبت يدا أبي لهب وتب","\n")   

def p_aya_2_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_111 : negation verbe_passe particule pronom nom pronom particule negation verbe_passe' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 111 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ما أغنى عنه ماله وما كسب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ما أغنى عنه ماله وما كسب","\n") 
        print("No profit to him from all his wealth, and all his gains!","\n") 
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("ما أغنى عنه ماله وما كسب","\n")            

def p_aya_3_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_111 : verbe_present nom nom nom'
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 111 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "سيصلى نارا ذات لهب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("سيصلى نارا ذات لهب","\n")  
        print("Burnt soon will he be in a Fire of Blazing Flame!","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("سيصلى نارا ذات لهب","\n")   

def p_aya_4_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_111 : particule nom pronom nom nom ' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 111') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "وامرأته حمالة الحطب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("وامرأته حمالة الحطب","\n")  
        print("His wife shall carry the (crackling) wood - As fuel!-","\n")  
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("وامرأته حمالة الحطب","\n")    

def p_aya_5_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_111 : particule nom pronom nom particule nom' 
    print("*****************************")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 111')  
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "في جيد ها حبل من مسد".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("في جيد ها حبل من مسد","\n")
        print("A twisted rope of palm-leaf fibre round her (own) neck!","\n")
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("في جيد ها حبل من مسد","\n")    

def p_error(p):
    print("*****************************")
    print("Erreur Syntaxique : ",p)

    

#"الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين إياك نعبد وإياك نستعين اهدنا الصراط المستقيم صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين"
#"قل أعوذ برب الناس ملك الناس إله الناس من شر الوسواس الخناس الذي يوسوس في صدور الناس من الجنة والناس"
#"قل أعوذ برب الفلق من شر ما خلق ومن شر غاسق إذا وقب ومن شر النفاثات في العقد ومن شر حاسد إذا حسد"
#"تبت يدا أبي لهب وتب ما أغنى عنه ماله وما كسب سيصلى نارا ذات لهب وامرأته حمالة الحطب في جيدها حبل من مسد"

parser = yacc.yacc()
res = parser.parse(data)
print(res)          
