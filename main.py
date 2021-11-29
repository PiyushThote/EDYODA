x = 10
booked_seat = 0
prize_of_ticket = 0
current_income = 0
total_income = 0
row = int(input('Enter the number of rows:\n'))
seats = int(input('Enter the number of seats in each row:\n'))
total_seat = row*seats
if total_seat <= 60:
    total_income = 10*(row*seats)
else:
    total_income = (10 * (row//2)*seats) + (8 *(row-(row//2))*seats)
booked_ticket_details = [[None for j in range(seats)] for i in range(row)]

class chart:
    def chart_maker():
        seats_chart = {}
        for i in range(row):
            seats_in_row = {}
            for j in range(seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart
    
    def find_percentage():
        percentage = (booked_seat/total_seat)*100
        return percentage

class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print('\n1. Show the seats \n2. Buy a Ticket \n3. Statistics ',
          '\n4. Show booked Tickets User Info \n0. Exit ')
    x = int(input('Select Option : '))
    if x == 1:
        if seats < 10:
            for seat in range(seats):
                print(seat, end='  ')
            print(seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, seats):
                print(seat, end=' ')
            print(seats)
        if seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant seats =', total_seat - booked_seat)
        
    elif x == 2:
        row_number = int(input('Enter Row Number :\n'))
        Column_number = int(input('Enter Column Number :\n'))
        if row_number in range(1, row+1) and Column_number in range(1, seats+1):
            if table_of_chart[str(row_number-1)][str(Column_number)] == 'S':
                if row*seats <= 60:
                    prize_of_ticket = 10
                else:
                    if row_number <= int(row/2):
                        prize_of_ticket = 10
                    else:
                        prize_of_ticket = 8
                print('prize of ticket : ${}'.format(prize_of_ticket))
                conform = input("Enter 'Yes' for booking or 'No' for Stop booking :\n")
                person_detail = {}
                if conform.lower() == 'yes':
                    person_detail['Name'] = input('Enter Name: ')
                    person_detail['Gender'] = input('Enter Gender: ')
                    person_detail['Age'] = input('Enter Age: ')
                    person_detail['Phone_No'] = input('Enter Phone number: ')
                    person_detail['Ticket_prize'] = prize_of_ticket
                    table_of_chart[str(row_number-1)][str(Column_number)] = 'B'
                    booked_seat += 1
                    current_income += prize_of_ticket
                else:
                    continue
                booked_ticket_details[row_number-1][Column_number-1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print('Please, Enter valid Row or Column Number')

    elif x == 3:
        print('Number of purchased Tickets:', booked_seat)
        print('Percentage: {}%'.format(class_call.find_percentage()))
        print('Current Income: ${}'.format(current_income))
        print('Total Income: ${}'.format(total_income))
        
    elif x == 4:
        Enter_row = int(input('Enter row number :\n'))
        Enter_column = int(input('Enter Column number :\n'))
        if Enter_row in range(1, row+1) and Enter_column in range(1, seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = booked_ticket_details[Enter_row - 1][Enter_column - 1]
                print('Name:', person['Name'])
                print('Gender:', person['Gender'])
                print('Age:', person['Age'])
                print('Ticket Prize: ${}'.format(person['Ticket_prize']))
                print('Phone Number:', person['Phone_No'])
            else:
                print('This seat is Vacant')
        else:
            print('Please, Enter valid Row or Column Number')
            
    elif x == 0:
        print("\nThanks for Visiting.\nHave A Nice Day.")
        break
        
    else:
        print('Please, Enter Valid Option')