from replit import clear
#HINT: You can call clear() to clear the output in the console.
bid={}
should_continue=True


def bidding_process(bid_info):
  highest_value=0
  winner=""
  for bidder in bid_info:
      each_info=bid_info[bidder]
      if each_info>highest_value:
        highest_value=each_info
        winner=bidder
  print(f"The highesr winner is {winner}with a bid of ${highest_value}")            
        
while  should_continue:
    
    name=input("what is your name? ")
    price=int(input("what is your bid? "))
      
    bid[name]=price
    bid_confirm=input(f"say'yes'to continue,say'no'to exit: ")
    if bid_confirm=="yes":
          clear()
    else:
      should_continue=False                              
          
bidding_process(bid_info=bid)          