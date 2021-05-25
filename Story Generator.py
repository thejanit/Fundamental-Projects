import random

part_1 = ['A few years ago', 'Yesterday', 'last night', 'A long time ago' , 'On 20th Jan']
part_2 = ['a rabbit' , 'an elephant' , 'a mouse' , 'a turtle' , 'a cat']
part_3 = ['Ali', 'Mohit', 'Sonam', 'Puran', 'Rani']
part_4 = ['Prayagraj', 'Delhi', 'Chandigarh', 'Sultanpur', 'Bhopal']
part_5 = ['cinema', 'university', 'seminar', 'school', 'laundry']
part_6 = ['made lot of friends', 'eats a burger', 'found a secret a key', 'solved a mystery', 'wrote a book']

print(random.choice(part_1) + ' , ' + random.choice(part_2) + ' , ' + random.choice(part_3) + ' , ' + random.choice(part_4)
      + ' , ' + random.choice(part_5) + ' , ' + random.choice(part_6))