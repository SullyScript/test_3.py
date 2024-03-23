# ECOR 1042 Lab 4 - Individual submission for test3 function

#import check module here
import check
import load_data
#import load_data module here


#check.equal(character_occupation_list('characters-test.csv', 'AT'),)
from load_data import character_occupation_list, character_strength_list, character_luck_list, character_weapon_list, load_data, calculate_health


open('characters-test.csv', 'r')

 
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "55"

#==========================================#
#Do not modify the code already provided.


def test_return_correct_dict_inside_list():
    
    filename = "characters-test.csv"
    #result = character_occupation_list('characters-test.csv','WA')
    
    
    expected_first = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
                      
    #{'Occupation': 'Warrior', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 
                   #   'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    
    expected_last = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
      
    
    
    check.equal(character_occupation_list('characters-test.csv','WA')[0], expected_first, "First character data incorrect.")
    check.equal(character_occupation_list('characters-test.csv','WA')[-1], expected_last, "Last character data incorrect.") 
    
    
    occupation_key = list(character_occupation_list('characters-test.csv','WA')[0].keys())[0]
    #print(occupation_key)
    
    occupation_value = list(character_occupation_list('characters-test.csv','WA')[0].values())[0]
    #print(occupation_value)
   
    
    check.equal(occupation_key,"Occupation3") 
    
    #print("1. ", test_occupation)
    
    #if (test_occupation == True):
        #print("True")
    #else:
        #print("False")
        
    
    
    
    
    
if __name__ == "__main__":
    test_return_correct_dict_inside_list()
    
    
    
    #Complete the function with your test cases

    
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    
    expected_first = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
    
    expected_last = {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    
    #Fix later
    expected_other = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}  
      
    
    check.equal(character_occupation_list('characters-test.csv','WA')[0], expected_first, "First character data incorrect.")
    check.equal(character_occupation_list('characters-test.csv','WA')[-1], expected_last, "Last character data incorrect.") 
    check.equal(character_occupation_list('characters-test.csv','WA')[0], expected_other, "First character data incorrect.")
    #are cheching teh same thing not three different
    
    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
    expected_first = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
    
    expected_last = {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    
    #Fix later
    expected_other = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}  
      
    
    #check.equal(character_strength_list('characters-test.csv',(1,7))[0], expected_first, "First character data incorrect.")
    #check.equal(character_strength_list('characters-test.csv',(1,7))[-1], expected_last, "Last character data incorrect.") 
    #check.equal(character_strength_list('characters-test.csv',(4,17))[0], expected_other, "First character data incorrect.")    
    

    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    expected_first = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
    
    expected_last = {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    
    #Fix later
    expected_other = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}  
      
    
    check.equal(character_occupation_list('characters-test.csv',0.67), expected_first, "First character data incorrect.")
    check.equal(character_occupation_list('characters-test.csv',0.67), expected_last, "Last character data incorrect.") 
    check.equal(character_occupation_list('characters-test.csv',0.5), expected_other, "First character data incorrect.")    
    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)
    expected_first = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
    
    expected_last = {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    
    #Fix later
    expected_other = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}  
    
    check.equal(character_occupation_list('characters-test.csv','Short sword')[0], expected_first, "First character data incorrect.")
    check.equal(character_occupation_list('characters-mat.csv','Short sword'), expected_last, "Last character data incorrect.") 
    check.equal(character_occupation_list('characters-mat.csv','Spear'), expected_other, "First character data incorrect.")    
    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    
    
    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
    
    
   
    check.summary()
    

# Do NOT include a main script in your submission
