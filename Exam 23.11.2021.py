# ----------------------------Again, Writen in python---------------------------


rider_count = 0


while rider_count != 8:
    rider_height = int(input('What is the height of the rider? (In cm) --> '))

    if rider_height >= 140:
        print ('This person is allowed to ride on this attraction.\n')
        can_ride = True


    elif rider_height >= 120:

        adult_check = True

        while adult_check:

            adult_yn = input('Is this person going to be accompanied by an adult? (Y/N) --> ')

            if adult_yn == 'Y':
                can_ride = True
                adult_check = False

                if rider_count == 8:
                    print('Unfortunatly, there are already enough riders for this attraction.\n')

            elif adult_yn == 'N':
                can_ride = False
                adult_check = False
                print('Unfortunatly, this person is not tall enough to ride on this attraction.\n')

            else:
                print('Please enter Y/N (caps).\n')
                adult_check = True

    else:
        print('Unfortunatly, this person is not tall enough to ride on this attraction.\n')
        can_ride = False

    if can_ride == True:
        rider_count +=1

    if rider_count == 8:
        print('Unfortunatly, there are already enough riders for this attraction.\n')
