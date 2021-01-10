def menuDisplay(chequingBalance,savingBalance,monetaryGoal):
    
    
    print("\n{:^33}\n---------------------------------".format("Menu:"))
    print("Chequing Balance:      $" + chequingBalance )
    print("Savings Balance:       $" + savingBalance )
    if monetaryGoal == 'none':
      print('Monetary Goal:         DNE')
    else:
      print("Monetary Goal:         $" + monetaryGoal)
    print()
    return input("{:<19}->  Press \"M\"\n{:<19}->  Press \"C\"\n{:<19}->  Press \"D\"\n{:<19}->  Press \"T\"\n{:<19}->  Press \"L\"\n".format("Set monetary goal", "Check current goal", "Deposit Money", "Transfer Funds", "Log out"))
