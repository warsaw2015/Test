n = int(input("Please insert your age: "))
if 5 < n < 14:
    print("Dude, you have so much time to do right things")
    x = str(input('Please insert your sex:'))
    if x == 'man' or x =='Man':
        print('You will be a famous sienciest')
    else:
        print('You will be a good mother')
elif 16 > n > 13:
    print("You comming to important age but still you are out of low")
    q = int(input('How many books you have read per year? '))
    if q > 4:
        print('Good job , but i am sure that you can read more')
    elif 5 > q > 1 :
        print('That is nice ,but You need to read more!5 books per year at least my friend')
    else:
        print('Now you know that time to change it is come')
elif 18 > n > 15:
    print("First steps are very important ,  remember about resposibility ")
    w = str(input('Do you plan to continiue studies?: '))
    if w == 'yes' or w == 'Yes':
        print('Good luck')
    else:
        print('I like this decision ,just more self-confident')
elif n == 18:
    print("Welcome to adult life , enjoint it :)")
elif 26 > n > 18:
    print("The best time of life, rock your body move your ass:))")
    m = str(input('Do you work or study?:'))
    if m == 'work' or m == 'Work':
        print('Experience much more better than theory!')
    elif m == 'study' or m =='Study':
        print('Knowledge is power, keep going! ')
    else:
        print('Sounds not good , or you are already get succeed')
elif 30 > n > 25:
    print("Welcome to young pensioners team")
    q1 = str(input('Dou you have a child or childrens?'))
    if q1 == 'yes' or q1 =='Yes':
        print('Gratulations!')
    else:
        print('Me too still enjoy life;)')
elif 38 > n > 29:
    print("Adult time just begann")
    z1 = str(input('Do you have a wife? '))
    if z1 == 'yes' or z1 =='Yes':
        print('Lazy evening together with 2 glases of wine are always welcome ')
    else:
        print('I also prefer to have a bathroom without tonnes of hair and millions shampoo on the shelf')
elif 46 > n > 38:
    print(" Time for formula : money+brain+ not lost at all health")
    c1 = str(input('Did you discover the world enough?'))
    if c1 == 'yes' or c1 =='Yes' or c1 == 'sure' or c1 =='Sure' or c1 =='yes i do' or c1 == 'Yes i do':
        print('In this case relax and chill')
    else:
        print('I think that is the best time to do that :)')
elif 56 > n > 45:
    print("Time to make a conclusion of a life")
    j1 = str(input('Are you happy of your life? '))
    if j1 == 'yes' or j1 =='Yes' or j1 =='yes i do' or j1 == 'Yes i do':
        print('Nice to hear it!')
    else:
        print('That is not true , i can not believe you')
elif 90 > n > 55:
    print('Begining of the end , rave in the grave is comming')
    print('It is just a fully joke :)')
else:
    print('You are nr 120234 who joking like that,please write a true age :)')
