import csv
import ply.lex as lex
 
 # List of token names.   This is always required
tokens = (
   'nom',
   'verbe_amr','verbe_passe','verbe_present',
   'Ism_Jalala',
   'pronom','pronom_d','pronom_r',"nom_defini",'particule','negation'

)

 # Regular expression rules for simple tokens

t_particule    = r'علي|من | إلى | حتى |خلا |حاشا |عدا |في |عن |على |مذ |منذ |رب |ل |كي |و |ك |ب |لعل |متى '
t_verbe_amr    = r'اهدنا|قل'
t_verbe_present    = r'نعبد|سيصلى'
t_pronom_d = r'هَذا|ذَلِكَ|هَذِهِ | تِلْكَ|أولئك '
t_pronom_r = r'اللاتِ | اللاتي|الذي| اللاءِ| اللائي| مَنْ| ما| ذو| ذا| الّذينَ| الّذونَ| الّذينَ| الّذي| الّتي| اللتَينِ'

def t_nom(t):
    r'شر |الوسواس |الخناس|أحد|لا|الضالين| غير| المغضوب|كفوا|الذين|صراط| الذين| الصراط |المستقيم|مالك| يوم |الدين|العالمين|رب|إياك|صدور|الحمد|ملك|مال|الجنة|الناس|غاسق|الفلق|العقد|يدا|أبي|لهب|نارا|ذات|لهب|امرأت|حمالة|الحطب|جيد|حاسد|النفاثات|حبل|مسد|إذا|سم'
    return t 

def t_Ism_Jalala(t):
    r'له|الله|الرحمن|الرحيم|الصمد|إله'
    return t

def t_negation(t):
    r'لم|لا|ما'
    return t 

def t_pronom(t):
    r'أنا| أنت|هو| هي| هي| هو| نحن|أنتم| أنتن|ها|هم|ه| هن'   
    return(t) 
def t_verbe_passe(t):
    r'أنعمت|أغنى|تبت|تب|كسب|حسد|وقب|يوسوس|نستعين|أعوذ|يلد|يولد|خلق|يكن'
    return(t) 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
lexer = lex.lex()

# "الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين إياك نعبد وإياك نستعين اهدنا الصراط المستقيم صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين"
#"قل أعوذ برب الناس ملك الناس إله الناس من شر الوسواس الخناس الذي يوسوس في صدور الناس من الجنة والناس"
#"قل أعوذ برب الفلق من شر ما خلق ومن شر غاسق إذا وقب ومن شر النفاثات في العقد ومن شر حاسد إذا حسد"
#"تبت يدا أبي لهب وتب ما أغنى عنه ماله وما كسب سيصلى نارا ذات لهب وامرأته حمالة الحطب في جيدها حبل من مسد"

data = input('Entrer une Aya Ou Une Sourate :')
print("---------------------------------")     
print("Vous Avez Entrez : ",data)     
print("---------------------------------")     
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        print("---------------------------------")         
        break      
    print(tok)
