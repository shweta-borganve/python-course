count = 10

while count > 0:
    if count % 3 == 0:
        count -= 1
        continue
    print(f'Processing Number {count}')
    count -= 1