'''
Date: 5/8/2002 9:04pm
@Author: Ifeanyi Onovo
@Email: Ifeanyionovo38@gmail.com
'''
# empty dictionary to collect data from the input
bidding_info = {}

# bidding function to hold the data and return the highest bidder
#check below to understand how the function is working
def biddingrecord(bidding_record):
    highest_bidder = 0
    winner = " "
    for bidders in bidding_record:
        bid_amount = bidding_record[bidders] 
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidders
    print(f'Thank you for bidding, the  winner is {winner} with the the highest bid of  ${highest_bidder}')

#declare variable for while loop
keep_running = False

#wrap the input code in a while loop to keep the code running
while not keep_running:
    

    name = input('What is your name? ')
    bidding_amount = int(input('What\'s your bidding amount? $'))

    bidding_info[name] = bidding_amount
    bid_again = input('Do you want to bid again? type? "yes" or "no"')
    if bid_again == 'yes':
        keep_running = False
    else:
        
        keep_running = True
        biddingrecord(bidding_info)

'''

#This will help you understand how the function is working
my_dic = {'ifeanyi': 2000, 'ifeco': 3000, 'ify': 8000}
highest = 0
number = 0
winner = '' #optional
for nums in my_dic:
    bignumber = my_dic[nums] # get the dictionary value
    if bignumber > highest: # use the if no compare the values 
        highest = bignumber # return the highest value
        winner = nums  # output the dictioanry keys
print(f'{winner} has highest {highest} number')  ''' 

