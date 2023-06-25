import time
import tkinter as tk
from tkinter import *

#lllll
def risolvi_sudoku():
    
     

# if you are still working under a Python 2 version, 
    # comment out the previous line and uncomment the following line
    # import Tkinter as tk


    start=time.time()
    def Sudoku():
        Sudoku.var=2
    Sudoku()
    def lista_quadrati():
            lista_quadrati.var=[]
    lista_quadrati()

    #inputsudoku()
    import itertools
    from datetime import datetime
    inizio = datetime.now()
    numeri=[x for x in range(1,10)]
    per=[]
    def hardest_sudoku_ever_created_by_Finnish_matematician_Arto_Inkala():
        a=[8, '', '', '', '', '', '', '', '']
        b=['', '', 3, 6, '', '', '', '', '']
        c=['', 7, '', '', 9, '', 2, '', '']#tempo risoluzione 16 minuti con geany 
                                                #21 minuti e 47 secondi con Anaconda notebook                
        d=['', 5, '', '', '', 7, '', '', '']
        e=['', '', '', '', 4, 5, 7, '', '']
        f=['', '', '', 1, '', '', '', 3, '']
        g=['', '', 1, '', '', '', '', 6, 8]
        h=['', '', 8, 5, '', '', '', 1, '']
        k=['', 9, '', '', '', '', 4, '', '']
    def sudoku_medio():
        a=[9, 2, 6, '', '', 8, '', 1, '']
        b=['', 5, 8, '', 2, '', 3, '', 7]
        c=['', '', '', 5, '', '', 8, 2, '']
        d=['', 9, '', '', 5, 7, '', '', '']
        e=['', '', 3, 9, '', '', '', 7, '']
        f=['', '', '', 6, 1, '', '', '', 5]
        g=[4, 6, '', '', '', '', 7, '', '']
        h=['', '', '', '', '', '', '', 8, '']
        k=[2, '', 1, '', '', '', 6, 9, '']
    #sudoku_medio()
    #LI RISOLVE TUTTI CON LE PERMUTAZIONI , ANCHE I PIU DIFFICILI, ELIMINATI I DEEPLY NESTED LOOPS, NON SONO PIù COSI ANNIDATI.
    #square=[]


    def restituisci_indice_quadrato(x,y):




        if  indice_r.var<=2:
                                        if indice_c.var>=0 and indice_c.var<=2:
                                            indice_quadrato.var=0
                                        elif indice_c.var>=3 and  indice_c.var<=5:
                                            indice_quadrato.var=1
                                        elif indice_c.var>=6 and indice_c.var<=8:
                                             indice_quadrato.var=2


        elif 3<=indice_r.var<=5:
                                                    if indice_c.var>=0 and indice_c.var<=2:
                                                        indice_quadrato.var=3
                                                    elif indice_c.var>=3  and indice_c.var<=5:
                                                        indice_quadrato.var=4
                                                    elif indice_c.var>=6  and indice_c.var<=8:
                                                        indice_quadrato.var=5

        else:
                                                    if indice_c.var>=0  and indice_c.var<=2:
                                                        indice_quadrato.var=6
                                                    elif indice_c.var>=3 and indice_c.var<=5:
                                                        indice_quadrato.var=7
                                                    elif indice_c.var>=6  and indice_c.var<=8:
                                                        indice_quadrato.var=8

        return indice_quadrato.var
    def findsquare():      
                lista_quadrati.var=[]
                for j in range(len(Sudoku.var)):
                    for y in range(len(Sudoku.var)):
                        if len(Sudoku.var)==9: 
                            if j==0 or j==3 or j==6:
                                    if y<=6 and y%3==0:
                                    #quadrato1.var=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
                                    #    square=sudoku1[j:j+3][y:y+3]
                                        square=Sudoku.var[j][y:y+3]+Sudoku.var[j+1][y:y+3]  +Sudoku.var[j+2][y:y+3]
                                        lista_quadrati.var.append(square)
                                     #   print(len(lista_quadrati.var),"lenlistaquad.var")
                            elif len(Sudoku.var)==6:
                                  if j==0 or j==2 or j==4:
                                    if y<=3 and y%3==0:
                                    #quadrato1.var=Sudoku.var[0][0:3]+Sudoku.var[1][0:3]  +Sudoku.var[2][0:3]
                                    #    square=sudoku1[j:j+3][y:y+3]
                                        square=Sudoku.var[j][y:y+3]+Sudoku.var[j+1][y:y+3] 
                                        lista_quadrati.var.append(square)

                restituisci_indice_quadrato(indice_r.var,indice_c.var)                     
    #algoritmo:filtra le permutazioni in base alle cifre iniziali, poi in base alle cifre che può contenere ogni cella vuota (solo le cifre della permutazione in corrispondneza delle celle vuote  corrispondono tante volte quando il numero di celle vuote in ogni riga), poi cerca di "incastrare" tra loro tre righe alla volta ,
    #poi cerca le soluzioni possibili delle prime sei righe ed infine la soluzione finale

    def sudokumalvagio2():
        a=['', '', 2, 7, '', 9, 3, 8, '']
        b=[4, '', '', '', '', '', '', 2, '']
        c=['', '', '', '', '', 1, '', '', '']
        d=['', '', '', '', 8, '', '', '', '']
        e=['', '', 4, 3, '', 2, 9, '', '']
        f=['', 5, '', '', '', '', '', '', 6]
        g=[6, '', '', 8, '', 7, '', '', 9]
        h=['', '', '', '', 4, '', 8, '', '']
        k=['', '', 7, '', 1, '', '', '', '']
    #soluziones udokumalvagio2
    #[5, 1, 2, 7, 6, 9, 3, 8, 4]
    #[4, 9, 6, 5, 3, 8, 7, 2, 1] tempo risoluzione con ultimo algoritmo(list_comprehension)
                                        #52.69652986526489 secondi
    #[7, 8, 3, 4, 2, 1, 6, 9, 5]
    #[2, 7, 9, 6, 8, 5, 1, 4, 3] 38.9051148891449 tempo risoluzione con list comprehension(anche nelle funzioni)
    #[1, 6, 4, 3, 7, 2, 9, 5, 8]
    #[3, 5, 8, 1, 9, 4, 2, 7, 6]
    #[6, 2, 1, 8, 5, 7, 4, 3, 9]
    #[9, 3, 5, 2, 4, 6, 8, 1, 7]
    #[8, 4, 7, 9, 1, 3, 5, 6, 2]
    def sudokucon2soluzioni():

        a=[9, '', 6, '', 7, '', 4, '', 3]
        b=['', '', '', 4, '', '', 2, '', '']
        c=['', 7, '', '', 2, 3, '', 1, '']#non è un vero sudoku
        d=[5, '', '', '', '', '', 1, '', '']
        e=['', 4, '', 2, '', 8, '', 6, '']
        f=['', '', 3, '', '', '', '', '', 5]
        g=['', 3, '', 7, '', '', '', 5, '']
        h=['', '', 7, '', '', 5, '', '', '']
        k=[4, '', 5, '', 1, '', 7, '', 8]


    def sudokudiabolico():
        a=['', 7, '', '', '', 1, '', '', 5]#0:00:47.730255 tempo risoluzine
        b=['', 4, '', 5, 2, '', '', 6, '']
        c=['', '', 2, '', '', 3, '', '', '']
        d=['', '', '', 1, '', '', '', '', '']#tempo risoluzione 0:00:44.735793
        e=['', '', 8, 4, 5, '', '', '', 7]#38.42667198181152 tempo risoluzionecon list comrpehension 
        f=[7, '', '', '', '', '', '', 3, '']# 35 secondi con range(9) nella list comprehension di filtro2
        g=['', '', '', '', '', 2, '', '', '']
        h=['', '', 4, 7, 8, '', '', '', 3]
        k=['', 6, '', '', '', '', 9, '', '']
    #sudokudiabolico()

     #[(0, 0), (0, 2), (0, 6), (1, 2), (1, 6), (2, 2), (2, 3), (2, 5), (3, 4), (3, 8), (4, 0), (4, 4), (5, 4), (5, 7), (5, 8), (6, 1), (6, 7), (7, 2), (7, 3), (7, 5), (7, 7), (8, 1), (8, 5), (8, 7)]
    def verydifficult():
        a=[6, '', 3, '', '', '', 1, '', '']
        b=['', '', 9, '', '', '', 2, '', '']
        c=['', '', 7, 4, '', 9, '', '', '']#in realtà non e cosi difficile , risolto in 01.73064 secondi
        d=['', '', '', '', 1, '', '', '', 7]
        e=[4, '', '', '', 6, '', '', '', '']
        f=['', '', '', '', 7, '', '', 5, 3]
        g=['', 1, '', '', '', '', '', 4, '']
        h=['', '', 6, 3, '', 7, '', 9, '']
        k=['', 9, '', '', '', 2, '', 3, '']
        #risolve sudoku facili e hard in secondi e quelli più difficili in poco piu di un minuto(esperoto e difficile)
     # t
    def ciao():
        a= ['', '', '', '', 3, '', 2, '', '']#sudokufacile2
        b= [7, '', 5, 2, '', '', '', 9, ''] #tempo risoluzione 0:00:00.364029,--> 3 decimi
        c= [8, 3, '', 4, 6, 9, 1, 5, '']
        d= [2, '', '', '', 9, 4, '', 3, '']
        e= [9, 8, '', '', '', 3, '', '', 2]
        f= [6, 1, 3, 8, '', 2, '', '', 9]
        g= [4, '', '', 1, '', '', 7, '', 3]
        h= [3, 7, 8, '', 2, '', 4, '', '']
        k= ['', 6, 1, '', '', '', '', '', '']
    def l_p():
            l_p.var=""
    l_p()

    l_p.var=[[] for x in range(9)]
    #print(l_p.var)
        #Sudoku.var=[
        #[1, 9, 6, 7, 3, 5, 2, 8, 4],#per controllare la correttezza delle soluzioni, se il programma restituisce le soluzioni corrette
        #[7, 5, 5, 2, 8, 1, 3, 9, 6],
        #[8, 3, 2, 4, 6, 9, 1, 5, 7],#osoluzione_facile
        #[2, 5, 7, 6, 9, 4, 8, 3, 1],
        #####[9, 8, 4, 5, 1, 3, 6, 7, 2],
        ###[6, 1, 3, 8, 7, 2, 5, 4, 9],
        ####[4, 2, 9, 1, 5, 8, 7, 6, 3],
    ##[3, 7, 8, 9, 2, 6, 4, 1, 5],
    #[5, 6, 1, 3, 4, 7, 9, 2, 8]]


    def sudokudifficile2():
        a= [9, '', '', '', 2, 7, '', 5, '']
        b= ['', 5, '', '', '', '', 9, '', 4]
        c= ['', '', '', '', '', '', '', '', '']
        d= [8, '', '', '', 7, 5, 6, 4, 9]
        e= [1, '', '', '', 4, '', '', '', '']
        f= ['', '', '', '', '', 9, 8, '', '']
        g= ['', '', '', 4, '', '', '', '', '']
        h= ['', '', '', '', 3, '', '', 1, '']
        k= [5, '', 1, '', '', 2, '', 3, 7]


    #soluzionedifficile2
    difficile=[[9, 8, 4, 6, 2, 7, 1, 5, 3],
    [2, 5, 7, 8, 1, 3, 9, 6, 4], #tempo risoluzione  con nuovo algoritmo0:01:17.811564(1 minuto 17 secondi)
    [6, 1, 3, 5, 9, 4, 7, 8, 2 ],
    [8, 3, 2, 1, 7, 5, 6, 4, 9],                  #  altro tempo di risoluzione con nuovo algoritmo 0:01:08.030196 minuto
    [1, 9, 6, 2, 4, 8, 3, 7, 5 ],#tempo :58 secondi con list comprehension anche nella funzione filtro2
    [7, 4, 5, 3, 6, 9, 8, 2, 1],#55.9 con list comprehension in filtro2 e for x in range(9) nella list comprehension
    [3, 7, 8, 4, 5, 1, 2, 9, 6],
    [4, 2, 9, 7, 3, 6, 5, 1, 8],
    [5, 6, 1, 9, 8, 2, 4, 3, 7]]
    def quadrato1():
            quadrato1.var=""
    quadrato1()
    def    quadrato2():
            quadrato2.var=""
    quadrato2()
    def    quadrato3():
            quadrato3.var=""
    quadrato3()
    def    quadrato4():
            quadrato4.var=""
    quadrato4()
    def     quadrato5():
            quadrato5.var=""
    quadrato5()
    def    quadrato6():
            quadrato6.var=""
    quadrato6()
    def    quadrato7():
            quadrato7.var=""
    quadrato7()
    def    quadrato8():
            quadrato8.var=""
    quadrato8()
    def    quadrato9():
            quadrato9.var=""

    quadrato9()
    def controllo_ok():
        controllo_ok.var=""
    controllo_ok()
    def CHECK_colonna():
        CHECK_colonna.var=[]
    CHECK_colonna()

    def CHECK_quadrato():
         CHECK_quadrato=""
    CHECK_quadrato()
    #

    def difficoltaesperto():
        a= ['', '', 5, '', '', 8, 3, 9, '']#0:01:26.741832 tempo risoluzione con nuovo algoritmo(1 MINUTO E 26 secondi)

        b= ['', 3, '', '', '', '', '', '', '']#nuovo tempo risoluzione  0:01:06.303514 con nuovo algoritmo (1 minuto e 6 secondi)
        c= ['', '', '', 7, '', '', '', 8, '']
        d= ['', '', 4, 5, '', '', 6, '', 2]
        e= [6, 1, '', '', '', '', '', '', '']#52.14938473701477 tempo risoluzione con list comprehensions
        f= [2, '', '', '', 4, 9, '', '', '']
        g= ['', '', '', '', '', 2, 4, '', 5]
        h= ['', '', 9, '', 8, '', '', '', '']#46.18 con un nuovo algoritmo di filtro2
        k= [5, 6, '', '', '', '', '', '', '']


    ##soloquad2[0]    [8, 9, 4, 5, 1, 3, 6, 7, 2]
    #soloquad2[0] [6, 1, 3, 8, 2, 7, 5, 4, 9]
    #soloquad2[0] [2, 5, 7, 6, 4, 9, 1, 3, 8]

    listasoluzioniesperto=[[7, 4, 5, 2, 1, 8, 3, 9, 6],#esperto
    [8, 3, 2, 4, 9, 6, 1, 5, 7],#s
    [1, 9, 6, 7, 5, 3, 2, 8, 4],
    [9, 8, 4, 5, 3, 1, 6, 7, 2],
    [6, 1, 3, 8, 2, 7, 5, 4, 9],
    [2, 5, 7, 6, 4, 9, 8, 3, 1],
    [3, 7, 8, 9, 6, 2, 4, 1, 5],
    [4, 2, 9, 1, 8, 5, 7, 6, 3],#
    [5, 6, 1, 3, 7, 4, 9, 2, 8] ]
    #def hard():
    a=['', '', 4, 7, 5, '', '', 6, '']
    b=['', '', 2, '', 3, 8, 4, '', '']#
    c=[3, 6, '', '', '', '', '', '', '']#tempo risoluzione con Anaconda 1.236 secondi
    d=['', 3, 9, '', '', '', '', '', 1]#
    e=[7, '', 1, '', '', '', '', '', '']
    f=['', '', '', 4, '', 1, '', 9, 6]# 1
    g=[1, '', '', 9, '', 3, '', 8, '']#sbno 
    h=['', 2, '', '', '', '', '', '', 4]#l
    k=['', '', '', '', 8, '', '', 5, ''] 



    #soluzione sudokuhard
    #[9, 1, 4, 7, 5, 2, 8, 6, 3]tempo risoluzione0:54minuti:52.208947 algorimto annidato 9 volte
    #[5, 7, 2, 6, 3, 8, 4, 1, 9]
    #[3, 6, 8, 1, 9, 4, 2, 7, 5]
    #[6, 3, 9, 8, 2, 5, 7, 4, 1]0:00:01.734984secondo con nuovo algorimto
    #[7, 4, 1, 3, 6, 9, 5, 2, 8]
    #[2, 8, 5, 4, 7, 1, 3, 9, 6]
    #[1, 5, 7, 9, 4, 3, 6, 8, 2]
    #[8, 2, 6, 5, 1, 7, 9, 3, 4]
    #[4, 9, 3, 2, 8, 6, 1, 5, 7]#
    
    def ultimate():
        a=['', '', 9, '', '', 4, 5, '', '']# tempo risoluzione5.739772081375122 secondi
        b=['', 7, '', '', 1, '', '', '', 4]
        c=['', '', '', 8, '', 2, '', '', 1]
        d=['', 2, '', 9, '', 3, '', 1, '']
        e=['', '', 1, '', 2, '', 9, '', '']
        f=['', 9, '', 1, '', 7, '', 5, '']
        g=[6, '', '', 2, '', 9, '', '', '']
        h=[9, '', '', '', 7, '', '', 2, '']
        k=['', '', 2, 6, '', '', 8, '', '']

    def sudokufacile():
        a=["",4,1,"","",9,6,"",8]#LISTA COMBINAZIONI RIGA 7 SE FILTRATA IN BASE ALLE COMBINAZIONE DELLA RIGA 2 VIENE RIDOTTA DA CIRCA 40000 A 16687 COMBINAZIONI POSSIBILI

        b=[6,"","","","","","",3,""]

        c=["","","",2,7,"","",9,""]

        d=["",8,"","","","",1,5,""]
        e=[3,5,"","","","","","",""]
        f=["","","","",6,8,"",2,""]

        g=[7,"",8,"","",5,"","",4]
        h=["","",9,4,"","",7,"",3]
        k=["","","",1,"","",2,"",""]

    #[2, 4, 1, 3, 5, 9, 6, 7, 8]
    #[6, 9, 7, 8, 1, 4, 5, 3, 2]
    #[8, 3, 5, 2, 7, 6, 4, 9, 1]
    #[9, 8, 2, 7, 4, 3, 1, 5, 6]
    #[3, 5, 6, 9, 2, 1, 8, 4, 7]
    #[1, 7, 4, 5, 6, 8, 3, 2, 9]
    #[7, 2, 8, 6, 3, 5, 9, 1, 4]
    #[5, 1, 9, 4, 8, 2, 7, 6, 3]
    #[4, 6, 3, 1, 9, 7, 2, 8, 5]


    def colonna():
        colonna.var=""
    colonna()

    Sudoku.var=[a,b,c,d,e,f,g,h,k]
    print("Sudoku iniziale")
    for xj in Sudoku.var:
        print(xj)
    print()



    def indice_c():
                indice_c.var=2
    indice_c()        
    def indice_r():
                indice_r.var=2
    indice_r()
    def indice_quadrato():
                indice_quadrato.var=2
    indice_quadrato()  
    def get_column_square_row(): 

        colonna.var= [row[indice_c.var] for row in Sudoku.var]
       #definisce i quadrati e restituisce l'indice del quadrato
        riga.var=Sudoku.var[indice_r.var]
        findsquare()
        #print("funzone_get_column",indice_c.var,indice_quadrato.var,riga.var)
        #print(lista_quadrati.var)


       # lista_quadrati.var=[quadrato1.var,quadrato2.var,quadrato3.var,quadrato4.var,quadrato5.var,quadrato6.var,quadrato7.var,quadrato8.var,quadrato9.var]            
    def dizio():
                dizio.var={}
    dizio()   
    def riga():
        riga.var=2
    riga()
    indici_cifre_iniziali=[(x,y)  for x in range(len(Sudoku.var)) for y in range(len(Sudoku.var)) if Sudoku.var[x][y]!=""]
    #print("aaaa,,",indici_cifre_iniziali)
    def algoritmo():#non usare contaspazi come indice dizionario se no commette errore nelal creazione della lista L-F .VAR
        contaspazi=0
        conta=-1
        for indice_r.var in range(len(Sudoku.var)):
                    for indice_c.var in range(len(Sudoku.var)):#faccio scorrere una riga alla volta
                                lista_cif=[]
                                lista=[]
                                lista_pos=[] 
                                get_column_square_row()
                                conta+=1
                                if Sudoku.var[indice_r.var][indice_c.var ]=="":
                                        contaspazi+=1
                                        for cif in range(1,10):

                                           # restituisci_indice_quadrato(indice_r.var,indice_c.var)
                                            #print(lista_quadrati.var)
                                           # print("indidce£",indice_quadrato.var)
                                            if cif not in colonna.var and cif not in riga.var and cif not in lista_quadrati.var[indice_quadrato.var]:
                                                lista_cif.append(cif)
                                                #print(colonna.var)
                                                lista_pos=[indice_r.var,indice_c.var]
                                                lista=[lista_cif,lista_pos]
                                                dizio.var[str(conta)]=lista
                                           # else:
                                            #    print(indice_r.var,indice_c.var,"bug")
        print(contaspazi,"contaspazi")

    def controlla_sudoku():
       # for indice_r.var in range(len(Sudoku.var)):
        lista_colonne=[]
        for indice_c.var in range(len(Sudoku.var)):#fac
                        get_column_square_row()
                        lista_colonne.append(len(list(set(colonna.var)))==len(colonna.var))
        get_column_square_row()
        controlla_q=[]
        controlla_riga=[]

        for j in lista_quadrati.var:
            controlla_q.append(len(list(set(j)))==len(j))
                            # pass
        for j1 in Sudoku.var:
             controlla_riga.append(len(list(set(j1)))==len(j1))

        if False not in controlla_riga and False not in controlla_q and False not in lista_colonne:
                                   return "niente errori"+str(lista_colonne)+"  "+str(controlla_q)+" "+str(controlla_riga)
        else:
                                   return  "ci sono errori( colonne, quadrati,righe)"+str(lista_colonne)+"  "+str(controlla_q)+" "+str(controlla_riga)
        # if j=="":a

                             #   pass



                               # lista=[]
        print("n spazi",contaspazi)
        print("dizio.var_len",len(dizio.var))
    algoritmo()

    #print(controlla_sudoku())
    #print(dizio.var,"dizio")                 
    print("dizio.var len",len(dizio.var))






    def L_F():
        L_F.var=3
    L_F()
    def listasoluzioni_finali():
          listasoluzioni_finali.var=[[] for x in range(9)]
    listasoluzioni_finali()

    def lista_sol():
        lista_sol.var=""
    lista_sol()




    def filtro_iniziale():
        print("execute initial filtering")
        sol1,sol2,sol3,sol4,sol5,sol6,sol7,sol8,sol9=[],[],[],[],[],[],[],[],[]
        conta_sud=-1
        lista_ind1,lista_ind2,lista_ind3,lista_ind4,lista_ind5,lista_ind6,lista_ind7,lista_ind8,lista_ind9=[],[],[],[],[],[],[],[],[]

        s1,s2,s3,s4,s5,s6,s7,s8,s9=[],[],[],[],[],[],[],[],[]
        lista_lista_ind=[lista_ind1,lista_ind2,lista_ind3,lista_ind4,lista_ind5,lista_ind6,lista_ind7,lista_ind8,lista_ind9]
        lista_s=[s1,s2,s3,s4,s5,s6,s7,s8,s9]
        lista_sol.var=[sol1,sol2,sol3,sol4,sol5,sol6,sol7,sol8,sol9]
        for sud in Sudoku.var:#FILTRA IN BASE CIFRE INIZIALI IN MODO CHE RIMANGANO NELLA LORO POSIZIONE
            #print(sud)
            conta_sud=conta_sud+1


            for x1 in numeri:
                if x1 not in sud:
                    #print(x1)
                    lista_s[conta_sud].append(x1)

            for x in range(0,len(a)):
                if sud[x]=="":
                    index1=x

                    lista_lista_ind[conta_sud].append(index1)#fino a qui funziona



            for v in itertools.permutations(lista_s[conta_sud]):
                lista=["","","","","","","","",""]

                conta=-1
               # print(v)

                for x3 in sud:
                    conta=conta+1
                  #  print(conta)
                    #print(x3)


                    for j ,y in zip(lista_lista_ind[conta_sud],v):
                        if x3=="":
                            lista[j]=y
                        else:
                            lista[conta]=x3

                lista_sol.var[conta_sud].append(lista)  

        for x in lista_sol.var:
                print("sol",len(x))
        conta=-1
    filtro_iniziale()
    def filtro2():#filtra le permutazioni in base alle cifre che possono andare bene nelle celle vuote
        soluzione1,soluzione2,soluzione3,soluzione4,soluzione5,soluzione6,soluzione7,soluzione8,soluzione9=[],[],[],[],[],[],[],[],[]
     #   print(dizio.var,"fjfffffffffffff")
        l_f=[]
        vero=[]
        intero1=0
        intero2=6
        n_lista=0
        n=0
        listasoluzioni_finali.var=[soluzione1,soluzione2,soluzione3,soluzione4,soluzione5,soluzione6,soluzione7,soluzione8,soluzione9]
        l_f1,l_f2,l_f3,l_f4,l_f5,l_f6,l_f7,l_f8,l_f9=[],[],[],[],[],[],[],[],[]
        L_F.var=[l_f1,l_f2,l_f3,l_f4,l_f5,l_f6,l_f7,l_f8,l_f9]
        c=0
        def partealgoritmo6x6():
            for x in range(82):#distribuisco il dizionario sulle varie righe

                if str(x) in dizio.var:

                    if x<6:
                        L_F.var[0].append(dizio.var[str(x)])
                    elif 6<=x<=11:
                        L_F.var[1].append(dizio.var[str(x)])
                    elif 12<=x<=17:
                        L_F.var[2].append(dizio.var[str(x)])

                    elif 18<=x<=23:
                        L_F.var[3].append(dizio.var[str(x)])
                    elif 24<=x<=29:
                        L_F.var[4].append(dizio.var[str(x)])
                    elif 30<=x<=35:
                        L_F.var[5].append(dizio.var[str(x)])
                            #l_f.append(dizio.var[str(x)])

        #a=["",4,1,"","",9,6,"",8] intervallo 0 - 8


        #b=[6,"","","","","","",3,""]intervallo 9 - 17

        #c=["","","",2,7,"","",9,""]intervallo 18 - 26

        #d=["",8,"","","","",1,5,""]intervallo 27 - 35
        #e=[3,5,"","","","","","",""]intervallo36 - 44
        #f=["","","","",6,8,"",2,""]intervallo45 - 53

        #g=[7,"",8,"","",5,"","",4]intervallo54 - 62
        #h=["","",9,4,"","",7,"",3]intervallo 63 -71
        #k=["","","",1,"","",2,"",""]intervallo 72 -80
                       # if x%6==0:
        #def partealgoritmo9x9():
        for x in range(82):#distribuisco il dizionario sulle varie righe

                if str(x) in dizio.var:

                    if x<9:
                        L_F.var[0].append(dizio.var[str(x)])
                    elif 9<=x<=17:
                        L_F.var[1].append(dizio.var[str(x)])
                    elif 18<=x<=26:
                        L_F.var[2].append(dizio.var[str(x)])

                    elif 27<=x<=35:
                        L_F.var[3].append(dizio.var[str(x)])
                    elif 36<=x<=44:
                        L_F.var[4].append(dizio.var[str(x)])
                    elif 45<=x<=53:
                        L_F.var[5].append(dizio.var[str(x)])
                    elif 54<=x<=62:
                        L_F.var[6].append(dizio.var[str(x)])
                    elif 63<=x<=71:
                        L_F.var[7].append(dizio.var[str(x)])
                    elif 72<=x<=80:
                        L_F.var[8].append(dizio.var[str(x)])
                     #   L_F.append(dizio.var[str(x)])
        #print("lf1",L_F.var[1])
        #print(lista_sol[5],"sol5")
      #  print("lf")
       # for x in L_F.var:
        #    print(x)
        
        for x in L_F.var:
           # for j in x:
                print("lennn",len(x))

        #print("L_F",len(L_F.var))
        #print(L_F.var,"LF1")
        #lista_sol.var[hh],L_F.var[hh]
        def indice22():
            indice22.var=1111
        indice22()
        def get_index(j,x):
            
            
          
                    conta=0
                  

                    for j in L_F.var[indice22.var]:
                        cifre=j[0]
                        indici=j[1]
               # for j in :
                   # print(j,"j")
                   
                           # print("cifre",cifre)
                        #print("indici",indici)
                        if x[indici[1]] in cifre:
                                 #   print("ciao")
                            conta+=1
                           # print("conta444",conta)
                    if conta==len(L_F.var[indice22.var]):#se 
                       # if x not in listasoluzioni_finali.var[indice22.var]:
                            return(x)
           
        def senza_none(x):
            if x != None:
                  return True  

            return False
        #for indice22.var in range(9):
            #listasoluzioni_finali.var[indice22.var]=list(filter(senza_none,[[get_index(L_F.var[indice22.var],x) for x in lista_sol.var[indice22.var]]for indice22.var in range(9)]))
       # print("dd",listasoluzioni_finali.var[8])
      ##   primetrerighe=list(filter(senza_none,[ colonne_diverse(i,j,z) for i in listasoluzioni_finali.var[0] for j in listasoluzioni_finali.var[1] for z in   listasoluzioni_fi
        listasoluzioni_finali.var=[[get_index(L_F.var[indice22.var],x) for x in lista_sol.var[indice22.var]] for indice22.var in range(9) ]  
       # print(listasoluzioni_finali.var[6],"www")
        listasoluzioni_finali.var=[list(filter(senza_none,x) )for x in listasoluzioni_finali.var]
        #print(listasoluzioni_finali.var,"www2")
    filtro2()

     #  def ciao():
      #  for hh in range(9):
             
           #    for x, j in itertools.product(lista_sol.var[hh],L_F.var[hh]):
           # for x in :
           # print("x",x)
                  # le cifre delle permutazioni corrispondono alle cifre contenuto nella lista di cifre possibil
                           #    if x not in   listasoluzioni_finali.var[hh]:
                               #    listasoluzioni_finali.var[hh].append(x)
       # print(len("zz"),zz)  
    print("len dopo secondo filtraggio")
    for j in listasoluzioni_finali.var:
              print(len(j))
   # for j in listasoluzioni_finali.var:
           #or  y in j:
        #for  z in j:
         #   if j.count(z)>1:
          #      print("conta333",j.count(z))
        
    #filtro2()
    #print("ciao22223",listasoluzioni_finali.var)
    def find_sol(a,b):
       # if a[0]!=b[0]!=c[0] and a[1]!=b[1]!=c[0] and a[2]!=b[2]!=c[0] and a[3]!=b[3]!=c[0]:
        ciao2=[a[0],a[1],a[2],a[3],a[4],a[5],b[0],b[1],b[2]]  

        col=[]
        c_q=[]  
        q1=ciao2[0][0:3]+ciao2[1][0:3]  +ciao2[2][0:3]
        q2=ciao2[0][3:6]+ciao2[1][3:6]  +ciao2[2][3:6]
        q3=ciao2[0][6:9]+ciao2[1][6:9]   +ciao2[2][6:9]
        q4=ciao2[3][0:3]+ciao2[4][0:3]  +ciao2[5][0:3]
        q5=ciao2[3][3:6]+ciao2[4][3:6]  +ciao2[5][3:6]
        q6=ciao2[3][6:9]+ciao2[4][6:9]   +ciao2[5][6:9]
        q7=ciao2[6][0:3]+ciao2[7][0:3]  +ciao2[8][0:3]
        q8=ciao2[6][3:6]+ciao2[7][3:6]  +ciao2[8][3:6]
        q9=ciao2[6][6:9]+ciao2[7][6:9]   +ciao2[8][6:9]
        lista_quadrati=[q1,q2,q3,q4,q5,q6,q7,q8,q9]

        #colonna= [ for jz in range(9) ]
        #print("vvvvvvcc",colonna) 
        #col=[len(list(set(jz)))==len(jz) for jz in colonna ]
        #for jz in range(9):
        colonna11= [[row[jz] for row  in ciao2] for jz in range(9)]
        col=[len(list(set(jz)))==len(jz) for jz in colonna11]
            #col.append(len(list(set(colonna11)))==len(colonna11))
       # print("ccc",colonna11)
        #print("ccc2c",col)
        #for jz in lista_quadrati:
         #   colonna= [row[jz] for row in ciao]
         #   c_q.append(len(list(set(jz)))==len(jz))
        c_q=[len(list(set(jz)))==len(jz) for jz in lista_quadrati]
       # print(c_q,"CCCCC")
        #col.append(len(list(set(colonna3)))==len(colonna3))
        #col.append(len(list(set(colonna4)))==len(colonna4))
        #if list(set(colonne))==len(colonne):
         #       conta+=1
       # if a!=None or b!=None or c!=None:
        if False not in col and False not in c_q:
            return ciao2





    def risolvi_prime6(a,b):
       # if a[0]!=b[0]!=c[0] and a[1]!=b[1]!=c[0] and a[2]!=b[2]!=c[0] and a[3]!=b[3]!=c[0]:
        ciao2=[a[0],a[1],a[2],b[0],b[1],b[2]]  

        col=[]
        c_q=[]  
        q1=ciao2[0][0:3]+ciao2[1][0:3]  +ciao2[2][0:3]
        q2=ciao2[0][3:6]+ciao2[1][3:6]  +ciao2[2][3:6]
        q3=ciao2[0][6:9]+ciao2[1][6:9]   +ciao2[2][6:9]
        q4=ciao2[3][0:3]+ciao2[4][0:3]  +ciao2[5][0:3]
        q5=ciao2[3][3:6]+ciao2[4][3:6]  +ciao2[5][3:6]
        q6=ciao2[3][6:9]+ciao2[4][6:9]   +ciao2[5][6:9]
        lista_quadrati=[q1,q2,q3,q4,q5,q6]
        for jz in range(9):
            colonna11= [row[jz] for row in ciao2]
            col.append(len(list(set(colonna11)))==len(colonna11))
        for jz in lista_quadrati:
         #   colonna= [row[jz] for row in ciao]
            c_q.append(len(list(set(jz)))==len(jz))

        #col.append(len(list(set(colonna3)))==len(colonna3))
        #col.append(len(list(set(colonna4)))==len(colonna4))
        #if list(set(colonne))==len(colonne):
         #       conta+=1
       # if a!=None or b!=None or c!=None:
        if False not in col and False not in c_q:
            return ciao2


    def colonne_diverse(a,b,c):
       # if a[0]!=b[0]!=c[0] and a[1]!=b[1]!=c[0] and a[2]!=b[2]!=c[0] and a[3]!=b[3]!=c[0]:
        ciao=[a,b,c]  

       # col=[]
        #c_q=[]  
        quadrato1=ciao[0][0:3]+ciao[1][0:3]  +ciao[2][0:3]
        quadrato2=ciao[0][3:6]+ciao[1][3:6]  +ciao[2][3:6]
        quadrato3=ciao[0][6:9]+ciao[1][6:9]   +ciao[2][6:9]
        lista_quadrati=[quadrato1,quadrato2,quadrato3]

        colonna= [[row[jz] for row  in ciao] for jz in range(9) ]
        #print("vvvvvvcc",colonna) 
        col=[len(list(set(jz)))==len(jz) for jz in colonna ]
        #col.append()
        #for jz in lista_quadrati:
         #   colonna= [row[jz] for row in ciao]
         #   c_q.append(len(list(set(jz)))==len(jz))
        c_q=[len(list(set(jz)))==len(jz) for jz in lista_quadrati ]
       # print("cq",c_q)
        #print("col",col)
        #col.append(len(list(set(colonna3)))==len(colonna3))
        #col.append(len(list(set(colonna4)))==len(colonna4))
        #if list(set(colonne))==len(colonne):
         #       conta+=1
       # if a!=None or b!=None or c!=None:
        if False not in col and False not in c_q:
            return a,b,c
        #else:
         #   pass

      #  listacolonne=[]
    def senza_none(x):
        if x != None:
              return True  

        return False

    # Extract elements from the numbers list for which check_even() returns True


    primetrerighe=list(filter(senza_none,[ colonne_diverse(i,j,z) for i in listasoluzioni_finali.var[0] for j in listasoluzioni_finali.var[1] for z in   listasoluzioni_finali.var[2]]  ) )
    #lista4=[x for x in lista for y in lista1]
    #print("prime3",primetrerighe)
    #print()
    righe456=list(filter(senza_none,[ colonne_diverse(i,j,z) for i in listasoluzioni_finali.var[3] for j in listasoluzioni_finali.var[4] for z in   listasoluzioni_finali.var[5]]  ) )
    #print()
    #print(righe456)
    #print()
    righe789=list(filter(senza_none,[ colonne_diverse(i,j,z) for i in listasoluzioni_finali.var[6] for j in listasoluzioni_finali.var[7] for z in   listasoluzioni_finali.var[8]]  ) )
    #print(righe789)
    #print(even )
    #print()
    # converting to list
    #primetrerighe= list(lista4)
    primesei=list(filter(senza_none,[ risolvi_prime6(i,j) for i in primetrerighe for j in righe456]  ) )
    #print("ciao",primesei)
    soluzione=list(filter(senza_none,[ find_sol(i,j) for i in primesei for j in righe789]  ) )
    now=time.time()
    print("tempo risoluzione",now-start)
    root = tk.Tk()
    root.geometry("1000x1000")
    canvas= Canvas(root, width= 1000, height= 750, bg="SpringGreen2")   
   
    canvas.create_text(200, 20, text="sudoku iniziale", fill="black", font=('Helvetica 15 bold'))
    root.title('Sudoku Solver')
    #greeting = tk.Label(text="Sudoku Solver")
   # greeting.pack()
    x=50
    
    y=50
    #contatore=0   
    def disegna_contorno_sudoku_iniziale():
        canvas.create_line(58, 30, 338, 30,width=4.5)
        canvas.create_line(58, 300, 338, 300,width=4.5)
        canvas.create_line(60,30, 60, 300,width=4.5)
        canvas.create_line(335,30, 335, 300,width=4.5)
      
    disegna_contorno_sudoku_iniziale()    
    for jj in range(len(Sudoku.var)): #stampa il sudoku iniziale sul canvas di tk inter
              
            for pp in range(len(Sudoku.var)):
                x=x+30 
           # print(x)
               # contatore+=1
                x1=30
                x2=60
                if Sudoku.var[jj][pp]=="":
                  #  print("ccccce")
                    #canvas.create_text(x, y,text=" * ", fill="black", font=('Helvetica 15 bold'))
                    contatore=0
                    for jjjy in range(8):
                        contatore+=1
                        x2=x2+30
                        if contatore%3==0:
                            canvas.create_line(x2,30, x2, 300,width=4.5)
                        else:
                            canvas.create_line(x2,30, x2, 300)
                    contatore=0
                    for jjjy in range(8):
                        contatore+=1
                        x1=x1+30
                        if contatore%3==0:
                            canvas.create_line(60, x1, 335, x1,width=4.5)
                        else:
                            canvas.create_line(60, x1, 335, x1)
                    canvas.pack()
   
                    #w.place(x, y)
                    #w.pack()
                else:
                    canvas.create_text(x, y, text=str(Sudoku.var[jj][pp])+" ", fill="black", font=('Helvetica 15 bold'))
                    canvas.pack()
                
            y=y+30
            x=50
    
    canvas.create_text(750, 20, text="soluzione", fill="black", font=('Helvetica 15 bold'))
    x=600
    y=50
    print("s",soluzione)
   # indici_cifre_iniziali
    import random
    lista_colori=["red","blue","purple","yellow"]
    colore=random.choice(lista_colori)
    tempo_risoluzione=now-start
    minuti=tempo_risoluzione//60
    secondi=tempo_risoluzione%60
    if minuti>0:
        if minuti==1:
            tempo2=str(minuti)+" minuto e "+str(secondi)+" secondi"
        else:
            tempo2=str(minuti)+" minuti e "+str(secondi)+" secondi"
    else:
        tempo2=str(secondi)+" secondi"
   
    def disegna_contorno_soluzione():
        canvas.create_line(600,30, 887, 30,width=4.5)
        canvas.create_line(600,300, 887, 300,width=4.5)
        canvas.create_line(602,30, 602, 300,width=4.5)
        canvas.create_line(884,30, 884, 300,width=4.5)
    disegna_contorno_soluzione()
    for jj in range(len(soluzione[0])):#stampa la soluzione sul canvas di tkinter
          
            for pp in range(len(soluzione[0])):
                x=x+30 
           # print(x)
                print(soluzione[0][jj][pp])
           # print()
   
                    #w.place(x, y)
                    #w.pack()
                x1=30
                x2=610
                if (jj,pp)  in indici_cifre_iniziali:
                   #print("Aaaaaaaaa")
                    canvas.create_text(x, y, text=str(soluzione[0][jj][pp])+" ", fill=colore, font=('Helvetica 15 bold'))
                    canvas.pack() 
                    contatore=0
                    for jjjy in range(8):
                        contatore+=1
                        x2=x2+30
                     
                        if contatore%3==0:
                            canvas.create_line(x2,30, x2, 300,width=4.5)
                        else:
                            canvas.create_line(x2,30, x2, 300)
                    contatore=0
                    for jjjy in range(8):
                        contatore+=1
                        x1=x1+30
                        if contatore%3==0:
                            canvas.create_line(600, x1, 887, x1,width=4.5)
                        else:
                            canvas.create_line(600, x1, 887, x1)
                else:
                    canvas.create_text(x, y, text=str(soluzione[0][jj][pp])+" ", fill="black", font=('Helvetica 15 bold'))
                    canvas.pack() 
            y=y+30
            x=600
    canvas.create_text(500, 500, text="tempo risoluzione "+str(tempo2), fill="black", font=('Helvetica 15 bold'))
    root.mainloop()
    
    for x in soluzione[0]:
        print(x)
    print(controlla_sudoku())
    
             #   colonna= [row[jz] for row in ciao]
             #   c_q.append(len(list(set(jz)))==len(jz))
risolvi_sudoku()
        #print(primetrerighe)



