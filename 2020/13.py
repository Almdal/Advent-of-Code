



if __name__ == '__main__':
    ts,ids = open('input/13_test.txt').readlines()
    ts, ids = open('input/13.txt').readlines()
    ts = int(ts)

    iids = []
    for i in ids.split(','):
        if not i == 'x':
            iids.append(int(i))

    print(iids)
    i = ts
    found = False
    found_id = 0
    while i < 10000000000000 and not found:
        for id in iids:
            if i % id == 0:
                #print(f'Found departure at {i}')
                found = True
                found_id = id
                break
        if not found:
            i += 1
        else:
            break

    if found:
        res = (i-ts)*found_id
        print(f'Finished. And found match at {i}/{found_id}. {res}')

    print(ts, ids)
