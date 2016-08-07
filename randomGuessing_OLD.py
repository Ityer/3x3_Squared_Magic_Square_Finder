import random, pickle
#found=False 
array=[] #Magic squares with 0 matching rows
twoeM=[] #Magic squares with 2 matching rows
threeeM=[] #Magic squares with 3 matching rows
foureM=[] #Magic squares with 4 matching rows
fiveeM=[] #Magic squares with 5 matching rows
sixeM=[] #Magic squares with 6 matching rows
seveneM=[] #Magic squares with 7 matching rows
Win=[] #Magic squares with all 8rows matching
limit=15 #the min/max == -limit/limit eg. if limit == 10: min/max == -10/10
loops=100 #number of tests to be done
Dupes=0 #to list number of dupe tests. (0 matching rows are not checked due to how long it takes)

################################## Loads all arrays from text files
with open("Win.txt", 'rb') as f:
    Win = pickle.load(f)
with open("Two.txt", 'rb') as f:
    twoeM = pickle.load(f)
with open("Three.txt", 'rb') as f:
    threeeM = pickle.load(f)
with open("Four.txt", 'rb') as f:
    foureM = pickle.load(f)
with open("Five.txt", 'rb') as f:
    fiveeM = pickle.load(f)
with open("Six.txt", 'rb') as f:
    sixeM = pickle.load(f)
with open("Seven.txt", 'rb') as f:
    seveneM = pickle.load(f)
################################## End of file loading
def endingg(): #Runs at the end. manually call if you cut tests early. it prints and saves the results.
    print("One (may contain duplicates):")
    print(len(array))
    print("Two:")
    print(len(twoeM))
    #print(twoeM)
    print("Three:")
    print(len(threeeM))
    #print(threeeM)
    print("Four:")
    print(len(foureM))
    #print(foureM)
    print("Five:")
    print(len(fiveeM))
    print(fiveeM)
    print("Six:")
    print(len(sixeM))
    print(sixeM)
    print("Seven:")
    print(len(seveneM))
    print(seveneM)
    print("Win:")
    print(len(Win))
    print(Win)
    print(Dupes,"/",loops, "Where dupes")
    ################################## Saves all arrays to text files
    with open("Win.txt", 'wb') as f:
        pickle.dump(Win, f)
    with open("Two.txt", 'wb') as f:
        pickle.dump(twoeM, f)
    with open("Three.txt", 'wb') as f:
        pickle.dump(threeeM, f)
    with open("Four.txt", 'wb') as f:
        pickle.dump(foureM, f)
    with open("Five.txt", 'wb') as f:
        pickle.dump(fiveeM, f)
    with open("Six.txt", 'wb') as f:
        pickle.dump(sixeM, f)
    with open("Seven.txt", 'wb') as f:
        pickle.dump(seveneM, f)
    with open("Fail.txt", 'wb') as f:
        pickle.dump(array, f)
    ################################## End of file saving
#End of end



def most_common(lst,lstt):#lst = results. lstt= original numbers
    Occ=0
    mcn = max(set(lst), key=lst.count) #most common result
    for i in lst: #how many of said most common result
        if i == mcn:
            Occ+=1
    if Occ==1: 
        array.append(lstt)
    elif Occ==2:
        twoeM.append(lstt)
    elif Occ==3:
        threeeM.append(lstt)
    elif Occ==4:
        foureM.append(lstt)
    elif Occ==5:
        fiveeM.append(lstt)
    elif Occ==6:
        sixeM.append(lstt)
    elif Occ==7:
        seveneM.append(lstt)
    elif Occ==8:
        Win.append(lstt)
    print((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
for iii in range(0,loops):#while found == False:
    tmp = False
    N=[]
    for x in ["a","b","c","d","e","f","g","h","i"]:
        while tmp == False:
            globals()[x]=random.randint((limit*-1),limit)
            if ((globals()[x] in N)==False) and ((globals()[x])<limit) :
                N.append(globals()[x])
                tmp=True
        tmp=False
    if ((([a,b,c,d,e,f,g,h,i] in twoeM)==False) and (([a,b,c,d,e,f,g,h,i] in threeeM)==False)  and (([a,b,c,d,e,f,g,h,i] in foureM)==False) and (([a,b,c,d,e,f,g,h,i] in fiveeM)==False) and (([a,b,c,d,e,f,g,h,i] in sixeM)==False) and (([a,b,c,d,e,f,g,h,i] in seveneM)==False) and (([a,b,c,d,e,f,g,h,i] in Win)==False)):
        aa=a*a
        bb=b*b
        cc=c*c 
        dd=d*d
        ee=e*e 
        ff=f*f 
        gg=g*g 
        hh=h*h
        ii=i*i 
        h1=aa+bb+cc 
        h2=dd+ee+ff 
        h3=gg+hh+ii 
        v1=aa+dd+gg
        v2=bb+ee+hh
        v3=cc+ff+ii
        d1=aa+ee+ii
        d2=gg+ee+cc
        SqNumbers=[a,b,c,d,e,f,g,h,i]
        awnsers=[h1,h2,h3,v1,v2,v3,d1,d2]
        most_common(awnsers,SqNumbers)


        
#        if (h1==h2) and (h1==h3) and (h1==v1) and (h1==v2) and (h1==v3) and (h1==d1) and (h1==d2):
#            found=True
#            with open("Win.txt", 'wb') as f:
#                pickle.dump(Win, f)
#            print("Correct awnser")
#            print(a,b,c,d,e,f,g,h,i)
#            print(h1,h2,h3,v1,v2,v3,d1,d2)
#            Win.append([[a,b,c,d,e,f,g,h,i],[h1]])
#        else:
            
    else:
        print("Dupe")
        Dupes+=1

endingg()
