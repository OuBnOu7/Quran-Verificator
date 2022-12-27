import ply.yacc as yacc
from lexer import tokens
from lexer import *
from pyarabic import *
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Checking')
root.geometry('700x400')
root.configure(bg="#dae6f6")
bg=PhotoImage(file='Qur_an_and_Rehal.png')
mylabel=Label(root,image=bg,bg="black")
mylabel.place(x=0,y=0,relwidth=1,relheight=1)
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
    'aya_1_1 : mot particule Ism_Jalala mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 1 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "الحمد لله رب العالمين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("الحمد لله رب العالمين","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 1\nSourat : 1 \nالحمد لله رب العالمين',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=250)
        #output.pack()

def p_aya_2_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_1 : Ism_Jalala Ism_Jalala' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "الرحمن الرحيم".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("الرحمن الرحيم","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 2\nSourat : 1\n الرحمن الرحيم',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=250)
        #output.pack()

def p_aya_3_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_1 : mot mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "مالك يوم الدين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("مالك يوم الدين","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct:\nAya : 3 \nSourat : 1 \nمالك يوم الدين',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=880,y=250)
        #output.pack()

def p_aya_4_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_1 : mot verbe_present particule mot verbe_passe' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "إياك نعبد وإياك نستعين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("إياك نعبد وإياك نستعين","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 4\nSourat : 1 \n إياك نعبد وإياك نستعين',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=350)

def p_aya_5_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_1 : verbe_amr mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "اهدنا الصراط المستقيم".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("اهدنا الصراط المستقيم","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct:\nAya : 5\nSourat : 1\n اهدنا الصراط المستقيم',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=350)
        #output.pack()

def p_aya_6_1(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_6_1 : mot mot verbe_passe particule pronom mot mot particule pronom particule mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 6 \nSourat : 1 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين","\n")
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct:\nAya : 6\nSourat : 1\n صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=880,y=350)
        #output.pack() 

#-----------------------------------------------------#
#Sourat Al-Nass 114
#"قل أعوذ برب الناس ملك الناس إله الناس من شر الوسواس الخناس الذي يوسوس في صدور الناس من الجنة والناس"

def p_aya_1_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_114 : verbe_amr verbe_passe particule mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 114 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "قل أعوذ برب الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("قل أعوذ برب الناس","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 1\nSourat : 114 \n  قل أعوذ برب الناس ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=250)

def p_aya_2_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_114 : mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ملك الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ملك الناس","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 2\nSourat : 114\n  ملك الناس',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=250)

def p_aya_3_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_114 : Ism_Jalala mot'
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "إله الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("إله الناس","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 3\nSourat : 114\n   إله الناس ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=880,y=250)

def p_aya_4_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_114 : particule mot mot mot ' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "من شر الوسواس الخناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("من شر الوسواس الخناس","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 4\nSourat : 114\n من شر الوسواس الخناس',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=350)

def p_aya_5_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_114 : pronom_r verbe_passe particule mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "الذي يوسوس في صدور الناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("الذي يوسوس في صدور الناس","\n") 
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 5\nSourat : 114\n الذي يوسوس في صدور الناس ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=350)

def p_aya_6_114(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_6_114 : particule mot particule mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 6 \nSourat : 114 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "من الجنة والناس".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("من الجنة والناس","\n")
        output=Label(root,text='- Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 6\nSourat : 114\nمن الجنة والناس',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=880,y=350)     

#-----------------------------------------------------#
#Sourat Al-Falak 113
#"قل أعوذ برب الفلق من شر ما خلق ومن شر غاسق إذا وقب ومن شر النفاثات في العقد ومن شر حاسد إذا حسد"
    
def p_aya_1_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_113 : verbe_amr verbe_passe particule mot mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 113 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "قل أعوذ برب الفلق".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("قل أعوذ برب الفلق","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 1\nSourat : 113 \n قل أعوذ برب الفلق ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=250) 

def p_aya_2_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_113 : particule mot negation verbe_passe' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "من شر ما خلق".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("من شر ما خلق","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 2\nSourat : 113 \n  من شر ما خلق ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=250)  

def p_aya_3_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_113 : particule particule mot mot mot verbe_passe'
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ومن شر غاسق إذا وقب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ومن شر غاسق إذا وقب","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 3\nSourat : 113 \n  ومن شر غاسق إذا وقب ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=880,y=250)  

def p_aya_4_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_113 : particule particule mot mot particule mot ' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ومن شر النفاثات في العقد".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ومن شر النفاثات في العقد","\n")  
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 4\nSourat : 113 \n  ومن شر النفاثات في العقد',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=350) 

def p_aya_5_113(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_113 : particule particule mot mot mot verbe_passe' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 113 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ومن شر حاسد إذا حسد".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ومن شر حاسد إذا حسد","\n")
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 5\nSourat : 113 \n  ومن شر حاسد إذا حسد',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=350)   

#-----------------------------------------------------#
#Sourat Al-Massad 111
#"تبت يدا أبي لهب وتب ما أغنى عنه ماله وما كسب سيصلى نارا ذات لهب وامرأته حمالة الحطب في جيدها حبل من مسد"    

def p_aya_1_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_1_111 : verbe_passe mot mot mot particule verbe_passe' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 1 \nSourat : 111 \n')
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "تبت يدا أبي لهب وتب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("تبت يدا أبي لهب وتب","\n")  
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 1\nSourat : 111 \n تبت يدا أبي لهب وتب ',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=250)  

def p_aya_2_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_2_111 : negation verbe_passe particule pronom mot pronom particule negation verbe_passe' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 2 \nSourat : 111 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "ما أغنى عنه ماله وما كسب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("ما أغنى عنه ماله وما كسب","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 2\nSourat : 111 \n ما أغنى عنه ماله وما كسب',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=250)  

