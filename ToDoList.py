# ------------------------------------------------------------------------ #
# Title: ToDoList
# Description: When this program starts, it loads each row of data
#              from "ToDoList.txt" into a dictionary item, then into a list table.
#              Allows the user to add new rows into the table, and save them into the .txt file.
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Zeb W, 14Nov2021, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
strFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = '''=================================== 
 1) Show current data
 2) Add a new item.
 3) Remove an existing item.
 4) Save Data to File
 5) Exit Program
  ===================================
  '''   # A menu of user options

# -- Processing -- #
# Step 1 - When the program starts, load data from .txt file into dicRow, then into lstTable
objFile = open(strFile, "r")
for row in objFile:
    p, t = row.split(",")
    dicRow = {"Priority":p, "Task":t}
    lstTable.append(dicRow)

# -- Input/Output -- #
# Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

# 1 - Show the current items in the table
    if strChoice.strip() == '1':
        # for dicRow in lstTable:
        #     print(dicRow["Priority"] + ": " + dicRow["Task"].strip())
        for row in lstTable:
            print(row["Priority"], row["Task"].strip(), sep=": ")
        print()

# 2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        while True:
            strPriority = input("Task Priority: ")
            strTask = input("Task Name: " )
            lstTable.append({"Priority": strPriority, "Task": strTask +"\n"})
            strChoice = input("Exit? Y/N: ")
            print()
            if strChoice.lower() == "y": break
            elif strChoice.lower() == "n": continue
            else:
                strChoice = input("Please enter either Y or N: ")
            print()

# 3 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        for row in lstTable:
            print(row['Priority'], row['Task'].strip(), sep=': ')
        print()
        strChoice = str(input('Which # would you like to remove? '))
        print()
        popItem = lstTable.pop(int(strChoice))
        print(popItem['Priority'] + ": " + popItem['Task'].strip() + " has been removed")
        print()
        continue

# 4 - Save tasks to the ToDoToDoList.txt file
    if strChoice.strip() == "4":
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Priority"]) + "," + str(row["Task"]))
        objFile.close()
        print("ToDoList.txt has been updated!")
        print()

# 5 - Exit program
    elif strChoice.strip() == '5': break