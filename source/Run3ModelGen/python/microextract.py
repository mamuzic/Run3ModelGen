'''Module for extracting micromegas values from humanly readable output into csv file'''

import os

def microextract(infilen: str, outfilen: str) -> bool:
    '''Function for extracting micromegas values from infilen into outfilen. Returns success code'''
    
    varlist = ["deltartho","gmuon","bsgnlo","bsgnlo_SM","bsmumu","btaunu","bmunu","Rl23","Xf","Omega","Omega2"]
    correctline = False
    foundcrs = False

    file = open(infilen)
    newfile = open(outfilen, 'w')
    
    foundvars = 0
    newfile.write("Variable,MO\n")
    for line in file.readlines():
        for i in range(len(varlist)):
            try:
                line.split().index(varlist[i])
                correctline = True
                foundvars+=1
            except:
                line
        
            if correctline:
                if varlist[i]=='deltartho':
                    newfile.write('deltarho,'+str(line.split()[line.split().index(varlist[i])+1])+'\n')
                else:
                    newfile.write(varlist[i]+','+str(line.split()[line.split().index(varlist[i])+1])+'\n')
                correctline = False
        if "[pb]" in line:
            foundcrs = True
        if 'proton' in line and foundcrs:
            newfile.write('proton_SI,'+line.split()[2]+'\n')
            #print line.split()[2]
            newfile.write('proton_SD,'+line.split()[4]+'\n')
        if 'neutron' in line and foundcrs:
            newfile.write('neutron_SI,'+line.split()[2]+'\n')
            newfile.write('neutron_SD,'+line.split()[4]+'\n')
            foundcrs = False

    if foundvars == 0:
        #newfile.write("ERROR: No values have been found!")
        newfile.close()
        os.remove(newfile.name)
        
        return False
    
    else: return True
