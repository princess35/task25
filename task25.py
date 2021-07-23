''''Libraries'''
import datetime
from datetime import date

'''Global constants variables'''
userdata = {}
string_data = ''

'''Defining functions'''
# Modify the reg_user to make sure that there are no duplicates
def reg_user():
    userFile = open("user.txt", "a")
    Username = input("Create username:")
    while Username in userdata:
        Username = input('''username already exists try again.
        Enter user name: ''')
    Password = input("Create a password:")
    Password1 = input("Confirm a password:")
    if Password == Password1:
        userFile.write(f'\n{Username}, {Password}')
    else:
        print('Correct user details')
    userFile.close()

# add_task will be called when the user selects 'a'
def add_task():
    assigned_to = input("Please enter the person this is assigned to: ")
    task_title = input("Please enter the title of the task:")
    task_description = input("Please enter the description of the task:")
    due_date = input("Please enter the task due date:")
    task_complete = "No"
    date_assigned = date.today()
    userFile = open("tasks.txt", "a", encoding= 'utf-8')
    userFile.write(f'\n{assigned_to}, {task_title}, {task_description}, {date_assigned}, {due_date}, {task_complete}')
    userFile.close()

# Add_task will be called when the user selects 'va'
def view_all():
    userFile = open('tasks.txt', 'r')
    userdata = userFile.readlines()
    for line in userdata:
        assigned_to, task_title, task_description, date_assigned, due_date, task_complete = line.split(", ")
        print(f'Task title:\t{task_title}')
        print(f'assigned_to:\t{assigned_to}')
        print(f'date_assigned:\t{date_assigned}')
        print(f'due_date:\t{due_date}')
        print(f'task_complete:\t{task_complete}')
        print(f'task_description:\t{task_description}')
        userFile.close()

# Add functionality when the user selects "vm"
# Each task is display with corresponding number
def view_mine():
    task_num = 0
    d = {}
    userFile = open('tasks.txt', 'r')
    for line in userFile:
        task_num += 1
        assigned_to, task_title, task_description, date_assigned, due_date, task_complete = line.split(", ")
        d[task_num] = line.strip('\n').split(", ")
        if assigned_to == userName:
            print((f'Task number is: {task_num}'))
            print(f'Task title:\t{task_title}')
            print(f'assigned_to:\t{assigned_to}')
            print(f'date_assigned:\t{date_assigned}')
            print(f'due_date:\t{due_date}')
            print(f'task_complete:\t{task_complete}')
            print(f'task_description:\t{task_description}')
    userFile.close()

    t_numb = int(input(
            '''Please select the task number for a specific task or -1 to return to main menu:'''))

    task = d[t_numb]

    menu1 = input("Enter m to mark the task as complete or e to edit the task")
    if menu1 == 'm':
        task[-1] = 'Yes'
    if menu1 == 'e':
        menu2 = input("Enter eu to edit username or edd to edit due date ")
        if menu2 == 'eu':
            task[0] = input("Enter a new username ")
        if menu2 == 'edd':
            task[-2] = input("Enter a new due date ")
    d[t_numb] = task
    print(d)
    stringdata = ''
    for tk in d.values():
        stringdata += ', '.join(tk) + '\n'
        stringdata += stringdata.strip()
    taskfile = open('tasks.txt', 'w')
    taskfile.write(stringdata)
    taskfile.close()
    print('successfully updated the file')

# If the user decides to generate reports ,text files should output data in a user friendly manner
# Initialise the following variables zero and also initialise datetime
taskfile = ''
userName = 0
complete_task = 0
incomplete_task = 0
incomplete_overdue = 0
overdue = 0
task_count = 0
current_date = datetime.datetime.now()
#duedate = taskfile[-2]
due_date = "d% m% y%"
tot_num_task = 4
#percentage_of_task = (tot_num_task / task_count) * 100
percentage_completed = (complete_task / tot_num_task) * 100
percentage_incomplete = (incomplete_task / tot_num_task) * 100

def generate_tasks():
    if menu == 'gr':
        taskfile = open('tasks.txt', 'r')
        task_count = 0
    for lines in taskfile:
        string_data = lines.strip('\n').split(', ')
        if userName == string_data[0]:
            task_count += 1
            print(f'The total number of tasks that have been generated and tracked using the task25.py are {task_count}')
    if complete_task == 'Yes':
        task_count += 1
        print(f'The total number of completed tasks are {complete_task}')
        if incomplete_task == 'No':
            task_count += 1
        print(f'The total number of uncompleted tasks are {incomplete_task}')
    if 'due_date  > datetime.datetime.now()' and incomplete_task == 'No':
        task_count += 1
        print(f'The total number of tasks that have not been completed and that are overdue are {incomplete_task}, {overdue}')
    if 'datetime.datetime.now() < due_date' == 'Incomplete task':
        task_count += 1
        print(f' The task is incomplete {incomplete_task}')
    if 'datetime.datetime.now() < due_date' == "overdue":
        task_count += 1
        print(f'The percentage of tasks that are overdue {overdue}')

