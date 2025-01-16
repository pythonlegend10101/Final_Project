#Diego
#computer science 101 final assignment: boss fight
#1/8/25

#pseudocode
#start

    #import random

    #make list(enemies)
        #ask player to chose enemy
    #make list (weapons)
        #ask player to chose weapon
        #remove chosen one
    #make list(chosen weapon)
        #add chosen one to this list


    #determine player's health (health1)
    #determine enemy's health (health2)



    #create while loop:
        #ask player if they want to roll and attack or block

        #if they attack:
            #roll dice based of weapon's range
            #remove dice number from enemy's health
        #if block:
            #roll dice

        #roll enemy damage
        #if player blocked:
            #remove dice number from enemy's damage
            #remove enemy damage from health
        #if player did not block :
            #remove enemy damage from health

        #if health 1 <= 0:
            #print player win message
            #break
        #if health 2 <=0:
            #print player lost message
            #break
    #print "thanks for playing" message

#end

import random
import time
import sys

enemies = ["Bear","Dragon","Hounds"]                         #enemy list
weapons = ["Morning star","Medium sword","Dagger"]   #weapon list
a,b,c=enemies       #assign list items
x,y,z=weapons

try:
    print("You venture the woods in search of treasure...")     #context
    time.sleep(1.5)
    print("You enter a dungeon that could have goods...")
    time.sleep(1.5)
    print("\nYou explore...\n")
    time.sleep(2)
    print("You encounter three paths")                              #pick boss
    enemy = input("Pick one (a, b , or c) ")

    print("You sense danger in the darkness beyond...")
    time.sleep(1.5)
    print("You bring out your bag")
    time.sleep(1.5)
    print("\nSearching...\n")
    time.sleep(2)
    print("\nIn your bag there are three weapons")           #pick weapon
    weapon = input("What weapon do you pick (x,y,z) ")


except ValueError:
    print("Error, Please write letters")        #error catching 
except Exception:
    print(Exception)


else:
    
    health1 = 100                                                                #determine player health
    if enemy == "a":
        print("\nInside a immense cave you have found a",a)                                      #determine bear option(health, damage)
        print ("The bear is a tough oponent!\n")
        time.sleep(1)
        health2= 55
        enemy_dmg=18
    elif enemy == "b":
        print("\nInside a immense cave you have found a",b)                                       #determine dragon option(health, damage)     
        print("The dragon is incredibly strong! Good luck!\n")
        time.sleep(1)
        health2= 75
        enemy_dmg=25
    elif enemy == "c":
        print("\nInside a immense cave you have found a",c)                                       #determine hounds option(health, damage)
        print("The hounds are very weak enemies!\n")
        time.sleep(1)
        enemy_dmg=20
        health2 = 45

    if weapon == "x":
        print("You have picked up a",x)
        print("The morning star is a reliable weapon!\n")                                          #determine morning star option(damage, block)
        damage = 15
        block = 30

    elif weapon == "y":
        print("You have picked up a",y)
        print("The medium sword is very strong!\n")                                                 #determine medium sword option(damage, block)
        damage = 20
        block = 25

    elif weapon == "z":
        print("You have picked up a",z)
        print("The dagger is very weak! Good luck!\n")                                              #determine dagger option(damage, block)
        option(damage, block)
        damage = 8
        block = 18

    elif enemy != "a" or enemy != "b" or enemy != "c":
        print("You have typed in something incorrect")                  #if typed wrong letter 
        print("The program will now close")                                  #close program
        exit()

    elif weapon != "x" or weapon != "y" or weapon != "z":           
        print("You have typed in something incorrect")                  #if typed wrong weapon
        print("The program will now close")                                  #close program
        exit()

while True:     #start loop



    blocked=0   #reset blocked points

    time.sleep(1)

    try:
        choice = input("Do you want to attack (type 1) or block (type 2) ")     #ask for choice

    except ValueError:
        print("Error, Please type 1, or 2")     #error catching
    except Exception:
        print("ERROR!")


    else:
        if choice == "1":
            attack = random.randint(1,damage)                                                           #attacking
            health2 = health2-attack
            print("\nAttacking...")
            time.sleep(2)
            print("\nYou have attacked! You damage the enemy for:",attack,"points")         #printing attack results
            print("Enemy's health bar:",health2)

        if choice == "2":
            blocked = random.randint(3,block)                                                             #blocking
            print("\nYou have blocked! You blocked for",blocked,"points")                       #printing block results 

        if health2<=0:
            print("YOU WON!")                                                   #if enemy dies after attack
            print("The enemy's health has reached",health2)            #print health and end game
            break
    

        enemy_atk= random.randint(1,enemy_dmg)      #enemy attack roll

        if choice == "2":
            enemy_atk= enemy_atk-blocked                                                                                        #if blocked attack
        health1 = health1-enemy_atk                                                                                                 #block roll
        print("\nEnemy attacking...")
        time.sleep(2)
        print("\nThe enemy attacks! It damages you for",enemy_atk,"points. Points blocked:",blocked)        #print attack results and blocked points
        print("Your health bar:",health1)


        if health1 <=0:
            print("YOU LOST!")
            print("Your health has reached",health1,)           #if you die after enemy attack
            break                                                           #end game



print ("\nThank you for playing")                               #final message

#pseudocode correction
#add time sleep when printing for better readability
#add time sleep for attacks
#if fail to pick weapon or boss close program


    







    