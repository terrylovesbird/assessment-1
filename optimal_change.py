# Write your solution here!
def optimal_change(item_cost, amount_paid):
    #calculate how much is the change
    change = amount_paid - item_cost
    #having a dict of denominations, bill : value; Since its "optimal", so the dict's order is from biggest bill to smallest bill
    denos = {
        '$100 bill': 100,
        '$50 bill': 50,
        '$20 bill': 20,
        '$10 bill': 10,
        '$5 bill': 5,
        '$1 bill': 1,
        'quarter': 0.25,
        'dime': 0.10,
        'nickel': 0.05,
        'penny': 0.01
    }

    #initialize the answer
    answer = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "

    #some edge or special cases, like you dont pay or pay is less than the cost, also when exact pay w/o any change needed
    if change < 0:
        answer += 'Please pay with enough amount!'
    elif change == 0:
        answer += 'No changes needed!'
    
    #when change > 0, compare the change through the denos dict
    elif change > 0:
        for deno_string in denos:
            #how many times to pay for each deno_string
            times = int(change//denos[deno_string])
            # if deno_string is penny and plural
            if times > 1 and deno_string == 'penny': 
                answer += f"and {times} pennies."
            # if deno_string is penny and singular
            elif times == 1 and deno_string == 'penny': 
                answer += f"and 1 penny."
            # if deno_string is else and plural
            elif times > 1:
                answer += f"{times} {deno_string}s, "
            # if deno_string is else and singular
            elif times ==1:
                answer += f"1 {deno_string}, "
            
            #update change
            change -= times * denos[deno_string] 
            #in debug mode, found some defect could happen to make change like 0.019999, so round here to get correct times
            change = round(change, 2)
        #when change happens, replace the last punctuation with "."
        if answer[-2] == ",": # if the 2nd last punctuation is ","
            answer = answer[:-2]+"." # replace the last 2 chars with a "."
        
    return answer
#print(optimal_change(30, 100)) 
