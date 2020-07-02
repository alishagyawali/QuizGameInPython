Question = ["Which one is the first search engine in internet?","Number of bits used in IPV6 address","Which one is the web browser invented in 1990",
                "Which of the programming language is used to create program like applets?","What is the name of the first computer virus",
                "Why do we use firewall ?","What are the numbers of layers in OSI model ? ",".gif is an extension of",
                "Where is the headquareter of Microsoft office located in Washington ?","who is the CEO of Google ?"]
options = [['GOOGLE','ARCHIE','ALTAVISTA','WAIS'],['32 BIT','64 BIT','128 BIT','256 BIT'],['INTERNET EXPLORER','MOSAIC','MOZIALLA','NEXUS'],
            ['COBOL','C LANGUAGE','JAVA','BASIC'],['RABBIT','CREEPER VIRUS','ELK CLONER','SCA VIRUS'],['SECURITY','DATA TRANSMISSION','AUTHENTICATION','MONITORING'],['3','9','7','11'],
            ['IMAGE FILE','VIDEO FILE','AUDIO FILE','WORD FILE'],['TEXAS','NEW YORK','CALIFORNIA','WASHINGTON'],['BILL GATES','STEVE BALLMER','TIM COOK','SUNDAR PICHAI']]
Answer = ['ALTAVISTA','128 BIT','NEXUS','JAVA','CREEPER VIRUS','SECURITY','7','IMAGE FILE','WASHINGTON','SUNDAR PICHAI']
score = 0
doneQuestin = []
def enterQN():
    global choice
    global score  #making these variable global is important

    choice = int(input("Enter your question number from 1-10 :   "))
    if choice not in doneQuestin:
        print(Question[choice - 1])
        print("------------------")
        print('The options are given below:')
        print("-----------------------")
        print(options[choice - 1])
        userAnswer = input("Enter your answer :   ").upper()
        if(userAnswer == Answer[choice-1]):
            print("Your answer is correct")
            print("-----------------")
            score  = score + 1
        else:      
            print("your answer is incorrect")
            print("-----------------")
            print("The correct answer is ", Answer[choice - 1])
        doneQuestin.append(choice)
    else:
        print("Question is already done enter another question number")
        enterQN()
        print("Today! we are going to play interesting quiz game")
doneQuestion = [] 
for i in range(10):
    enterQN()
print(" Your score out of 10 is ", score)