import pickle
def removedupe(L):
    if L:
       L.sort()
       last = L[-1]
       for i in range(len(L)-2, -1, -1):
           if last == L[i]:
               del L[i]
           else:
               last = L[i]
    return L
listt=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9]]

with open("Fail.txt", 'rb') as f: #loads list containing no matches
        listt = pickle.load(f)

print(len(listt))
listt = removedupe(listt)
print(len(listt))
