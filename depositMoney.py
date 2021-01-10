from datetime import datetime 

def chequingDeposit(depositAmount, rowNum, fields):
  accountFile = open('clients.txt','r')
  accountFile.close()
  
  chequingAmount = int(fields[rowNum][8])+int(depositAmount)
  fields[rowNum][8] = str(chequingAmount)
    
  accountFile = open('clients.txt','w')

  clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days\n'
  
  for row in range (len(fields)):
    for column in range(12):
      if column != 11:
        clientList += fields[row][column] + ' '
      else:
        clientList+= fields[row][column]
  accountFile.write(clientList)

def savingDeposit(depositAmount, rowNum, fields):
  accountFile = open('clients.txt','r')
  accountFile.close()
  
  savingAmount = int(fields[rowNum][7])+int(depositAmount)
  fields[rowNum][7] = str(savingAmount)
  if fields[rowNum][2].isnumeric():
    goalProgress = str(int(depositAmount)+int(fields[rowNum][9]))
    fields[rowNum][9] = goalProgress
    fields[rowNum][11] = str(datetime.now().day) + "\n"
    print("You deposited ${} into your savings account and only need ${} to reach your money management goal!".format(depositAmount, int(fields[rowNum][2]) - int(fields[rowNum][9])))
    
  accountFile = open('clients.txt','w')

  clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days | Last Plan Deposit Day\n'
  for row in range (len(fields)):
    for column in range(12):
      if column != 11:
        clientList += fields[row][column] + ' '
      else:
        clientList+= fields[row][column]
  accountFile.write(clientList)
  accountFile.close()

