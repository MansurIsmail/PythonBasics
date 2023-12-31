
"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary
"""

friends = {'fname': 'Jan-Klod', 'lname': 'Van-Dam', 'age': '55', 'city': 'Kwebek'}
for i in friends:
    print(friends[i])

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program
"""

f_numbers = {'mom': '3', 'dady': '7', 'bro': '11', 'sis': '8', 'mine': '5'}
for i in f_numbers:
    print(f"{i}'s favorite number is {f_numbers[i]}")

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output
"""

glossary = {'mom': '3', 'dady': '7', 'bro': '11', 'sis': '8', 'mine': '5'}
for i in glossary:
    print(f"{i} meaning is: \n{glossary[i]}")

"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your 
glossary. When you run your program again, these new words and meanings 
should automatically be included in the output.
"""

glossary4 = {'mom': '3', 'dady': '7', 'bro': '11', 'sis': '8', 'mine': '5'}
for k, v in glossary4.items():
    print(k + ' meaning is:')
    print(v)

glossary4['nik']= '12'
glossary4['joe'] = '14'
for k, v in glossary4.items():
    print(k + ' meaning is:')
    print(v)

"""
6-5. Rivers: Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.
"""

rivers = {'dnepr': 'ukraine', 'amazon': 'brasil', 'volga': 'russia', 'mississippi': 'usa'}
for k, v in rivers.items():
    print('The ' + k.title() + ' runs through ' + v.title() +'.')

for k in rivers:
    print(k.title())

for v in rivers.values():
    print(v.title())

for i in rivers:
    print((rivers[i]).title())

"""
6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take 
the poll
"""
