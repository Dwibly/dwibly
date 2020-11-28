import time
import sys
import random
import os

                                                                       #LETTERS
LETTER_A=("*******\n*     *\n*******\n*     *\n*     *\n")
LETTER_B=("*******\n*     *\n****** \n*     *\n*******\n")    
LETTER_D=("*******\n*     *\n*     *\n*     *\n*******\n")
LETTER_E=("*******\n*      \n*****  \n*      \n*******\n")
LETTER_G=("*******\n*      \n*    **\n*     *\n*******\n")
LETTER_M=("*** ***\n*  *  *\n*  *  *\n*     *\n*     *\n")
LETTER_N=("**    *\n* *   *\n*  *  *\n*   * *\n*    **\n")
LETTER_O=("  **   \n*     *\n*     *\n*     *\n  **   \n")
LETTER_R=("*******\n*     *\n****** \n*     *\n*      *\n")
LETTER_T=("*******\n   *   \n   *   \n   *   \n   *   \n")
LETTER_U=("*     *\n*     *\n*     *\n*     *\n*******\n")
LETTER_V=("*     *\n*     *\n *   * \n  * *  \n   *   \n")
TM=("™")
   


def dot():        
    dot = ('......\n\n')       
    for char in (dot): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
 


def gameNameA() :
    time.sleep(.04)
    print("         ")
    print("__________________________________")
    print("         ")
    time.sleep(.4)
    (LETTER_A)
    print("    \n     ")
    
    for char in (LETTER_A): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)

def gameNameD() :
    time.sleep(.01)
    (LETTER_D)
    print("    \n     ")
    for char in (LETTER_D): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameV() :
    time.sleep(.01)
    (LETTER_V)
    print("   \n      ")
    for char in (LETTER_V): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameE() :
    time.sleep(.01)
    (LETTER_E)
    print("      \n   ") 
    for char in (LETTER_E): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameN() :
    time.sleep(.01)
    (LETTER_N)
    print("    \n     ")
    for char in (LETTER_N): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameT() :
    time.sleep(.01)
    (LETTER_T)
    print("     \n    ")
    for char in (LETTER_T): 
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.001)
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(.01)
        
def gameNameU() :
    time.sleep(.01)
    (LETTER_U)
    print("   \n      ")
    for char in (LETTER_U): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameR() : 
    time.sleep(.01)
    (LETTER_R)
    print("  \n       ")
    for char in (LETTER_R): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameE2() :   
    time.sleep(.01)
    
    sys.stdout.flush()
    time.sleep(0.001)
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.01)
        
def gameNameA2() :
    time.sleep(.01)
    (LETTER_A)
    print("    \n     ")
    for char in (LETTER_A): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
        
def gameNameM() :
    time.sleep(0.01)    
    (LETTER_M)
    print("    \n    ")
    for char in (LETTER_M): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)
                            
def gameNameE3() :   
    print("    \n    ")
    time.sleep(0.01)        
    (LETTER_E)
    time.sleep(.01)
    
  
    for char in (LETTER_E): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.01)
    print(TM)
    time.sleep(.5)
    print("__________________________________")          
    
    
def BIG_B() :
    time.sleep(.01)
    (LETTER_B)
    print("   \n      ")
    for char in (LETTER_B): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()    
def BIG_O() :
    time.sleep(.01)
    (LETTER_B)
    print("   \n      ")
    for char in (LETTER_O): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()  
def BIG_M() :
    time.sleep(.01)
    (LETTER_M)
    print("   \n      ")
    for char in (LETTER_M): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()    
                                        #STARTS GAME
def START_GAME():
    gameNameA()
    gameNameD()
    gameNameV()
    gameNameE()
    gameNameN()
    gameNameT()
    gameNameU()
    gameNameR()
    gameNameE2()
    space_name()
    gameNameG()
    gameNameA2()
    gameNameM()
    gameNameE3()        
    displayIntro()       
    
                                              #DEF CLR SCREEN
def clr():
    print("\n" * 100)

                                                                        # SPACE
def spc():
    print("\n"*4)
    
                                                                    #ADD INTRO
def intro() :
   time.sleep(1) 
   typ=("This is going to be the intro....\n............................\n ............................\n............................\n............................\n............................\n............................\n............................")
   for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
   time.sleep(1) 
   dot()
   time.sleep(1) 
   dot()
   chooseDoor1 ()
   
def intro_input():
    cheat = input()
    if cheat == (''): 
        typ=("BON VOYAGE!!!")
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1) 
        time.sleep(1)
        clr()
        intro()         
    elif cheat == ('2'): 
        chooseDoor2()
        door2()
        chooseDoor3()
        door3()
        chooseDoor4()
        door4()
        chooseDoor5()
        door5()
        chooseDoor6()
        door6()
        chooseDoor7()
        door7()
        clr()
    elif cheat == ('3'): 
        chooseDoor3()
        door3()
        chooseDoor4()
        door4()
        chooseDoor5()
        door5()
        chooseDoor6()
        door6()
        chooseDoor7()
        door7()
        clr()
                   
    elif cheat == ('4'): 
        chooseDoor4()
        door4()
        chooseDoor5()
        door5()
        chooseDoor6()
        door6()
        chooseDoor7()
        door7()
        clr()
        
    elif cheat == ('5'): 
        chooseDoor5()
        door5()
        chooseDoor6()
        door6()
        chooseDoor7()
        door7()
        clr()
        
    elif cheat == ('6'): 
        chooseDoor6()
        door6()
    elif cheat == ('7'): 
        chooseDoor7()
        door7()
        clr()     

                                                                 #DISPLAY INTRO
def displayIntro():
    
    print ("                       ")
    print ("                       ")
    print ("***********************")
    print ("***********************")
    print ("* WELCOME ADVENTURER! *")
    print ("***********************")
    print ("***********************")
    print ("                       ")
    time.sleep(2)
    print ("                       ")
    print ("***********************")
    print ("***** PRESS ENTER *****")
    print ("***** TO CONTINUE *****")
    print ("***********************")
    intro_input()
                                                              # GAME END SCREEN

