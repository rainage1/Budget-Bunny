from datetime import datetime 
from depositMoney import chequingDeposit, savingDeposit
from transferMoney import chequingToSaving, savingToChequing
from financialTips import randomTip
import menu

def findRow(username):
  row = -1
  for i in range(len(fields)):
    if str(username) == fields[i][0]:
      row = i
  return row

#Prints opening page
print("\n{:^32}\n---------------------------------".format("BUDGETBUNNY"))
command = input("{:<19}->  Press \"R\"\n{:<19}->  Press \"S\"\n".format("Register", "Sign in"))
while True:
  if command.lower().strip() != 'r' and command.lower().strip() != 's':
    print("---------Invalid Input!----------")
    command = input("{:<19}->  Press \"R\"\n{:<19}->  Press \"S\"\n".format("Register", "Sign In"))
  else:
    break

fields = []
userExists = False
passwordExists = False

#Reading data from files and storing in fields as nested lists (every row of data is a list)
dataFile = open('clients.txt','r+')
linesList = dataFile.readlines()
dataFile.close()
for element in range (1,len(linesList)):
  fields.append(linesList[element].split(' '))

#If the user chooses to signin, this checks to make sure the username exists in the data file
if command.lower().strip() == "s":
  while True:
    username = input("Enter username: ")
    if findRow(username) > -1:
      row = findRow(username)
      break
    else:  
      print("Invalid username.")

  #Checks if password exists with that username
  while not passwordExists:
    password = input("Enter password: ")
    if password == fields[row][1]:
      passwordExists = True
    if not passwordExists:
      print("Invalid password.")

#If user wants to register as a new user, following code asks for their information and writes it all to the data file
elif command.lower().strip() == "r":
  print("\nWelcome new client!")
  dataFile = open('clients.txt','a+')
  username = input("Create a username: ")
  for i in range(0, len(fields)):
    if username == fields[i][0]:
      username = input("That username already exists. Choose another username: ")
  password = input("Create a password: ")
  for i in range(0, len(fields)):
    if password == fields[i][1]:
      password = input("That password already exists. Choose another password: ")
  bankAccount = input("Enter a bank account number: ")
  for i in range(0, len(fields)):
    if password == fields[i][6]:
      bankAccount = input("That bank account number already exists. Choose another number: ")
  while not bankAccount.isnumeric():
    if not bankAccount.isnumeric():
      bankAccount = input("Your bank account number can't have any letters. Enter a bank account number: ")
  #Writes username, password, goal balance, year, month, day, bank account number, savings account balance, and chequing account balance to file
  new = username + ' ' + password + ' none 0 0 0 ' + bankAccount + ' 0 0 0 0 DNE\n'
  fields.append(new.split())
  print(fields)
  dataFile.write(new)
  dataFile.close()
  row = findRow(username)

command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)
while command.lower().strip() != 'l':
  #If command is to set new monetary goal
  if command.lower().strip() == 'm':
    #Checks if a current goal exists by seeing if the balance in the data file is "none" or a total amount
    if fields[row][2].isnumeric(): 
      print("\nYou already have an ongoing goal with ${:s} saved after {:s} day(s)".format(fields[row][2], str(datetime.now().day - int(fields[row][5])+1)))
      confirm = input("Would you like to overwrite your current goal? (Y/N): ")
    else:
      confirm = input("You currently don't have a money management plan. Would you like to create a new goal? (Y/N): ")
    if confirm.lower().strip() == "n":
      command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)
    elif confirm.lower().strip() == "y":
      #Prompts user to enter desired savings amount in a giventime period
      totalSaving = input("\nHow much money would you like to save (numeric value): ")
      totalDays = input("How many days do you plan to take to save the desired amount: ")
      #Determines how much money the client should set aside each day
      savingPerDay = round(int(totalSaving)/int(totalDays),2)
        
      fields[row][2] = totalSaving
      fields[row][3] = str(datetime.now().year)
      fields[row][4] = str(datetime.now().month)
      fields[row][5] = str(datetime.now().day)
      fields[row][9] = '0'
      fields[row][10] = totalDays
      fields[row][11] = str(datetime.now().day + 1) + "\n"

      dataFile = open('clients.txt','w')
      clientList = 'Username | Password | Goal Balance | Year | Month | Day | Bank Number | Savings Balance | Chequing Balance | Money Towards Goal | Goal Days | Last Plan Deposit Day\n'
      for r in range (len(fields)):
        for column in range(12):
          #if row == len(fields)-1 and column == 0:
            #clientList+= '\n'+ fields[row][column] + ' '
          if column != 11:
            clientList += fields[r][column] + ' '
          else:
            clientList+= fields[r][column]
      dataFile.write(clientList)
      dataFile.close()
      command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)
  
  elif command.lower().strip() == 'c':
    if fields[row][2].isalpha():
      print("You currently don't have a money management plan. Set a monetary goal from the main menu to start a plan.")
    else:
      print("_________________________________________________________________\nHello! Today is day", str(datetime.now().day - int(fields[row][5])+1) , "of your money management plan.\nIt is recommended that you deposit ${:.2f} into your saving account today.\n_________________________________________________________________".format(((int(fields[row][2]) - int(fields[row][9])))/(int(fields[row][10]) - (datetime.now().day - int(fields[row][5])))))
      command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)    

  elif command.lower().strip() == 'd':
    #print("It is recommended that you deposit $" + str(savingPerDay), "into your saving account today.")
    bankAccount = input("\nEnter your bank account number: ")
    while str(bankAccount) != fields[row][6]:
      bankAccount = input("Invalid bank number. Enter your bank account number: ")
    depositAccount = input("Deposit into chequing       -> Press \"C\"\nDeposit into saving         -> Press \"S\"\nQuit                        -> Press \"Q\"\n")
    depositAmount = input("Enter deposit amount:           ")

    if depositAccount.lower().strip() != 'q':
      if depositAccount.lower().strip() == 'c':
        chequingDeposit(depositAmount, row, fields)

      elif depositAccount.lower().strip() == 's':
        savingDeposit(depositAmount, row, fields)

    randomTip()
    command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)

  elif command.lower().strip() == 't':

    bankAccount = input("\nEnter your bank account number: ")
    while str(bankAccount) != fields[row][6]:
      bankAccount = input("Invalid bank number. Enter your bank account number: ")
    transferAccount = input("Transfer from chequing      -> Press \"C\"\nTransfer from saving        -> Press \"S\"\nQuit                        -> Press \"Q\"\n")
    if transferAccount.lower().strip() == 'c' or transferAccount.lower().strip() == 's':
      transferAmount = input("Enter the amount of money you are transfering: ")

      if transferAccount.lower().strip() == 'c':
        chequingToSaving(transferAmount,row,fields)
    
      elif transferAccount.lower().strip() == 's':
        savingToChequing(transferAmount,row,fields)
      randomTip()
      command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)

    elif transferAccount.lower().strip() == 'q':
      randomTip()
      command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)
    else:
      next = input("That is not a valid command. Press ENTER to the main menu. ")
      command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)
    

  else:
    print("\nThat is not a valid command. Try again.\n")
    command = menu.menuDisplay(fields[row][8],fields[row][7],fields[row][2], fields, row)
    
if command.lower().strip() == 'l':  
  print("Successfully logged out.")
