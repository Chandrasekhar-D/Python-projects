try :
    nominee_1 = input('Enter name of 1st nominee : ')
    nominee_2 = input('Enter name of 2st nominee : ')
except :
    if EOFError:
        print('You must enter the nominee name in string data type')
    else :
        print('Somthing went wrong try again')    
no1_votes = 0
no2_votes = 0

voter_ids = list(range(1,11))

no_of_votes = len(voter_ids)


while True:
    if voter_ids == []:
        print('Voting section is over !!')
        if no1_votes > no2_votes :
            print(nominee_1,' total votes count : ',no1_votes)
            print(nominee_2,' total votes count : ',no2_votes)
            if no2_votes == 0 :
                percent = no1_votes*100
            else :    
                percent = (no1_votes/no2_votes)*100
            print(nominee_1,'has won this election with :',int(percent),'% votes')
            print('congratulation ***',nominee_1,'***')
            break
        elif no2_votes > no1_votes :
            print(nominee_1,' total votes count : ',no1_votes)
            print(nominee_2,' total votes count : ',no2_votes)
            if no1_votes == 0 :
                percent = no2_votes*100
            else :    
                percent = (no1_votes/no2_votes)*100
            print(nominee_2,'has won this election with :',int(percent),'% votes')
            print('congratulation ***',nominee_2,'***')
            break
        else :
            print('Both got equal votes !!')
            break

#if time out Or any other reasons to stop voting and given result.  enter : 9999 
    try :
        voter = int(input('Enter your voter ID : '))
    except:
        if EOFError:
            print('You must have enter valid voter ID number in <int> data type')
            break
        else :
            print('Somthing went wrong try again')
            break    

    if voter == 9999 :
        voter_ids = []
    elif voter in voter_ids:
        print('your are a voter')
        print('---------------------')
        print('If you want give vote to <', nominee_1 ,'> Press 1')
        print('If you want give vote to <', nominee_2 ,'> Press 2')
        print('---------------------')
        vote = int(input('Enter your vote : '))
        if vote == 1:
            voter_ids.remove(voter)
            no1_votes += 1
            print('Thanks for your vote , You voted to : ',nominee_1,)
            print('*******')
        elif vote == 2:
            voter_ids.remove(voter)
            no2_votes += 1
            print('Thanks for your vote , You voted to : ',nominee_2,)
            print('*******')
        elif vote > 2 :
            print('Check your entered key')
    
    else :
            print('You are not a voter OR You have already voted')    