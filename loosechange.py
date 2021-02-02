def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    int_cents = int (cents)
    if int_cents <=0:
        return change_dict
    else:
        if int_cents//25 > 0:
            change_dict["Quarters"] = int_cents//25
            int_cents = int_cents%25
        if int_cents//10 > 0:
            change_dict["Dimes"] = int_cents//10
            int_cents = int_cents%10
        if int_cents//5 > 0:
            change_dict["Nickels"] = int_cents//5
            int_cents = int_cents%5
        if int_cents//1 > 0:
            change_dict["Pennies"] = int_cents//1
        return change_dict