def end():
    print ("******************************************")
    print ("******************************************")
    print ("******* -------------------------- *******")
    print ("*******       YAY!!!!!!!!!!        *******")
    print ("*******      YOU MADE IT!!!!       *******") 
    print ("******* -------------------------- *******")
    print ("******************************************")
    time.sleep(5) 
    clr()
  
                                                                       # DOOR 7 

              
def door7():
    door7 = input('')

    if door7 == "2":
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        typ=('KILL DARK WIZARD......\n\n......\n\n......\n\n')
        
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        time.sleep(3)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("*** 1:                              ******")
        print ("*** 2:                                 ***") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
    if input('') == ('1'):
        time.sleep(1) 
        dot()
        time.sleep(1)
        dot()
        typ=('......\n\n......\n\n')
        
    
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        
        time.sleep(1)                                           
    if input('') == ('2'):
            time.sleep(1) 
            dot()
            time.sleep(1)    
            dot()
            time.sleep(1) 
            typ=('......\n\n......\n\n......\n\n......\n\n......\n\n......\n\n')          
     
        
           
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

           
            time.sleep(3)
            spc()
            print ("******************************************")
            print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
            print ("*** ------------------------------- ******")
            print ("*** 1:                              ******")
            print ("*** 2:                                 ***") 
            print ("*** ------------------------------- ******")
            print ("******************************************")
        
