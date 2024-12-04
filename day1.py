with open('day1_input.txt' , 'r') as file : 
    data = file.read().split()
     
first_row = data[::2]
second_row = data[1::2]

first_row.sort()
second_row.sort()

total_distance = 0
for f, s in zip(first_row , second_row):
    if int(f) >= int(s) :
        distance = int(f) - int(s)
    elif int(f) < int(s) :
        distance = int(s) - int(f)
    total_distance += distance

print(f"part one awnser : {total_distance}")

similarity_score = 0
for f in first_row :
    times_repeated = second_row.count(f)
    similarity = int(f) * int(times_repeated)
    similarity_score += similarity

print(f"part two awnser : {similarity_score}")

    