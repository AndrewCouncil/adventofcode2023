with open('day1input.txt') as f:
    data = f.read()
    lines = data.split('\n')
    
    # so nasty but it works
    sum = 0
    for line in lines:
        num = 0
        for c in line:
            if c.isdigit():
                num += int(c) * 10
                break
        for c in reversed(line):
            if c.isdigit():
                num += int(c)
                break
        sum += num

    print(sum)
        
