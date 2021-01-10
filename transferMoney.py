from datetime import datetime 

def chequingToSaving(transferAmount,rowNum,fields):

  if int(fields[rowNum][8])-int(transferAmount) >= 0:
    savingAmount = int(fields[rowNum][7])+int(transferAmount)
    fields[rowNum][7] = str(savingAmount)
    chequingAmount = int(fields[rowNum][8])-int(transferAmount)
    fields[rowNum][8] = str(chequingAmount)
    goalProgress = str(int(transferAmount)+int(fields[rowNum][9]))
    fields[rowNum][9] = goalProgress
    fields[rowNum][11] = str(datetime.now().day) + "\n"
    print("You transferred ${} into your savings account and only need ${} to reach your money management goal!".format(transferAmount, int(fields[rowNum][2]) - int(fields[rowNum][9])))


    accountFile = open('clients.txt','w')

    clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days | Last Plan Deposit Date\n'
    
    for row in range (len(fields)):
      for column in range(12):
        if column != 11:
          clientList += fields[row][column] + ' '
        else:
          clientList+= fields[row][column]
    accountFile.write(clientList)
  else:
    print("You do not have enough money to make the transfer.")

  


def savingToChequing(transferAmount,rowNum,fields):
  if int(fields[rowNum][7])-int(transferAmount) >= 0:  
    
    savingAmount = int(fields[rowNum][7])-int(transferAmount)
    fields[rowNum][7] = str(savingAmount)
    
    chequingAmount = int(fields[rowNum][8])+int(transferAmount)
    fields[rowNum][8] = str(chequingAmount)
      
    accountFile = open('clients.txt','w')

    clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days | Last Plan Deposit Date\n'
    
    for row in range (len(fields)):
      for column in range(12):
        if column != 11:
          clientList += fields[row][column] + ' '
        else:
          clientList+= fields[row][column]

    accountFile.write(clientList)
  else:
    print("You do not have enough money to make the transfer.")
