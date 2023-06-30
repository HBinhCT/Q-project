s = input().strip()
parts = s.split('.')
if len(parts) != 4:
    print('NO')
else:
    for part in parts:
        try:
            val = int(part)
            if val < 0 or val > 255:
                print('NO')
                break
        except ValueError:
            print('NO')
            break
    else:
        print('YES')
