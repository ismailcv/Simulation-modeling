#sudoku oyunu 
#Verilen değerlere göre sudoku oyununu çözen uygulama
import numpy as np
def Mimari1 () :
    groups = []
    x = np . array ((0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8) )
    for i in range ( 9 ) :
        groups . append ( list ( x + i *9) ) # satırlar
    for i in range (9) :
        groups . append ( list ( x *9 + i ) ) # sütunlar
    x = np . array ( (0 ,1 ,2 ,9 ,10 ,11 ,18 ,19 ,20) )
    for i in (0 ,27 ,54) :
        for j in (0 ,3 ,6) :
            groups . append ( list ( x + i + j ) ) # bloklar
    return groups

# -1 o kısmın boş olduğu anlamına gelir.
def Puzzle1 () :
    mat = np . array ( (
        (  8 , -1 , -1 , -1 , -1 , 6 , 1 , -1 , 7) ,
        ( -1 , -1 , 5 , 2 , 1 , -1 , 3 , 9 , 6) ,
        ( -1 , 9 , -1 , -1 , 5 , -1 , 2 , -1 , -1) ,
        ( -1 , 7 , -1 , -1 , -1 , 2 , 4 , -1 , -1) ,
        ( -1 , 2 , 9 , 1 , -1 , 5 , -1 , -1 , 3) ,
        ( 5 , -1 , -1 , -1 , 7 , 4 , 9 , -1 , -1) ,
        ( 9 , -1 , -1 , 5 , 3 , -1 , -1 , 7 , 2) ,
        ( 6 , 1 , -1 , -1 , -1 , -1 , 5 , 4 , 9) ,
        ( 2 , -1 , -1 , -1 , 4 , -1 , -1 , 3 , -1) ) )
    dct = ConvertMat ( mat )
    return dct

def ConvertMat ( mat ) :
    dct = {}
    k = 0
    V , H = mat . shape
    for i in range ( V ) :
        for j in range ( H ) :
            if mat [i , j ] == -1:
                box = [ -1 ,[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]]
            else :
                box = [ mat [i , j ] ,[]]
            dct [ k ] = box
            k += 1
    return dct

def UnsolvedCount ( dct ) :
    answ = 0
    for k in dct . keys () :
        if dct [ k ][0] == -1:
            answ +=1
    return answ

def PrintSolution ( dct , L =9) :
    #L: sutun sayisi
    k = 0
    for i in range ( L ) :
        for j in range ( L ) :
            print ( " {0: >3} " . format ( dct [ k ][0]) , end = ' ')
            k = k+ 1
        print ( ' ')


def Rule1 ( dct , groups ) :
    for g in groups :
        aig = AnswersInGroup ( dct , g )
        RemovalInGroup ( aig , dct , g )
    ct = FindSolos ( dct )
    return ct

def AnswersInGroup ( dct , groupsi ) :
    knowns = []
    for cellid in groupsi :
        if dct [ cellid ][0] != -1:
            knowns . append ( dct [ cellid ][0] )
    return knowns

def RemovalInGroup ( aig , dct , groupsi ) :
    for cellid in groupsi :
        for j in aig :
            if j in dct [ cellid ][1]:
                dct [ cellid ][1]. remove ( j )

def FindSolos ( dct ) :
    ct = 0
    for cellid in dct . keys () :
        if dct [ cellid ][0]== -1 and len ( dct [ cellid ][1]) ==1:
            ct += 1
            dct [ cellid ][0] = dct [ cellid ][1]. pop (0)
            print ( ' rule 1 ' , cellid , dct [ cellid ][0] )
    return ct

def Rule2 ( dct , groups ) :
    soli = []
    for grp in groups :
        cands = []
        for cellid in grp :
            if dct [ cellid ][0] == -1:
                cands . extend ( dct [ cellid ][1] )
        unq = list ( set ( cands ) )
        for solveval in unq :
            if cands . count ( solveval ) == 1:
                for cellid in grp :
                    if solveval in dct [ cellid ][1]:
                        soli . append (( cellid , solveval ) )
    soli = list ( set ( soli ) )
    print ( ' Rule 2 ' , soli )
    for i , q in soli :
        dct [ i ][0] = q
        dct [ i ][1] = []

def SudokuR1R2 ( dct , groups ) :
    ok = True
    while ok :
        end1 = UnsolvedCount ( dct )
        Rule1 ( dct , groups )
        end2 = UnsolvedCount ( dct )
        if end2 == 0:
            ok = False
        if end1 == end2 :
            hits = Rule2 ( dct , groups )
            end3 = UnsolvedCount ( dct )
            if end1 == end3 :
                ok = False
    PrintSolution ( dct )

groups = Mimari1 ()
dct = Puzzle1 ()
SudokuR1R2 ( dct , groups )
