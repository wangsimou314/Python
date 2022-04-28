import numbers

has_ticket = False
knife_length = 21

if has_ticket:
    if knife_length <= 20:
        print('Enter')
    else:
        print('You are too danger to enter')
else:
    print('Please buy the ticket')
