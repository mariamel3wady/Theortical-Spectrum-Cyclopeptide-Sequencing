AA_WMap = {
'G': 57,
'A': 71,
'S': 87,
'P': 97,
'V': 99,
'T': 101,
'C': 103,
'I': 113,
'L': 113,
'N': 114,
'D': 115,
'K': 128,
'Q': 128,
'E': 129,
'M': 131,
'H': 137,
'F': 147,
'R': 156,
'Y': 163,
'W': 186, }

############################ PART ONE START ############################################

def theorticalSpectrum(Peptide):

    cycloSpectrum=[0]

    cycleVAl=AA_WMap[Peptide[0]]+AA_WMap[Peptide[len(Peptide)-1]]
    if len(Peptide) > 2:
        cycloSpectrum.append(cycleVAl)

    for i in range(len(Peptide)):

        prevVal = AA_WMap[Peptide[i]]
        cycloSpectrum.append(prevVal)

        j= i+1
        while j != len(Peptide):
            prevVal += AA_WMap[Peptide[j]]
            j += 1
            cycloSpectrum.append(prevVal)
        if len(Peptide) > 2:
            if i != 0 and i != len(Peptide)-1:
                temp=cycleVAl+AA_WMap[Peptide[i]]
                cycloSpectrum.append(temp)

    cycloSpectrum.sort()
    print(cycloSpectrum)


############################ PART ONE END ############################################










############################ PART TWO START ############################################



#def isConistent(spectrum , subpeptide):

    #temp_list = list(spectrum)

    #for i in range(len(subpeptide)):

        #temp = 0
        #j = i+1

        #if AA_WMap[subpeptide[i]] not in temp_list:
       #     return False
      #  else:
     #       temp_list.remove(AA_WMap[subpeptide[i]])

    #    if j < len(subpeptide)-1:
   #         temp += AA_WMap[subpeptide[i]]+AA_WMap[subpeptide[j]]
  #          if temp not in temp_list:
 #               return False
#            else:
#                temp_list.remove(temp)


#       while j < len(subpeptide)-1:
#            temp += AA_WMap[subpeptide[j+1]]
#            if temp not in temp_list:
#               return False
#            else:
#               temp_list.remove(temp)
#
#            j += 1

    #return True



def isConistent(spectrum , subpeptide):

    temp_list = list(spectrum)

    for i in range(len(subpeptide)):

        temp = 0
        j = i
        while j < len(subpeptide):
            temp += AA_WMap[subpeptide[j]]
            if temp not in temp_list:
                return False
            else:
                temp_list.remove(temp)
            j += 1

    return True





def Intial_list(spectrum):
    AA_list = []
    peptideLength = 0
    for i in range(len(spectrum)):
        for key,val in AA_WMap.items():
            if val == spectrum[i]:
                peptideLength += 1
                if key not in AA_list:
                    AA_list.append(key)
    return AA_list , peptideLength



def mainFunction(spectrum):

    AA_list , peptideLen = Intial_list(spectrum)
    Temp_list = AA_list
    spectrum_temp=spectrum
    for i in range(1, peptideLen):
        dummyList = []
        for k in range(len(Temp_list)):

            for j in range(len(AA_list)):
                tempString = ""
                tempString += Temp_list[k]
                tempString += AA_list[j]

                check = isConistent(spectrum,tempString)
                if check == True:
                    dummyList.append(tempString)


        Temp_list = dummyList

    print(Temp_list)




############################ PART TWO END ############################################








######################################################## MAIN START ###################################################################

print("PART ONE TEST")
peptide=input("ENTER THE AMINO ACID STRING PEPTIDE:")

theorticalSpectrum(peptide)



print("PART TWO TEST")
#s = [0,97 ,97 ,99,101,103,196,198,198,200,202,295,297,299,299,301,394,396,398,400,400,497]

s=input("ENTER THE VALUES OF SPECTRUM")

mainFunction(s)




######################################################## MAIN END ###################################################################