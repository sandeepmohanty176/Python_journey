#re arrange the word by alphabatically
w1,w2=str(input("Enter a word:")),str(input("Enter 2nd word:"))
if w1<w2:
    print(w1,w2,sep="/")
else:
    print(w2,w1,sep=",")