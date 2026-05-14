# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:47:12 2026

@author: josep

Demo on file i/o and classes in python as applied to dnd
There is a LOT missing here but i wanted to make something simple and accessible

"""
import json
import random as r

# OPEN THE JSON FILE
# 5e monster database from breni-tiber on github
# link: https://github.com/5e-bits/5e-database/blob/main/src/2014/en/5e-SRD-Monsters.json
# use the with keyword to automatically close after, safest
with open("monsters.json") as f:
    monsters = json.load(f)

playerCharacters = []  # you really shouldn't use globals but i am here :/

# A class is a blueprint for objects of that type. In dnd, all characters have these characteristics.
class Player:
    def __init__(self, name, race, charClass, subclass, strength, dex, con, wis, intel, cha):
        self.name = name
        self.race = race
        self.charClass = charClass
        self.subclass = subclass
        self.strength = strength
        self.dex = dex;
        self.con = con;
        self.wis = wis;
        self.intel = intel;
        self.cha = cha;
        self.hp = con * 2;

def main():
    print("Create your character!")
    createCharacter() # user character is an object of the player class
    printCharacterSheet(playerCharacters[0])
    genRandomEncounter(playerCharacters[0])

def createCharacter():
    name = input("What is your character's name? ").lower()
    race = input("What is your character's race? ").lower()
    charClass = input("What is your character's class? ").lower()
    
    # Use of a conditional to give warlocks, sorcerers, or clerics their lvl 1 subclass/domain
    if (charClass == "warlock" or charClass == "sorcerer" or charClass == "cleric"):
        subclass = input("Which subclass? ").lower()
    else:
        subclass = "none"
    
    # I'd recommend adding do-while verifications based on DND rules here, but
    # I don't know them off the top of my head, and I want this to be simple.
    
    strength = int(input("How strong is your character? "))
    dex = int(input("How dexterous is your character? "))
    con = int(input("What is your character's constitution like? "))
    wis = int(input("How wise is your character? "))
    intel = int(input("How intelligent is your character? "))
    cha = int(input("How charismatic is your character? "))
    
    # You could call a 'applyRacialBonuses' function here
    
    playerCharacters.append(Player(name, race, charClass, subclass, strength, dex, con, wis, intel, cha))
    
def printCharacterSheet(character):
    print(f"\nName: {character.name}\nRace: {character.race}\n\
Class: {character.charClass}\nSubclass: {character.subclass}\n\
Strength: {character.strength}\nDexterity: {character.dex}\n\
Constitution: {character.con}\nWisdom: {character.wis}\n\
Intelligence: {character.intel}\nCharisma: {character.cha}\n")
    
def genRandomEncounter(character):
    monster = r.choice(monsters)
    monsterHP = monster['hit_points']
    
    print(f"Oh no! You've ran into a {monster['name']}")
    
    monsterInitiative = r.randint(1, 20)
    playerInitiative = r.randint(1, 20)
    
    if (playerInitiative == monsterInitiative):
        playerInitiative += 1
        
    if (playerInitiative > monsterInitiative):
        player1 = character
        player2 = monster
    else:
        player1 = monster
        player2 = character
        
    while (character.hp > 0 and monsterHP > 0):
        attack = r.randint(1, 20)
        
        if player1 == character:
            attack += character.strength - 10
            monsterHP -= attack
            print(f"{character.name} attacks for {attack} damage.")
            
            if (monsterHP <= 0):
                print(f"{monster['name']} died to your blow.")
            else:
                print(f"{character.name} hits {monster['name']} for {attack} damage! ({monsterHP} HP remaining)")
            player1, player2 = player2, player1
        
        else:
            attack += monster['strength'] - 10        
            character.hp -= attack
            print(f"{monster['name']} attacks for {attack} damage.")
            
            if (character.hp <= 0):
                print(f"{character.name} died.")
            else:
                print(f"{monster['name']} hits {character.name} for {attack} damage! ({character.hp} HP remaining)")
            player1, player2 = player2, player1
            
    print()
    
main()