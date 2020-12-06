
test_input = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
#    BFFFBBFRRR: row 70, column 7, seat ID 567.
#    FFFBBBFRRR: row 14, column 7, seat ID 119.
#    BBFFBBFRLL: row 102, column 4, seat ID 820.



def bisect(letter, low, high):

    rng = (high-low) / 2
    
    if letter in ['F', 'L']:
        return (low, high-rng)

    if letter in ['B' ,'R']:
        return (low+rng,high)

    
    
if __name__ == '__main__':
    boardingpass = open('input/5.txt').readlines()
    #boardingpass = test_input
    #boardingpass = ['FBFBBFFRLR']

    ids = []
    highest_id = 0
    for bpass in boardingpass:
        
        rows = bpass[0:7]
        seats = bpass[-4:-1]

        low_row = 0
        high_row = 128
        
        for row in rows:
            low_row, high_row = bisect(row, low_row, high_row)

        low_seat = 0
        high_seat = 8
        for s in seats:
            low_seat, high_seat = bisect(s, low_seat, high_seat)

        seat_id = low_row*8 + (high_seat-1)
        
        ids.append(seat_id)


        if seat_id > highest_id:
            highest_id = seat_id

    print('highest id is ', highest_id)
    ids.sort()

    for i in range(0, len(ids)-1):
        if (ids[i+1] == ids[i] + 2):
            print ('We have the Seat ID: ', ids[i] + 1)