#ADD IF        
        
    if input('') == ('1'):
            time.sleep(1) 
            dot()
            time.sleep(1)
            dot()
            time.sleep(1)
    
            
            typ=('......\n\n......\n\n')
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)         
            
            
            time.sleep(1)                                           
    if input('') == ('2'):
            time.sleep(1) 
            dot()
            time.sleep(1)         
            dot()
            time.sleep(1)  

            typ=('......\n\n......\n\n')
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

        
            time.sleep(1)
            dot()
            time.sleep(1)
            dot()
            spc()
            spc()
            end()
            time.sleep(3)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               intro()
            else: ded == sys.exit()  
    else: 
        time.sleep(1)
        dot() 
        time.sleep(1)
        dot()
        time.sleep(1)
        typ=('YOU DECIDE TO STEAL THE SPELL BOOK TO CAST AN ATTACK SPELL\n\nWHILE THE DARK WIZARD IS BUSY MIXING HIS POTION...\n\nUSE SPELL BOOK...\n\nA: ...\n\nB: ...\n\n')
        
        
       
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        time.sleep(3)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***      1:  CAST A FIRE ATTACK     ******")
        print ("***      2:  CAST AN ICE ATTACK     ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
    

    if input('') == ('1'):
            time.sleep(1) 
            dot()
            time.sleep(1)
            dot()
            time.sleep(1)
                        
            typ=("......\n\n......\n\n......\n\n......\n\n")
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            
            
            time.sleep(1)                                           
    else:
        time.sleep(1) 
        dot()
        time.sleep(1)    
        dot()
        time.sleep(1) 
        dot()
        time.sleep(1)    
      
        
        typ=('YOU HAVE DIED...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        
        time.sleep(1)
        ded = input('PLAY AGAIN: Y/N? \n\n')           
        if ded == ('1'):
            chooseDoor5 () 
            door5()
        else: ded == sys.exit()  
def chooseDoor7():
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(1)
    typ=('YOU CONTINUE TO CLIMB UP THE MOUNTAIN...\n\nYOU CAN FINALLY SEE THE SUMMIT...\n\nYOU SEE A DARK CASTLE IN THE DISTANCE...\n\nIT IS ON THE VERY TOP OF THE MOUNTAIN...\n\nYOU DECIDE TO EXPLORE THE CASTLE...\n\nYOU ENTER THE CASTLE...\n\nYOU NOTICE THERE IS DEFINITELY SOMEONE THERE...\n\nYOU QUIETLY MOVE THROUGH THE CASTLE...\n\nYOU FIND A FEW SMALL PIECES OF TREASURE...\n\nYOU KEEP SEARCHING...\n\nTHERE IS A STARECASE...\n\nYOU GO UPSTAIRS...\n\nYOU CONTINUE TO SEARCH THE CASTLE...\n\nTHERE IS ANOTHER STARECASE...\n\nTHIS ONE IS SPIRAL AND LEADING TO A TURRET...\n\nYOU QUIETLY CLIMB THE STAIRS...\n\nAS YOU GET TO THE TOP YOU SEE A WIZARD...\n\nHE IS FACING AWAY FROM YOU...\n\nAND APPEARS TO BE BUSY MIXING POTIONS...\n\n')

    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    
    time.sleep(1)
    spc()
    print ("************************************************")
    print ("*********  WHAT WOULD YOU LIKE TO DO?  *********")
    print ("*** ---------------------------------------- ***")
    print ("*** 1: STEAL THE SPELL BOOK TO CAST A SPELL  ***")
    print ("*** 2:                                       ***") 
    print ("*** ---------------------------------------- ***")
    print ("************************************************")


                                                                       # Door 6 
def door6():
    door6 = input('')

    if door6 == '1':     
        time.sleep(1)
        dot() 
        time.sleep(1)
        dot()
        time.sleep(1)
        typ('YOU DECIDE TO GÏVES IT A SCHNÄCK\n\n')
        
        
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        
        time.sleep(1)
        typ=('......\n\n......\n\n......\n\n......\n\n')
        
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***    1: GIVES IT A SANDWICH       ******")
        print ("***    2: GIVES IT AN APPLE         ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        if input('') == ('1'):
            time.sleep(1) 
            typ=('YOU DECIDE TO GIVES THE GECKO PART OF YOUR SANDWICH...\n\n......\n\n......\n\n......\n\n......\n\nYOU PULL OUT HALF OF A SANDWICH...\n\nTHE GECKO PERKS UP...\n\nIT LOOKS AT YOU WITH HUNGRY EYES...\n\nYOU GIVE IT A SMALL PIECE...\n\nIT LOVES IT!!!...\n\nYOU PUT THE REST DOWN ON THE FLOOR...\n\nIT EATS THE REST AND SCURRIES OFF INTO DARKNESS...\n\nYOU DECIDE TO GET SOME SLEEP...\n\nTHE LATE MORNING SUNLIGHT WAKES YOU UP...\n\nYOU FIND THREE PIECES OF GOLD NEXT TO YOU...\n\nYOU LOOK AROUND TO MAKE SURE THERE IS NO MORE TREASURE...\n\nTHEN CONTINUE UP THE MOUNTAIN...\n\n') 
    
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            time.sleep(1)
            spc()
            chooseDoor7()
            door7()
        else:
            time.sleep(1) 
            typ=('YOU DECIDE TO GIVES THE GECKO AN APPLE ...\n\n......\n\n......\n\nTHE GECKO PERKS UP...\n\nIT LOOKS AT YOU WITH HUNGRY EYES...\n\nYOU GIVE IT A SMALL PIECE...\n\nIT LOVES IT!!!...\n\nYOU PUT THE REST DOWN ON THE FLOOR...\n\nIT EATS THE REST AND SCURRIES OFF INTO DARKNESS...\n\nYOU DECIDE TO GET SOME SLEEP...\n\nTHE LATE MORNING SUNLIGHT WAKES YOU UP...\n\nYOU FIND THREE PIECES OF GOLD NEXT TO YOU...\n\nYOU LOOK AROUND TO MAKE SURE THERE IS NO MORE TREASURE...\n\nTHEN CONTINUE UP THE MOUNTAIN...\n\n')   

            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)                      
            
            time.sleep(1)
            spc()
            chooseDoor7()
            door7()

    if door6 == '2':   
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
    

    typ=('YOU DECIDE TO BOOP IT’S NOSE\n\nAND START TO PICK IT UP...\n\nA SPHERE OF LIGHT ERUPTS FROM THE GECKO...\n\nTHE FORCE OF THE LIGHT SENDS YOU FLYING ACROSS THE CAVE...\n\nYOU LOOK BACK UP FROM THE FLOOR...\n\nTHERE IS NOW A FULLY GROWN DRAGON STANDING THERE...\n\n......\n\n......')
       

    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***       1: FIGHT                  ******")
        print ("***       2: RUN                    ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************") 
        if input('') == ('1'):
            time.sleep(1) 
            typ=('YOU DECIDE TO FIGHT THE DRAGON...\n\n......\n\n......\n\nYOU PULL OUT YOUR SWORD...\n\nYOU LOOK AT THE DRAGON WITH NO FEAR...\n\nYOU CAN SEE DEEP INTO THE DRAGONS EYES ...\n\nAS SOON AS YOU DO YOU KNOW YOU HAVE MADE A MISTAKE IN ATTACKING...\n\nTHE DRAGON BREATHES A LARGE PLUME OF FIRE AT YOU...\n\nTHERE IS NO CHANCE OF ESCAPING...\n\nYOU CAN SMELL YOUR FLESH BURNING ON TOP OF BURNT HAIR...\n\nODDLY YOU ARE NOT IN PAIN...\n\nYOU START TO LAUGH BECAUSE YOU CAN SEE YOUR FOREARM BONE THROUGH THE FIRE...\n\nYOU HAVE DIED...\n\n')            
            
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

            
            
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               chooseDoor6 () 
               door6()
            else: ded == sys.exit()  
        else:
            time.sleep(1) 
            typ=('YOU DECIDE TO RUN AWAY FROM THE DRAGON...\n\n......\n\n......\n\nYOU SPRINT FAST...\n\nBUT NOT FAST ENOUGH TO ESCAPE THE DRAGONS FIRE...\n\nYOU LOOK BEHIND TO SEE IF YOU HAVE A CHANCE OF ESCAPE...\n\nYOU SEE A PLUME OF FIRE COMING AT YOU AT AN INCREDIBLE SPEED...\n\n......\n\nYOU TRIP AND FALL ...\n\n......\n\nTHE PLUME OF FIRE GOES OVER YOUR HEAD ...\n\nYOU MIGHT ACTUALLY BE ABLE TO SURVIVE THIS...\n\nYOU SCRAMBLE TO GET UP ...\n\nAS YOU DO YOU LOOK BACK ONCE MORE ...\n\n......\n\nYOU FIND THE DRAGON IS MUCH FASTER THAN IT APPEARS...\n\nAND IS NOW STANDING DIRECTLY IN FRONT OF YOU...\n\nWITH ONE QUICK BITE, THE DRAGON REMOVES YOUR HEAD\n\nAND PART OF YOUR TORSO...\n\nIT WALKS AWAY AND LEAVES YOUR REMAINS TO ROT...\n\nYOU HAVE DIED...\n\n')

            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               chooseDoor6 () 
               door6()
            else: ded == sys.exit()  
            
def chooseDoor6():
    
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(1)
    typ=('YOU EXIT THE GRAVEYARD YOU FEEL A SENSE OF RELIEF...\n\nYOU HAVE A GOOD FEELING ABOUT THE REST OF THIS JOURNEY...\n\nYOU WALK FOR THE NEXT DAY WITHOUT EVENT...\n\n......\n\nTHE MARSHLAND CHANGES INTO FOOTHILLS...\n\nYOU CAN FEEL THE GROUND CHANGING UNDER YOUR FOOT...\n\nEACH STEP TAKES MORE WORK THAN THE LAST...\n\nAS YOU APPROACH THE GRUEMEAN MOUNTAIN RANGE...\n\nYOU START TO LOOK FOR A DIRECT PATH UP THE MOUNTAIN...\n\nYOU BEGAN YOUR ASCENT...\n\n......\n\n......\n\nAFTER A LONG DAY OF CLIMBING YOU STUMBLE UPON A CAVE...\n\nTHIS LOOKS LIKE THE PERFECT PLACE TO SLEEP FOR THE NIGHT...\n\nYOU ENTER THE CAVE...\n\nYOU NOTICE A SMALL CREATURE ON THE FLOOR...\n\n......\n\nIT IS A BABY GECKO...\n\nIT HAS THE MOST ADORABLE EYES YOU HAVE EVER SEEN...\n\nYOU DECIDE THAT YOU NEED TO TAKE IT WITH YOU...\n\nYOU ASK IT IF IT WANTS TO BE YOUR ADVENTURE BUDDY...\n\n')

    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
   
    time.sleep(1)
    spc()
    print ("******************************************")
    print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
    print ("*** ------------------------------- ******")
    print ("***      1: GÏVES IT A SCHNÄCK      ******")
    print ("***      2: BOOP IT’S NOSE          ******") 
    print ("*** ------------------------------- ******")
    print ("******************************************")


                                                                       # Door 5 
    
def door5():
    door5 = input('')

    if door5 == '1':
        time.sleep(1)
        typ=('1......\n\n......\n\n......\n\n......\n\n')
        

        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("*** 1:  DIE                         ******")
        print ("*** 2:  2...                           ***") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        if input('') == ('1'):
            time.sleep(1) 
            typ=('1......\n\n......\n\n......\n\ndie......\n\n')
            
            
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

            
            
            time.sleep(1)     
            print('YOU HAVE DIED...\n\n')
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               chooseDoor5 () 
               door5()
            else: ded == sys.exit()                         
        else:
            time.sleep(1) 
            typ=('2......\n\n......\n\n......\n\n......\n\n......\n\n')
            
            
            
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            time.sleep(1)
            
            spc()
            chooseDoor6()
            door6()
       
    if door5 == '2':
        time.sleep(1)
        typ=('2......\n\n......\n\n......\n\n......\n\n......\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        time.sleep(1)       
        
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("*** 1:      DIE                     ******")
        print ("*** 2:      DIE                     ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        time.sleep(1)                        
        if input('') == ('1'):
            time.sleep(1) 
            print('1...\n\n')
            time.sleep(1)    
            dot()
            time.sleep(1) 
            dot()
            time.sleep(1)    
            dot()
            time.sleep(1) 
            dot()
            time.sleep(1)
            print('YOU HAVE DIED...\n\n')
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               chooseDoor5 () 
               door5()
            else: ded == sys.exit()  
        else:    
            typ=('2...\n\n')
            
            
            
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

            
            
            time.sleep(1)             
            dot()
            time.sleep(1)      
            dot()
            time.sleep(1)
            dot()
            time.sleep(1)
            dot()
            time.sleep(1)
            print('YOU HAVE DIED...\n\n')
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               chooseDoor5 () 
               door5()
            else: ded == sys.exit()                 
def chooseDoor5():

    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(1)  
    dot()
    time.sleep(1)
    typ=('......Necromancer\n\n') 
    
    
    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    
    
    
    
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(3)
    spc()
    print ("******************************************")
    print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
    print ("*** ------------------------------- ******")
    print ("*** 1: THROW A BANANA PEEL          ******")
    print ("*** 2: ATTEMPT TELEKINESIS          ******") 
    print ("*** ------------------------------- ******")
    print ("******************************************")


                                                                        #DOOR 4

def door4():
    door4 = input('')

    if door4 == "2":
        time.sleep(1)
        typ=('YOU DECIDE TO OPEN THE BOX...\n\n......\n\n......\n\nYOU FIND THE BOX CONTAINS TWO VIALS...\n\nTHERE IS NO TIME TO KNOW EXACTLY WHAT THEY DO...\n\n')
       
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        
        
        time.sleep(1)
        spc()
        print ("***************************************************")
        print ("***      WHAT WOULD YOU LIKE TO DO?             ***")
        print ("*** ------------------------------------------- ***")
        print ("*** 1: THROW THE VIALS AT THE SAME TIME         ***")
        print ("*** 2: COMBINE THE VIALS AND THROW THE MIXTURE  ***") 
        print ("*** ------------------------------------------- ***")
        print ("***************************************************")
        if input('') == ('1'):
            time.sleep(1) 
            typ=('THROW THE VIALS AT THE SAME TIME ...\n\n......\n\n......\n\n......\n\nTHE VIALS HIT THE SKELETON...\n\nTHEY APPEAR TO HAVE NO EFFECT...\n\nYOU HEAR A CRACKLE...\n\n......\n\n......\n\nTHEN A BUBBLE...\n\n')
            
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            
            
            
            time.sleep(1)
            dot()
            time.sleep(1)
            print(LETTER_B) 
            print(LETTER_O)
            print(LETTER_O)
            print(LETTER_M)
            
            
         
            
            time.sleep(1)
            typ=('THE SUBSTANCE COMBINED TO CREATE A VERY EFFECTIVE EXPLOSIVE...\n\n')
            
            
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            
            
            time.sleep(1)
            dot()
            spc()
            chooseDoor5()
            door5()                                           
        else:
            time.sleep(1) 
            typ=('COMBINE THE VIALS AND THROW THE MIXTURE...\n\n......\n\n......\n\n......\n\n')
            
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            time.sleep(1)    
            dot()
            time.sleep(1)             
            dot()
            time.sleep(1)  
            dot()
            time.sleep(1)
            print(LETTER_B) 
            print(LETTER_O)
            print(LETTER_O)
            print(LETTER_M)
            print("YOU HAVE DIED")
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n\n')           
            if ded == ('1'):
               chooseDoor4 () 
               door4()
            else: ded == sys.exit()                 
            
    if door4 == '1':
        time.sleep(1)
        dot() 
        time.sleep(1)
        dot()
        time.sleep(1)
        typ=('YOU CHOOSE TO ATTACK USING THE SWORD...\n\n......\n\n......\n\n') 
        
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        
        
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***   1: DIRECT ATTACK...           ******")
        print ("***   2: THROW YOUR SWORD AT IT!!!  ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")    
        if input('') == ('1'):
                typ=('YOU CHOSE A DIRECT ATTACK...\n\nYOU RUN DIRECTLY AT THE SKELETON...\n\nYOU LIFT YOUR BLADE HIGH...\n\nYOU ATTACK THE SKELETON WITH YOUR SWORD...\n\nIT BLOCKS YOU WITH LITTLE EFFORT...\n\nIT IS STILL COMING FORWARD TOWARDS YOU...\n\nYOU STRIKE AGAIN...\n\nYOU KNOCK OFF AN ARM...\n\nIT IS STILL COMING TOWARDS YOU...\n\nYOU STRIKE AGAIN...\n\nYOU DECAPITATE IT...\n\nIT IS STILL COMING TOWARDS YOU...\n\nYOU ATTEMPT TO STRIKE AGAIN...\n\nTHE SKELETON BLOCKS YOU...\n\nIT FOLLOWS ITS BLOCK WITH A STRIKE...\n\nIT HITS YOU ACROSS YOUR CHEST...\n\nIT IS NOT FATAL...\n\nBUT WITHOUT IMMEDIATE ATTENTION IT WILL SO BE...\n\n            YOU STAND IN SHOCK AS THE SKELETON STRIKES AGAIN...\n\nYOUR HEAD IS TAKEN OFF IN ONE SMOOTH MOTION...\n\nTHE BLADE IS TO DULL TO COMPLETE THE CUT...\n\nYOU ARE LEFT WITH SEVERAL INCHES OF SKIN HOLDING YOUR HEAD...\n\n......\n\n......\n\nYOU HAVE DIED...\n\n')
                
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n')           
            if ded == ('1'):
                chooseDoor4 () 
                door4()
            else: ded == sys.exit()                 
        else:
            typ=('DO SOMETHING ELSE...\n\n......\n\n')
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)           
                time.sleep(1)

def chooseDoor4():
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    typ= ('YOU CONTINUE THROUGH THE FOREST...\n\nYOU NOTICE THE TREES THINNING OUT...\n\nTHE SKY SOON BECOMES VISIBLE AGAIN...\n\nYOU KEEP WALKING TOWARDS THE GRUEMEAN MOUNTAIN RANGE...\n\nTHEY ARE STILL HOPELESSLY FAR AWAY...\n\n......\n\nDAYS PASS...\n\nTHE LANDSCAPE CHANGES MANY TIMES...\n\n......\n\n......\n\nFOR A WEEK YOU WERE STUCK IN THE WASTE...\n\n......\n\nYOU WERE CERTAIN YOU WERE GOING TO DIE...\n\nYOU STUMBLE OF OF THE DESERT A SHELL OF YOURSELF...\n\n AFTER SEVERAL DAYS THE LAND CHANGES TO MARSHLAND...\n\nYOU TRUDGE THROUGH THIS VILE LAND FOR THE NEXT 3 DAYS...\n\nON THE EDGE OF THE MARSH THERE IS AN OLD GRAVEYARD...\n\nTHIS PLACE HAS BEEN ABANDONED FOR YEARS...\n\nYOU DECIDE TO SEARCH FOR ANY VALUABLES LEFT BEHIND...\n\nYOU FIND A BOX AND AN OLD SWORD...\n\nYOU DECIDE IT IS TIME TO VENTURE ONWARDS...\n\n   YOU HEAR A RUSTLE IN THE BUSH NEAR YOU...\n\n YOU START TO WALK OVER...\n\nA SKELETON WARRIOR EMERGES...\n\nHE DOES NOT MOVE VERY FAST...\n\n......\n\nBUT HE IS COMING FOR YOU WITH HIS SWORD DRAWN...\n\n')    
    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)   
    time.sleep(1)
    dot()
    time.sleep(1)
    spc()
    print ("******************************************")
    print ("***    WHAT WOULD YOU LIKE TO DO?   ******")
    print ("*** ------------------------------- ******")
    print ("***   1: ATTACK IT WITH THE SWORD   ******")
    print ("***   2: BLOW UP                    ******") 
    print ("*** ------------------------------- ******")
    print ("******************************************")


                                                                        #DOOR 3                                                   
def door3():
    door3 = input('')

    if door3 == '2':
        time.sleep(1)
        typ=('YOU DECIDE TO THROW AN OBJECT AT HER...\n\n......\n\n......\n\nYOU THINK ABOUT WHAT YOU CAN THROW...\n\n......\n\nYOU CHECK YOUR POCKET AND FIND A SMALL COIN...\n\n......\n\nYOU LOOK OVER AND SEE A ROCK YOU CAN THROW...\n\n')     
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***     1: THROW ROCK               ******")
        print ("***     2: THROW COIN               ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        if door3  == ('1'):
            time.sleep(1) 
            typ=('YOU DECIDE TO THROW A ROCK AT HER...\n\n......\n\n......\n\nDIRECT HIT...\n\nIT SEEMS TO HAVE NO EFFECT...\n\n......\n\nSHE GIGGLES AT YOU...\n\n......\n\nIT FEELS LIKE SHE IS PLAYING A GAME...\n\n......\n\nYOU DECIDE TO TALK TO HER...\n\nYOU APPROACH HER...\n\nYOU NOTICE HOW STUNNINGLY BEAUTIFUL SHE IS...\n\nYOU HAVE NEVER SEEN ANYONE SO AMAZING BEFORE...\n\nYOU START TO WADE ANKLE DEEP INTO THE WATER...\n\nSHE LOOKS UP AT YOU...\n\nSHE IS LOOKING DEEP INTO YOUR SOUL...\n\nYOU WOULD GIVE ANYTHING JUST TO TALK TO HER...')    
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            spc()
            print ("***********************************************")
            print ("***      WHAT WOULD YOU LIKE TO DO?         ***")
            print ("*** --------------------------------------- ***")
            print ("***  1: ASK HER FOR PERMISSION ACROSS       ***")
            print ("***  2: ASK HER FOR PERMISSION TO KISS HER  ***") 
            print ("*** --------------------------------------- ***")
            print ("***********************************************")    
            input ('')
        typ=('YOU CALL OUT TO HER...\n\nSHE DOES NOT SEEM TO HEAR YOU...\n\nYOU START TO WALK CLOSER TO HER...\n\nYOU STUMBLE AND START TO SWIM ...\n\nYOU CALL OUT TO HER AGAIN...\n\nSHE EXTENDS HER HAND TO MOTION YOU OVER...\n\nYOU START TO SWIM FASTER...\n\nAS YOU GET CLOSE YOU FEEL SOMETHING...\n\nSOMETHING IS ON YOUR LEG...\n\nYOU FEEL A FORCE PULL YOU UNDER WATER...\n\nYOUR LUNGS FILL WITH WATER...\n\nYOU HAVE DIED... \n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)           
            time.sleep(1)
            ded = input('PLAY AGAIN: Y/N? \n')           
            if ded == ('1'):
               chooseDoor3 () 
               door3()
            else: ded == sys.exit()                 
    if door3 == '2':
        time.sleep(1) 
        typ=('YOU DECIDE TO THROW A COIN AT HER...\n\n......\n\n......\n\nSHE SCREAMS AND HISSES...\n\nYOU HAVE NEVER HEARD ANYTHING SO LOUD BEFORE...\n\nAS SHE MELTS AWAY SHE CURSES YOU...\n\nLUCKILY FOR YOU THE CURSE OF A DEAD NYMPH IS USELESS...')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        spc()
        chooseDoor4()
        door4()  

    if door3 == ('1'):
        time.sleep(1)
        dot() 
        time.sleep(1)
        dot()
        time.sleep(1)
        typ=('YOU DECIDE TO TALK TO HER...\n\nYOU APPROACH HER...\n\nYOU NOTICE HOW STUNNINGLY BEAUTIFUL SHE IS...\n\nYOU HAVE NEVER SEEN ANYONE SO AMAZING BEFORE...\n\nYOU START TO WADE ANKLE DEEP INTO THE WATER...\n\nSHE LOOKS UP AT YOU...\n\nSHE IS LOOKING DEEP INTO YOUR SOUL...\n\nYOU WOULD GIVE ANYTHING JUST TO TALK TO HER...')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        spc()
        print ("***********************************************")
        print ("***      WHAT WOULD YOU LIKE TO DO?         ***")
        print ("*** --------------------------------------- ***")
        print ("***  1: ASK HER FOR PERMISSION ACROSS       ***")
        print ("***  2: ASK HER FOR PERMISSION TO KISS HER  ***") 
        print ("*** --------------------------------------- ***")
        print ("***********************************************")    
        input ('')
        time.sleep(1)
        typ=('YOU CALL OUT TO HER...\n\nSHE DOES NOT SEEM TO HEAR YOU...\n\nYOU START TO WALK CLOSER TO HER...\n\nYOU STUMBLE AND START TO SWIM ...\n\nYOU CALL OUT TO HER AGAIN...\n\nSHE EXTENDS HER HAND TO MOTION YOU OVER...\n\nYOU START TO SWIM FASTER...\n\nAS YOU GET CLOSE YOU FEEL SOMETHING...\n\nSOMETHING IS ON YOUR LEG...\n\nYOU FEEL A FORCE PULL YOU UNDER WATER...\n\nYOUR LUNGS FILL WITH WATER...\n\nYOU HAVE DIED... \n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        ded = input('PLAY AGAIN: Y/N? \n')
        if ded == ('1'):
           chooseDoor3 () 
           door3()
        else: ded == sys.exit()    

def chooseDoor3 ():    
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(1)
    typ=('YOU CONTINUE YOUR ADVENTURE THROUGH THE FOREST...\n\nYOU HEAR THE SOUND OF A RIVER...\n\nAS YOU APPROACH YOU CAN HEAR THE SOUND OF LAUGHTER...\n\nYOU APPROACH CAREFULLY...\n\nYOU SEE A BEAUTIFUL WOMAN ON A ROCK IN THE MIDDLE OF THE RIVER...\n\nTHERE IS A SMALL BOAT DOCKED NEAR YOU...\n\nSHE WILL SEE YOU IF YOU TRY TO TAKE THE BOAT...\n\nYOU LOOK AT HER...\n\nYOU NEED TO TALK TO HER...\n\nSHE IS NOT THAT FAR AWAY...\n\n......\n\n......\n\n')    
    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    spc()
    print ("******************************************")
    print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
    print ("*** ------------------------------- ******")
    print ("***      1: TALK TO HER             ******")
    print ("***      2: THROW OBJECT AT HER     ******") 
    print ("*** ------------------------------- ******")
    print ("******************************************")


                                                                        #DOOR 2
                     
def door2():
    door2 = input('')

    if door2 == '1':
        time.sleep(1)
        typ=('YOU DECIDE TO ASK THE DARK ELF A QUESTION...\n\n......\n\n......\n\nIN A HURRY ALL YOU CAN THINK OF TO ASK IS...')   
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        
        spc()
        print ("********************************************")
        print ("***    WHAT WOULD YOU LIKE TO ASK?       ***")
        print ("*** ------------------------------------ ***")
        print ('***  1: HOW WAS YOUR DAY?                ***')
        print ('***  2: CAN I PASS THROUGH THIS FOREST?  ***') 
        print ("*** ------------------------------------ ***")
        print ("********************************************")
        if input('') == '1':
           time.sleep(1)
           typ=('YOU ASK THE DARK ELF "HOW WAS YOUR DAY?"...\n\n')           
           
        for char in (typ): 
           sys.stdout.write(char)
           sys.stdout.flush()
           time.sleep(0.1)
           time.sleep(1)
           spc()
           print ("********************************************")
           print ("***    WHAT WOULD YOU LIKE TO ASK?       ***")
           print ("*** ------------------------------------ ***")
           print ('***  1: WHO ARE THE CYDELS?              ***')
           print ('***  2: ARROGANT                         ***') 
           print ("*** ------------------------------------ ***")
           print ("********************************************")
           if input('') == '1':
               time.sleep(1)
               typ=('WHO ARE THE CYDELS?\n\n')
                           
               for char in (typ): 
                   sys.stdout.write(char)
                   sys.stdout.flush()
                   time.sleep(0.1)

               
               time.sleep(1)
               dot()
               time.sleep(1)
               dot()
               time.sleep(1)        
               dot() 
               time.sleep(1)
               spc()
               chooseDoor3()
               door3()            
           else:
               time.sleep(1)
               typ=('ARROGANT...\n\n')
               
               
               for char in (typ): 
                   sys.stdout.write(char)
                   sys.stdout.flush()
                   time.sleep(0.1)

               
               time.sleep(1)        
               dot() 
               time.sleep(1)
               print('YOU HAVE DIED...\n\n')
               ded = input('PLAY AGAIN: Y/N? \n\n')
               if ded == ('1'):
                   clr()
                   chooseDoor2 () 
                   door2()
               else: ded == sys.exit()    

        else:     
            time.sleep(1)  
            typ=('YOU ASK THE DARK ELF "IS IT POSSIBLE TO PASS THROUGH THIS FOREST?"...\n\nHE REPLIES CALMLY...\n\n"HUMANS ARE PERMINTTED"...\n\n"ALTHOUGH THAT US ONLY BECAUSE THE CYDELS"...') 
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)          
            time.sleep(1)
            spc()
            print ("******************************************")
            print ("***    WHAT WOULD YOU LIKE TO DO?   ******")
            print ("*** ------------------------------- ******")
            print ('***   1:  "WHO ARE THE CYDELS?"     ******')
            print ('***   2:  "THANK HIM AND CONTINUE   ******') 
            print ("*** ------------------------------- ******")
            print ("******************************************")
            time.sleep(1)
            if input('') == ('1'):
                time.sleep(1) 
                print('"WHO ARE THE CYDELS?"...\n')
                time.sleep(1)
                dot()
                time.sleep(1)
                dot()
                time.sleep(1)    
                dot()
                time.sleep(1)    
                dot()
                time.sleep(1) 
                dot()
                time.sleep(1)    
                dot()
                time.sleep(1) 
                dot()
                time.sleep(1)    
                dot()
                time.sleep(1)    
                dot()
                time.sleep(1)             
                dot()
                time.sleep(1)  
                typ=('YOU ASK HIM "WHO ARE THE CYDELS?" ...\n\n"THEY DWELL WITHIN THE DEPTHS OF THIS FOREST"...\n\n"THEY ARE RARELY SEEN BY ANYONE ASIDE FROM THEIR PREY"...\n\nYOU THANK HIM AND CONTINUE DEEPER INTO THE FOREST\n\n')              
                for char in (typ): 
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
 
                time.sleep(1) 
                dot()
                time.sleep(1) 
                dot()
                time.sleep(1) 
                spc()
                chooseDoor3()
                door3()
            else:   
                time.sleep(1) 
                typ=('THANK HIM AND CONTINUE ..\n\nDIE FROM CYDEL...\n\n')
                for char in (typ): 
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

                
                
                time.sleep(1)
                dot()
                time.sleep(1)    
                dot()
                time.sleep(1)    
                       
                
                typ=('YOU HAVE DIED...\n\n')
             
                for char in (typ): 
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

                
                
                ded = input('PLAY AGAIN: Y/N? \n\n')
                if ded == ('1'):
                   clr()
                   chooseDoor2 () 
                   door2()
                else: ded == sys.exit()  
                
    if door2 == '2':
        time.sleep(1) 
        dot()
        time.sleep(1) 
        dot()
        time.sleep(1)
        typ=('YOU ATTEMPT TO SNEAK PAST THE DARK ELF...\n\nDID YOU REALLY THINK YOU WOULD BE ABLE TO EVADE HIM?\n\nHE HEARS YOU...\n\nYOU SEE HIM DRAW AN ARROW...')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("***    WHAT WOULD YOU LIKE TO DO?   ******")
        print ("*** ------------------------------- ******")
        print ("***           1: RUN                ******")
        print ("***           2: FIGHT              ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        time.sleep(1)
        if input('') == ('1'):
            time.sleep(1) 
            typ=('RUN...\n\nYOU HAVE DIED...\n\n')
            
          
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            
    
            time.sleep(1)    
            dot()
            time.sleep(1)    
            dot()
            time.sleep(1)     

            ded = input('PLAY AGAIN: Y/N? \n\n')
            if ded == ('1'):
                chooseDoor2 () 
                door2()
            else: ded == sys.exit()     
        else:
            time.sleep(1) 
            print('FIGHT...\n\n')
            time.sleep(1)    
            dot()
            time.sleep(1)        
            
            typ=('YOU START TO RUN...\n\nAN ARROW PIERCES THROUGH THE BACK OF YOUR SKULL...\n\n')
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
            print('YOU HAVE DIED...\n\n')
            ded = input('PLAY AGAIN: Y/N? \n\n')
            if ded == ('1'):
                chooseDoor2 () 
                door2()
            else: ded == sys.exit()  

def chooseDoor2 ():    
  
    time.sleep(1)
    dot()
    time.sleep(1)
    dot()
    time.sleep(1)
    typ=('YOU VENTURE DEEPER INTO THE FOREST...\n\n......\n\nYOU COME ACROSS AN ENCAMPMENT...\n\nTHERE IS A DARK ELF GUARDING THE ENTRANCE…......\n\n......\n\nHE DOES NOT APPEAR TO BE FRIENDLY...')
    for char in (typ): 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)    
        time.sleep(1)
        spc()
    print ("******************************************")
    print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
    print ("****** ---------------------------- ******")
    print ("******   1: ASK HIM A QUESTION...   ******")
    print ("******   2: SNEAK BY UNNOTICED...   ******") 
    print ("****** ---------------------------- ******")
    print ("******************************************")
                                                                         #DOOR1
                 
        
def door1():
    door1 = input('')
    
    if door1 != '1':        
        typ=('YOU DECIDE TO GIVE UP HOPE...\n\n......\n\n......\n\nARE YOU SURE YOU WANT TO GIVE UP HOPE?!?\n\n......\n\n......\n\nTHINK ABOUT YOUR FAMILY?!?\n\n......\n\n......\n\nTHEY WILL NEVER KNOW WHAT HAPPENED TO YOU...\n\n')   
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******        GIVE UP HOPE?         ******")
        print ("****** ---------------------------- ******")
        print ("******         1: YES ...           ******")
        print ("******         2: NO ...            ******") 
        print ("****** ---------------------------- ******")
        print ("******************************************")
        if input('') == '1':
                time.sleep(1) 
                dot()
                time.sleep(1)
                dot()
                time.sleep(1)
                dot()
                time.sleep(1)
                typ=('THE SWAMP MONSTER LETS GO OF YOUR LEG AND RETURNS INTO THE MUD...\n\nIT MUST HAVE THOUGHT YOU WERE ALREADY DEAD...\n\nI HOPE THAT WAS YOUR PLAN...\n\n......\n\n......\n\n')
                for char in (typ): 
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.1)         
                time.sleep(1) 
                clr()
                chooseDoor2()
                door2()
        else: 
            time.sleep(1) 
            dot()
            time.sleep(1) 
            dot()
            time.sleep(1)
            typ=('YOU TRY TO PULL YOUR LEG BACK...\n\nKICKING IS HOPELESS WITHOUT YOUR LEGS...')     
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
                time.sleep(1)
                spc()
            print ("******************************************")
            print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
            print ("*** ------------------------------- ******")
            print ("***    1: TRY TO RUN                ******")
            print ("***    2: FIGHT FOR YOUR LIFE       ******") 
            print ("*** ------------------------------- ******")
            print ("******************************************")
            if input('') == '1':
                time.sleep(1) 
                typ=('YOU TRY TO RUN...\n\nYOU ARE STILL COMPLETELY STUCK...\n\nYOU STRUGGLE AND SQUIRM TO ESCAPE...\n\n......\n\n......\n\nYOUR LEGS ARE HOPELESSLY STUCK...\n\nYOU TRY TO PUNCH THE SWAMP MONSTER...\n\nYOUR FIST GOES DEEP INTO THE MUD...\n\nIT GRABS YOU BY THE WAIST AND PULLS YOU INTO YOUR MUDDY GRAVE...\n\nYOU HAVE DIED...\n\n')
                for char in (typ): 
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                ded = input('PLAY AGAIN: Y/N? \n\n')
                if ded == ('1'):
                   clr()
                   chooseDoor1 () 
                   door1()
                else: ded == sys.exit()  
            else: 
                time.sleep(1) 
                typ=('YOU TRY TO FIGHT FOR YOUR LIFE...\n\n......\n\n......\n\nYOUR LEGS ARE HOPELESSLY STUCK...\n\nYOU TRY TO PUNCH THE SWAMP MONSTER...\n\nYOUR FIST GOES DEEP INTO THE MUD...\n\nIT GRABS YOU BY THE WAIST AND PULLS YOU INTO YOUR MUDDY GRAVE...\n\nYOU HAVE DIED...\n\n')
           
                for char in (typ): 
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                ded = input('PLAY AGAIN: Y/N? \n\n')
                if ded == ('1'):
                   clr()
                   chooseDoor1 () 
                   door1()
                else: ded == sys.exit()  
    else: 
        time.sleep(1) 
        typ=('YOU DECIDE TO KICK IT IN THE FACE!!!\n\n......\n\n......\n\nYOU TRY TO PULL YOUR LEG BACK...\n\nBUT THE SWAMP MONSTER IS TOO FAST...\n\nIT GRABS YOUR OTHER LEG...\n\nKICKING IS HOPELESS WITHOUT YOUR LEGS...')      
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)          
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***    1: TRY TO RUN                ******")
        print ("***    2: FIGHT FOR YOUR LIFE       ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        if input() == '1':
            time.sleep(1) 
            typ=('YOU TRY TO RUN...\n\nYOU ARE STILL COMPLETELY STUCK...\n\nYOU STRUGGLE AND SQUIRM TO ESCAPE...\n\n......\n\n......\n\nIT GRABS YOU BY THE WAIST AND PULLS YOU INTO YOUR MUDDY GRAVE...\n\nYOU HAVE DIED...\n\n')
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)            
                ded = input('PLAY AGAIN: Y/N? \n')
            if ded == ('1'):
                clr()
                chooseDoor1 () 
                door1()
            else: ded == sys.exit()  
            
        else: 
            typ= ('YOU TRY TO FIGHT FOR YOUR LIFE...\n\n......\n\n......\n\nYOUR LEGS ARE HOPELESSLY STUCK...\n\nYOU TRY TO PUNCH THE SWAMP MONSTER...\n\nYOUR FIST GOES DEEP INTO THE MUD...\n\nIT GRABS YOU BY THE WAIST AND PULLS YOU INTO YOUR MUDDY GRAVE...\n\nYOU HAVE DIED...\n\n')
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            time.sleep(1)           
            ded = input('PLAY AGAIN: Y/N? \n\n')
            if ded == ('1'):
              clr()
              chooseDoor1 () 
              door1()
            else: ded == sys.exit()  
                          
def chooseDoor1 ():
        
        time.sleep(1)
        typ=('YOU WALK INTO THE FOREST...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        typ= ('THE PATH SEEMS CLEAR THIS WAY...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("*** ARE YOU SURE YOU WISH TO CONTINUE? ***")
        print ("***  -------------------------------   ***")
        print ("***    1: CONTINUE AHEAD               ***")
        print ("***    2: WALK BACK TO THE VILLAGE     ***") 
        print ("*** -------------------------------    ***")
        print ("******************************************")
        if input('') == ('2'):
            typ= ('YOU CHOOSE TO TURN BACK \n\nYOU START TO WALK BACK TOWARDS THE VILLAGE \n\nYOU SUDDENLY GET THE FEELING THAT YOU NEED TO TURN AROUND \n\n')          
            for char in (typ): 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
        typ=('YOU WALK DEEPER INTO THE FOREST...\n\n......\n\n......\n\n')  
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        typ=('THE PATH BECOMES TOO NARROW TO CONTINUE...\n\n......\n\n......\n\n')
        
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        typ=('YOU PUSH YOURSELF INTO THE DARKNESS HOPING TO SEE LIGHT AGAIN...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        dot() 
        typ=('THERE IS A CLEARING AHEAD!!!\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        dot()
        typ=('YOU START TO RUN TO GET OUT OF THE MESS YOU PUT YOURSELF IN...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)  
        dot()
        typ=('SUDDENLY YOU CAN NO LONGER MOVE...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(.1)
        typ=('YOUR LEG IS STUCK IN SOME MUD...\n\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        
        typ=('AS YOU LIFT YOUR LEG OUT OF THE MUD A HAND RISES OUT OF THE MUD...\n')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        typ=('YOU WERE WARNED ABOUT THESE TYPES OF SWAMP MONSTERS...')
        for char in (typ): 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        spc()
        print ("******************************************")
        print ("******  WHAT WOULD YOU LIKE TO DO?  ******")
        print ("*** ------------------------------- ******")
        print ("***     1: KICK IT IN THE FACE!!!   ******")
        print ("***     2: GIVE UP HOPE...          ******") 
        print ("*** ------------------------------- ******")
        print ("******************************************")
        door1()
                                                             # STARTS GAME

START_GAME()












#displayIntro()


   
#intro_input()
#clr()

#intro()

#chooseDoor1 ()
#door1()








                                                                   # NEEDS WORK
    
'''for character in intro:
        sys.stdout.write(character)
        sys.stout.flush()
        time.sleep(0.05)
'''            
    










  
    