# Initialise the following variables and also initialise datetime
tot_num_task = 4
complete_task = 0
incomplete_task = 0
task_count = 0
current_date = datetime.datetime.now()
percentage_of_tasks = (tot_num_task / tot_num_task) * 100
percentage_completed = (complete_task / tot_num_task) * 100
percentage_incomplete = (incomplete_task / tot_num_task) * 100

userFile = ' '
string_data = ' '
# Loop through the task that will count and add task and confirm if the task is complete or not
userFile = open('tasks.txt', 'r')
for line in userFile:
     task_count += 1
     userFile = line.strip('\n').split(', ')
     complete = line.strip('\n').split(' , ')[-1]
# if userName == string_data[0]:
#     tot_num_task += 1
if complete == "Yes":
    complete_task += 1
else:
    incomplete_task += 1

# Open the file user overview to write in it
task_overview_file = open('task_overview', 'a')
task_overview_file.write(f'The total number of tasks that have been generated and tracked using the task_manager.py are {task_count}')
task_overview_file.write(f'The total number of completed tasks are {complete_task}')
task_overview_file.write(f'The total number of uncompleted tasks are {incomplete_task}')
task_overview_file.write(f'The total number of tasks that have not been completed and that are overdue {incomplete_overdue}')
task_overview_file.write(f'The percentage of tasks that are incomplete {percentage_incomplete}')
task_overview_file.write(f'The percentage of tasks that are overdue {overdue}')
task_overview_file.close()

def user_overview():
    taskfile = open('task.txt', 'r')
    tasklist = taskfile.readlines()
    taskfile.close()
    tot_num_list = len(tasklist)
    userFile = open('user.txt', 'r')
    taskfile.close()

# The task_overview should contain the following information
# Oen the task_overview to write in it
user_overview_file = open('user_overview.txt', 'a')
user_overview_file.write(f'User details {userName}\n')
user_overview_file.write(f'The total number of tasks that have been generated and tracked using the task_manager.py are {tot_num_task}\n')
user_overview_file.write(f'The total number of tasks assigned to the user {tot_num_task}')
user_overview_file.write(f'The percentage of the total number of tasks that have been assigned to the user {percentage_of_tasks}')
user_overview_file.write(f'The percentage of the tasks that have assigned to the user that have been completed{percentage_completed}')
user_overview_file.write(f'The percentage of the tasks assigned to the user that must still be completed {percentage_incomplete}')
user_overview_file.write(f'The percentage of the tasks assigned to the user that have not been completed and are overdue {incomplete_task}, {overdue}')
user_overview_file.close()

# Menu allowing the admin to display statistics in order to read reports generated.
def display_statistics():
    if menu == 'ds':
        userFile = open('user_overview.txt', 'r')
        userFile.close()
        userFile = open('task_overview.txt', 'r')
        userFile.close()

'''Starting main program/ the main program starts here'''
# A program that helps to manage tasks assigned to each member of the team
# Open user.txt to read the information
# Create a for loop, strip the lines than split
userFile = open('user.txt', 'r')
for line in userFile:
    file_username, file_password = line.strip('\n').split(', ')
    userdata[file_username] = file_password

# Request the username and password from the user to check if it is correct using a while loop
userName = input("Enter user name: ")
while not userName in userdata:
    userName = input('''You have entered the wrong username try again.
    Enter user name: ''')
password = input("Enter password:")
while password != userdata[userName]:
    password = input('''You have entered the wrong password try again.
    Enter password: ''')

# Create a menu to display to the user once the login is being successful
# Add an option to generate reports to the main menu of the application.
if userName == 'admin':
    menu = input('''Please select one of the following options:\n r- register user \n a - add task \n va - view all tasks \n vm - view my tasks \n gr - generate reports \n ds- display statistics\n e - exit.''')
else:
    menu = input(
        '''Please select one of the following options: \n a - add task \n va - view all tasks \n vm - view my tasks \n e - exit.''')

# Allow the user to choose specific task or input '-1' to return tp main menu
if menu == "r" and userName == "admin":
    reg_user()
if menu == "a":
    add_task()
if menu == "va":
    view_all()
if menu == "vm":
    view_mine()
if menu == "gr":
    generate_tasks()
if menu == "ds":
    display_statistics()
if menu == 'e':
    exit

