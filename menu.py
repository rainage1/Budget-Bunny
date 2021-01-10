from datetime import datetime 

def menuDisplay(chequingBalance,savingBalance,monetaryGoal, fields, row):
    
    
    print("\n{:^33}\n---------------------------------".format("Menu:"))
    if fields[row][2].isnumeric():  
      if datetime.now().day - int(fields[row][11].strip()) > 1:
        print("You forgot to deposit money yesterday into your money management plan!\nDon't worry though. We adjusted the plan and recalculated the amount you should deposit per day for you.\nIt is recommended that you deposit ${:.2f} into your saving account today.\n\n".format(((int(fields[row][2]) - int(fields[row][9])))/(int(fields[row][10]) - (datetime.now().day - int(fields[row][5])))))
      elif datetime.now().day - int(fields[row][11].strip()) == 1 or datetime.now().day - int(fields[row][11].strip()) == -1:
        print("Dont forget to deposit ${:.2f} into your saving account today!\n\n".format(((int(fields[row][2]) - int(fields[row][9])))/(int(fields[row][10]) - (datetime.now().day - int(fields[row][5])))))
      elif datetime.now().day - int(fields[row][11].strip()) == 0:
        print("Great job! You deposited money into your savings account and are steadily reaching your money management goal.\n\n")
    else:
      print("You haven't set a money management plan yet.\n\n")

    print("Chequing Balance:      $" + chequingBalance )
    print("Savings Balance:       $" + savingBalance )
    if monetaryGoal == 'none':
      print('Monetary Goal:         DNE')
    else:
      print("Monetary Goal:         $" + monetaryGoal)
    print()
    return input("{:<19}->  Press \"M\"\n{:<19}->  Press \"C\"\n{:<19}->  Press \"D\"\n{:<19}->  Press \"T\"\n{:<19}->  Press \"L\"\n".format("Set monetary goal", "Check current goal", "Deposit Money", "Transfer Funds", "Log out"))
