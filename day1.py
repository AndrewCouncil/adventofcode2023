with open('day1input.txt') as f:
    data = f.read()
    lines = data.split('\n')
    
    # so nasty but it works
    possible_nums_p1 = [str(n) for n in range(10)]
    str_to_num = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '0':0,
    }

    sum = 0
  
    for line in lines:
        left_pos_best = 9999999
        left_num = None
        right_pos_best = -1
        right_num = None
        for num in str_to_num.keys():
            left_pos = line.find(num)
            if left_pos != -1 and left_pos < left_pos_best:
                left_pos_best = left_pos
                left_num = str_to_num[num]
            
            right_pos = line.rfind(num)
            if right_pos > right_pos_best:
                right_pos_best = right_pos
                right_num = str_to_num[num]

        # print(f"{left_num} {right_num}")
        sum += left_num * 10 + right_num

    print(sum)
