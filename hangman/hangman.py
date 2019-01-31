#import sys
#sys.argv[0]

score = 0
letter = 'abcdefghijklmnopqrstuvwxyz'
category = ['Movies','Animals','Sports']
word = ''
print('Select Category by number: ')
print('1.Movies\n2.Animals\n3.Sports\n4.Exit\n')


cate = input().strip()
while cate not in '1234':
    print('please select again')
    cate = input().strip()
cate = int(cate)-1
    
while cate != 3:
    print("Your category is "+ category[cate] + '\n')
    print("Let's start!!")
    #open file and create dict
    f = open(category[cate] +'.txt')
    container = dict() #keep word and hint in file category
    index = [] #keep word that can play
    for x in f:
        w,d = x.strip().split(':')
        container[w] = d
        index.append(w)
    f.close()
    #if len(word) > 0:
     #   index.remove(word)
    #create word to play
    import random
    word = random.choice(index) #word use to play this turn
    print("Hint: " + container[word] + "\n")
    
    tries = ''
    check = set()
    remain_wrong = 5
    wrong_word = ''
    flag = False

    for s in word:
        if s.lower() in letter:
            tries+='_'
        else:
            tries+=s

    while (remain_wrong>0 and not flag):
        pos = 0
        for i in tries:
            if i not in "_":
                print(i, end ="")
            else :
                print(i, end =" ") 
        print("\t score", score , ", remaining wrong guess", remain_wrong, end="")
        if wrong_word:
            print(", wrong guessed: "+ wrong_word + "\n")
        else:
            print("\n")

        t = input().lower().strip()
        while len(t) != 1:
            print("please try again \n")
            t = input().lower().strip()

        if (t in word.lower() and t not in check and t in letter):
            while True :
                pos = word.lower().find(t,pos)
                if pos == -1:
                    break
                tries = tries[:pos]+word[pos]+tries[pos+1:]
                check.add(t)
                score+= 5
                pos +=1
        elif t in check:
            print("please try another letter \n")
        else:
            if t not in wrong_word:
                wrong_word += " "+t
                remain_wrong -= 1
            else:
                print("you already try this letter \n")
        if '_' not in tries :
            flag = True
            break

    if flag :
        print("\n" + word + "\n")
        print("your score is", score)
        print("!!------ you win ------!!\n\n\n")
    else :
        print("!!------ you lose ------!!\n\n\n")
        print("your score is", score)
        score = 0

    print("------------------------------------------------------------------------------------")
        
    print("Let's play it again")
    category = ['Movies','Animals','Sports']
    print('Select Category by number: ')
    print('1.Movies\n2.Animals\n3.Sports\n4.Exit\n')

    cate = input().strip()
    while cate not in '1234':
        print('please select again')
        cate = input().strip()
    cate = int(cate)-1
    
    if cate == 3:
        exit
exit
