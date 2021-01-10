def chequingDeposit(depositAmount, rowNum, fields):
  accountFile = open('clients.txt','r')
  accountFile.close()
  
  chequingAmount = int(fields[rowNum][8])+int(depositAmount)
  fields[rowNum][8] = str(chequingAmount)
    
  accountFile = open('clients.txt','w')

  clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days\n'
  
  for row in range (len(fields)):
    for column in range(11):
      if column != 10:
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
    print("You deposited ${} into your savings account and only need ${} to reach your money management goal!".format(depositAmount, int(fields[rowNum][2]) - int(fields[rowNum][9])))
    
  accountFile = open('clients.txt','w')

  clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days\n'
  for row in range (len(fields)):
    for column in range(11):
      if column != 10:
        clientList += fields[row][column] + ' '
      else:
        clientList+= fields[row][column]
  accountFile.write(clientList)
  accountFile.close()