def p_aya_3_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_3_111 : verbe_present mot mot mot'
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 3 \nSourat : 111 \n') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "سيصلى نارا ذات لهب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("سيصلى نارا ذات لهب","\n") 
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 3\nSourat : 111 \n  سيصلى نارا ذات لهب',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=880,y=250) 

def p_aya_4_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_4_111 : particule mot pronom mot mot ' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 4 \nSourat : 111') 
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "وامرأته حمالة الحطب".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("وامرأته حمالة الحطب","\n")  
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 4\nSourat : 111 \nوامرأته حمالة الحطب',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=80,y=350)

def p_aya_5_111(p):
    #Partie Syntaxique Ou On Va Verifier Si Le Verset Est Syntaxiquement Correcte
    'aya_5_111 : particule mot pronom mot particule mot' 
    print("***********")
    print('- Al-Aya est Syntaxiquement Correct :\nAya : 5 \nSourat : 111')  
    #Partie Semantique Ou On Va Verifier Si Le Verset Est Correct 
    if toString(p) == "في جيد ها حبل من مسد".replace(" ", ""):
        print("- Al-Aya Est Coraniquement Correct :")
        print("في جيد ها حبل من مسد","\n")
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 5\nSourat : 111 \nفي جيد ها حبل من مسد',font=("arial",12),bg='#F9E79F',fg='black')
        output.place(x=480,y=350)
    else:
        print("- Al-Aya Est Coraniquement INCORRECTE")
        print("Correction :")
        print("في جيد ها حبل من مسد","\n")
        output=Label(root,text='-Al-Aya est Syntaxiquement et Coraniquement Correct :\nAya : 5\nSourat : 111 \nفي جيد ها حبل من مسد',font=("arial",12),bg='#F9E79F',fg='#053339')
        output.place(x=480,y=350)    

def p_error(p):
    print("***********")
    print("Erreur Coranique : ",p)
    output=Label(root,text='-Une-Aya est Coraniquement Incorrect\n et son numero est le numero de la position vide  ',font=("arial",12),bg='red',fg='black')
    output.place(x=480,y=180)


    

# "الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين إياك نعبد وإياك نستعين اهدنا الصراط المستقيم صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين"
#"قل أعوذ برب الناس ملك الناس إله الناس من شر الوسواس الخناس الذي يوسوس في صدور الناس من الجنة والناس"
#"قل أعوذ برب الفلق من شر ما خلق ومن شر غاسق إذا وقب ومن شر النفاثات في العقد ومن شر حاسد إذا حسد"
#"تبت يدا أبي لهب وتب ما أغنى عنه ماله وما كسب سيصلى نارا ذات لهب وامرأته حمالة الحطب في جيدها حبل من مسد"

#parser = yacc.yacc()
#parser.parse("الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين إياك نعبد وإياك نستعين اهدنا الصراط المستقيم صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين")
# print(res)       


def checker():
    parser = yacc.yacc()
    res = parser.parse(data)
    print(res)  

heading=Label(root,text='السورة أو الآية ادخل',font=("Trebuchet MS",30,"bold"),bg="black",fg="#F9E79F")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="right",width=55,font=('poppins',25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()
button=Button(root,text="  ابدأ  ",font=("arial",17,"bold"),fg="white",bg="#784212",command=checker)
button.place(x=1150,y=113)


root.mainloop()