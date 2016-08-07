import random, pickle
limit=100 #the min/max == -limit/limit eg. if limit == 10: min/max == -10²/10²
Dupes=0 #to list number of dupe tests. (0 matching rows are not checked due to how long it takes)

def LoadRes():
    array=[] #Magic squares with 0 matching rows
    twoeM=[] #Magic squares with 2 matching rows
    threeeM=[] #Magic squares with 3 matching rows
    foureM=[] #Magic squares with 4 matching rows
    fiveeM=[] #Magic squares with 5 matching rows
    sixeM=[] #Magic squares with 6 matching rows
    seveneM=[] #Magic squares with 7 matching rows
    Win=[] #Magic squares with all 8rows matching

    with open("Win.txt", 'rb') as f: #loads list containging winning combinations
        Win = pickle.load(f)
    with open("Two.txt", 'rb') as f: #loads list containing two matches
        twoeM = pickle.load(f)
    with open("Three.txt", 'rb') as f: #loads list containing three matches
        threeeM = pickle.load(f)
    with open("Four.txt", 'rb') as f: #loads list containing four matches
        foureM = pickle.load(f)
    with open("Five.txt", 'rb') as f: #loads list containing five matches
        fiveeM = pickle.load(f)
    with open("Six.txt", 'rb') as f: #loads list containing six matches
        sixeM = pickle.load(f)
    with open("Seven.txt", 'rb') as f: #loads list containing seven matches
        seveneM = pickle.load(f)
    #with open("Fail.txt", 'rb') as f: #loads list containing no matches
     #   array = pickle.load(f)
    return array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win #returns all lists

def GenerateNumbers(limit): #generates list of 9 unique numbers from -limit to limit (if limit = 10, the numbers whould tange from -10² to 10²
    tmp = False #used in loop#
    N=[] #generates list
    for x in ["a","b","c","d","e","f","g","h","i"]:
        while tmp == False:
            globals()[x]=random.randint((limit*-1),limit) #generates number
            if ((globals()[x] in N)==False) and ((globals()[x]<limit)):# and (globals()[x]>=100000000000000)or(globals()[x]<=-100000000000000)) : # if not already in the list and does not exceed upper limit
                N.append(globals()[x]) #add to 'N' list
                tmp=True #break the loop
        tmp=False #close the loop, ready for next letter
    return a, b, c, d, e, f, g, h, i #returns the 9 numbers

def most_common(lst,lstt,array,twoeM,threeeM,foureM,fiveeM,sixeM,seveneM,Win):#lst = results. lstt= original numbers
    Occ=0 #counts how many times the most common result appears
    mcn = max(set(lst), key=lst.count) #most common result
    for i in lst: #how many of said most common result
        if i == mcn:
            Occ+=1
    if Occ==1: # if two matches
        array.append(lstt) #save to list
    elif Occ==2: # if two matches
        twoeM.append(lstt) #save to list
    elif Occ==3: # if three matches
        threeeM.append(lstt) #save to list
    elif Occ==4: # if four matches
        foureM.append(lstt) #save to list
    elif Occ==5: # if five matches
        fiveeM.append(lstt) #save to list
    elif Occ==6: # if six matches
        sixeM.append(lstt) #save to list
    elif Occ==7: # if seven matches
        seveneM.append(lstt) #save to list
    elif Occ==8: # if all results match
        Win.append(lstt) #save to list
    print((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win))) #prints how many tests there are
    return array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win #returns the lists

def Calculate(array,twoeM,threeeM,foureM,fiveeM,sixeM,seveneM,Win,a,b,c,d,e,f,g,h,i):
    aa=a*a #square the numbers
    bb=b*b
    cc=c*c 
    dd=d*d
    ee=e*e 
    ff=f*f 
    gg=g*g 
    hh=h*h
    ii=i*i 
    h1=aa+bb+cc #calculate the rows
    h2=dd+ee+ff 
    h3=gg+hh+ii 
    v1=aa+dd+gg
    v2=bb+ee+hh
    v3=cc+ff+ii
    d1=aa+ee+ii
    d2=gg+ee+cc
    SqNumbers=[a,b,c,d,e,f,g,h,i] #save original numbers
    awnsers=[h1,h2,h3,v1,v2,v3,d1,d2]#save results
    array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win = most_common(awnsers,SqNumbers,array,twoeM,threeeM,foureM,fiveeM,sixeM,seveneM,Win)#check most common result and save to relevent list
    return array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win #return the lists

def endingg(array,twoeM,threeeM,foureM,fiveeM,sixeM,seveneM,Win): #Runs at the end. it prints and saves the results.
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
    print(Dupes,"Where dupes")
    ################################## Saves all arrays to text files
    print("Saving Results")
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
    ################################## End of file saving
#End of end

def removedupe(L): #removes duplicate enteries
    if L:
       L.sort()
       last = L[-1]
       for i in range(len(L)-2, -1, -1):
           if last == L[i]:
               del L[i]
           else:
               last = L[i]
    return L

array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win = LoadRes() #Loads old results
Current = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win))) #calculates current number of tests
print("Dont run too many tests at once, as results are only saved at the end")
target=(int(input("There are %s current tests. How many more? " % (Current))))+Current #number of tests to be done
loops = target - Current # inacurate estimate: number of loops performed
while ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))< target: #while number of tests less than target
    a, b, c, d, e, f, g, h, i = GenerateNumbers(limit) #generate 9 unique numbers
    array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win = Calculate(array,twoeM,threeeM,foureM,fiveeM,sixeM,seveneM,Win,a,b,c,d,e,f,g,h,i) #test 9 numbers

print("before purification:",((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win))))
print("Removing squares with 0 matching rows")
array=[]
print("Removing duplicates 1/7")
twoeM = removedupe(twoeM)
print("Removing duplicates 2/7")
threeeM = removedupe(threeeM)
print("Removing duplicates 3/7")
foureM = removedupe(foureM)
print("Removing duplicates 4/7")
fiveeM = removedupe(fiveeM)
print("Removing duplicates 4/7")
sixeM = removedupe(sixeM)
print("Removing duplicates 6/7")
seveneM = removedupe(seveneM)
print("Removing duplicates 7/7")

Win = removedupe(Win)
print("Removing duplicates complete")
print("After purification:",(len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))


endingg(array,twoeM,threeeM,foureM,fiveeM,sixeM,seveneM,Win) #saves everything at the end
input("Press enter to close")
