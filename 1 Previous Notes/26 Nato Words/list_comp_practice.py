numbers = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1

new_list.append(add_1)

#keywords to focus on
new_list = [new_item for item in list]

#with list comprehension
new_list = [n + 1 for n in numbers]
#output will be new_list = [2, 3, 4]

#just because it is called list comprehension it doesnt mean it can work with only list
name = "josh"
letters_list = [letter for letter in name]
#output name = ['j', 'o', 's', 'h']

#python sequences: list range string tuple
range(1,5)
new_numbers = [n*2 for n in range(1,5)] #remember range cuts of last number so this is 1-4
#output new_numbers = [2, 4, 6, 8]

#conditional list comprehension
new_list = [new_item for item in list if test]
names = ["adam", "bob", "charlie", "dave", "edgar", "francis"]
short_names = [name for name in names if len(name)<5]
#output short_names = ['adam', 'bob', 'dave']

long_names = [name.upper() for name in names if len(name) > 5]
#output long_names = ["CHARLIE", "FRANCIS"]

#dictionary comprehension
new_dict = {new_key: new_value for item in list}

#new dict based on value of current dict
new_dict = {new_key: new_value for (key,value) in dict.items()}

#conditional
new_dict = {new_key: new_value for (key,value) in dict.items() if test}

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

#data frames
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through column of a data frame
for (key, value) in student_data_frame.items():
    print(key)

#loop through rows of a data frame
for(index,row) in student_data_frame.iterrows():
    print(row)


