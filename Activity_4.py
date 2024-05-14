#ACTIVITY 4_2 Sorting dictionaries

_dict = {
    8: {'name':'JOE', 'details':{'age':'19','brgy':'Fairview'}, 'subject':{'DASTRUC':[1.0, 4.0, 3.0]}},
    6: {'name':'KYL', 'details':{'age':'22','brgy':'Maligaya'}, 'subject':{'DASTRUC':[2.0, 4.0, 1.0]}},
    3: {'name':'CHA', 'details':{'age':'26','brgy':'Fairview'}, 'subject':{'DASTRUC':[1.0, 2.0, 4.0]}},
    1: {'name':'PAT', 'details':{'age':'28','brgy':'Maligaya'}, 'subject':{'DASTRUC':[3.5, 2.0, 4.0]}},
    4: {'name':'TAP', 'details':{'age':'21','brgy':'Fairview'}, 'subject':{'DASTRUC':[2.5, 2.0, 1.5]}},
    5: {'name':'CAT', 'details':{'age':'23','brgy':'Maligaya'}, 'subject':{'DASTRUC':[1.5, 4.0, 3.0]}}
}

print("key sorted in a ascending format:")
_list = list(_dict.items())
_list.sort()
for i in range(0, len(_list)):
    print("Key:",_list[i][0],"\b, Name:",_list[i][1]['name'],"\b, Age:",_list[i][1]['details']['age'],"\b, Barangay:",_list[i][1]['details']['brgy'])


print("Age sorted in descending format:")
_list1 = list()
_list1.extend(_dict.values())
_list1.sort(key= lambda x: x['details']['age'], reverse=True)
for i in range(0, len(_list1)):
    print("My name is:",_list1[i]['name'],"with an age of:",_list1[i]['details']['age'],"years old and lives at barangay",_list1[i]['details']['brgy'])


print("grades sorted in ascending format:")
for i in range(0, len(_list)):
    _list[i][1]['subject']['DASTRUC'].sort()
    print("My name is:",_list[i][1]['name'],"with an ID number of:",_list[i][0],"will achieve a grade of:",_list[i][1]['subject']['DASTRUC'])