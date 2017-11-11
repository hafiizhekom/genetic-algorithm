#HAFIIZHEKOM - 2015102015

import random
import sys
from collections import Counter
huruf=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
print "ALGORITMA GENETIKA"
print "HANYA KARAKTER a-z & A-Z & SPACE"

#Input yang akan dicari
target = raw_input("TARGET EXAMPLE.(DENNY): ")
print
print "SELEKSI"
print "1. ROULLETE"
print "2. TOURNAMENT [DIREKOMENDASIKAN]"

#Seleksi yang akan digunakan
selection = input("SELEKSI: ")

#Jumlah Chromosom pada Populasi Baru yang digenerate
ch = 6
generasi = 0

def selectionturnamen(chromo):
    print "SELEKSI CHROMOSOM TURNAMEN"
    tempmax = 0
    tempbaris = None
    fitness={}
    for baris in chromo:
        tempfitness = 0
        kolombuatan=0
        for kolom in target:
            if kolom == chromo[baris][kolombuatan]:
                tempfitness=tempfitness+1
            kolombuatan = kolombuatan+1
        fitness[baris] = tempfitness
        if tempmax < tempfitness:
            tempmax = tempfitness
            tempbaris = baris


    if tempmax == 0:
        newpopulasigenerate(None)
    else:
    #cetak
        for baris in chromo:
            print convertchromosomttostring(chromo[baris]), ":", fitness[baris]

        print "TERPILIH: ", convertchromosomttostring(chromo[tempbaris])
        if convertchromosomttostring(chromo[tempbaris]) == target:
            print
            print
            print "TARGET DITEMUKAN DALAM GENERASI KE ", generasi
        else:
            mutasi(chromo[tempbaris])

def selectionroulette(chromo):
    print "SELEKSI CHROMOSOM ROULLETE"
    tempmax = 0
    tempbaris = None
    fitness={}
    for baris in chromo:
        tempfitness = 0
        kolombuatan=0
        for kolom in target:
            if kolom == chromo[baris][kolombuatan]:
                tempfitness=tempfitness+1
            kolombuatan = kolombuatan+1
        fitness[baris] = tempfitness
        if tempmax < tempfitness:
            tempmax = tempfitness
            tempbaris = baris

    if tempmax == 0:
        newpopulasigenerate(None)
    else:
    #cetak
        for baris in chromo:
            print "[", baris, "] ", convertchromosomttostring(chromo[baris]), ":", fitness[baris]

        roulette=[]
        tempresultroulette =[]
        resultroulette=None
        for index in fitness:
            if fitness[index]!=0:
                for x in range(0,fitness[index]):
                    roulette.append(index);

        print "ANGGOTA ROULETTE: ", roulette
        for x in range(0, len(roulette)):
            tempresultroulette.append(random.randrange(0,len(roulette)))

        tempkeluarterbanyak = 0
        tempx = None
        for x in Counter(tempresultroulette):
            if tempkeluarterbanyak < Counter(tempresultroulette)[x]:
                tempkeluarterbanyak = Counter(tempresultroulette)[x]
                tempx = tempresultroulette[x]

        print "ACAKAN PADA ANGGOTA ROULLETE SEBANYAK ", len(roulette), " MENGHASILKAN: ", tempresultroulette
        print "TERPILIH: ", convertchromosomttostring(chromo[roulette[tempx]])
        if convertchromosomttostring(chromo[roulette[tempx]]) == target:
            print "TARGET DITEMUKAN DALAM GENERASI KE ", generasi
        else:
            mutasi(chromo[roulette[tempx]])
        
    

def mutasi(chromo):
    chromobaru = newchromosomgenerate()
    print "MUTASI"
    print convertchromosomttostring(chromo), " - ", convertchromosomttostring(chromobaru)
    for index in chromo:
        if chromo[index] != chromobaru[index]:
            if chromo[index] != target[index]:
                print "swap", chromo[index], "-", chromobaru[index]
                chromo[index]=chromobaru[index]
                
    print convertchromosomttostring(chromo)
    newpopulasigenerate(chromo)

#def checktheresult():
    
            
def convertchromosomttostring(chromo):
    chromostring = ""
    for gennumber in chromo:
        chromostring = chromostring +  chromo[gennumber]
    return chromostring

def checkhuruftarget(huruf):
    kolomcount=0
    value = False
    index = []
    for kolom in target:
        if kolom == huruf:
            value = True
            index.append(kolomcount);
        kolomcount=kolomcount+1
    return {"value":value, "index":index}
        
def newchromosomgenerate():
    chromo={}
    for kolom in range(0,len(str(target))):
        acak = random.randrange(0,len(huruf))
        chromo[kolom] = huruf[acak]
    return chromo

def newpopulasigenerate(chromo):
    global generasi
    generasi = generasi + 1
    print
    print "GENERATE KUMPULAN CHROMOSOME - GENERASI KE", generasi
    chromoslot={}
    if chromo == None:
        ranges=0
    else:
        ranges=1
        chromoslot[0]=chromo
        
    
    for baris in range(ranges,ch):
        chromo={}
        for genbaru in range(0,len(str(target))):
            angkaacak = random.randrange(0,len(huruf))
            chromo[genbaru] = huruf[angkaacak]
            
        chromoslot[baris] = chromo

    if selection == 1:
        return selectionroulette(chromoslot)
    elif selection == 2:
        return selectionturnamen(chromoslot)

chromosom = newpopulasigenerate(None)





        
    

    
