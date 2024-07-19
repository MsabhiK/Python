# 1.1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
print("\n--------------------------------\n")

#1.2. Change the last_name of the first student from 'Jordan' to 'Bryant
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"]="Bryant"
print(students)
# 1.3. In the sports_directory, change 'Messi' to 'Andres'
print("\n--------------------------------\n")
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0]="Andres"
print(sports_directory)

# 1.4. Change the value 20 in z to 30
print("\n--------------------------------\n")
z = [ {'x': 10, 'y': 20} ]
z[0]["y"]=30
print(z)

# 2.1. Iterate Through a List of Dictionaries
print("\n--------------------------------\n")
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(0, len(list)):
        result=""
        for key, val in list[i].items():
            result+=f" {key} - {val} \n" 
        print(result)
iterateDictionary(students)  
"""
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
# 3. Get Values From a List of Dictionaries
print("\n--------------------------------\n")
def iterateDictionary2(by_key, list):
    for i in range(0, len(list)):
        for key, val in list[i].items():
            if(key==by_key): 
                print(val)
iterateDictionary2("first_name", students)  
print("--------------------------------")
iterateDictionary2('last_name', students) 

# 4. Iterate Through a Dictionary with List Values
"""
 dojo = {
 'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 
'Burbank'],
 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 
'Devon']
 }
 printInfo(dojo)
 # output:
 7 LOCATIONS
 San Jose
 Seattle
 Dallas
 Chicago
 Tulsa
 DC
 Burbank
 8 INSTRUCTORS
 Michael
 Amy
 Eduardo
 Josh
 Graham
 Patrick
 Minh
 Devon

"""
print("\n--------------------------------\n")
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 
'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 
'Devon']
}
def printInfo(dictionary):
    for key, val in dictionary.items():
        print("##################################")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

printInfo(dojo)
