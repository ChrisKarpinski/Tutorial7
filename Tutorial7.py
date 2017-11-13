# Tutorial 7 

from PersonClass import Person

p1 = Person("John", "Smith", 20, "111 Street St.", "613-613-6136", "john-smith@hotmail.com", ["swimming", "chess", "physics"])

p2 = Person("Bob", "Bill", 30, "120 Avenue St.", "613-613-1234", "bob-bill@hotmail.com", ["hiking", "soccer", "math"])

p3 = Person("Carl", "Jim", 10, "120 Way St.", "613-456-1234", "Carl-Jim@cmail.com", ["english", "skating", "running"])

p4 = Person("Jim", "Jones", 40, "120 Up St.", "822-456-1234", "JIM-Jones@cmail.com", ["english", "bowling", "skiing"])

people = [p1, p2, p3]

for person in people: 
    
    print(person)
    

def over_age(people, age): 
    
    for person in people: 
        
        if person.age > age: 
            
            print(person)
            
def something_in_common(person1, person2): 
    
    for interest in person1.interests: 
        
        if interest in person2.interests: 
            
            return True
        
    return False    
    
    
#over_age(people, 18)  

p1.add_interest("hiking") # Question 3
print(p1)
p1.remove_interest("chess") # Question 4
print(p1)

print(something_in_common(p3, p4)) # Question 5
