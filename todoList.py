"""
**Project: To-Do List Application with "Completed" List**

**Project Description**: In this project, you will create a to-do list application in Python. The application will allow users to add tasks, view their to-do list, mark tasks as completed, and move completed tasks to a separate list named "completed." You will implement this functionality using Python lists.

**Key Features**:
1. **Add Tasks**: Users should be able to add new tasks to their to-do list.

2. **View Tasks**: Users should be able to view their entire to-do list.

3. **Mark as Completed**: Users should be able to mark a task as completed. When marked as completed, the task should be moved from the to-do list to a separate list named "completed."

4. **Remove Tasks**: Users should be able to remove tasks from their list.

  
**Detailed Question**:

1. Create two empty lists: `to_do_list` to store the tasks and `completed` to store completed tasks.

2. Implement a menu-driven interface that allows users to perform the following actions:
   - **Add a Task**: Users should be able to add a new task to the `to_do_list`. Prompt the user for the task description and add it to the list.

   - **View Tasks**: Users should be able to view their entire to-do list, including the tasks marked as completed. Display each task with an index number.

   - **Mark as Completed**: Users should be able to mark a task as completed. When a task is marked as completed, move it from the `to_do_list` to the `completed` list. Prompt the user for the index number of the task they want to mark as completed.

   - **Remove Task**: Users should be able to remove a task from the `to_do_list`. Prompt the user for the index number of the task to remove and delete it from the list.

   - **Quit**: Allow users to exit the application.

3. Continuously display the menu and perform the chosen action until the user decides to quit.

4. Ensure that your code handles errors gracefully. For example, if a user enters an invalid index number when marking a task as completed or removing a task, display an error message and allow them to try again.

5. As an extra challenge, consider saving and loading both the to-do list and the completed list from text files so that users can retain their lists between sessions.

This modified project enhances the user experience by keeping a separate list for completed tasks, providing a more organized and user-friendly way to manage tasks. It also reinforces Python list manipulation skills.

"""
toDoList = []
completeList = []

def viewTasks():
  if(len(toDoList) == 0 and len(completeList) == 0):
    print("Nothing to view :|")
  else:
    print("To do list:")
    for i in range(0, len(toDoList)):
      print(i+1, ":", toDoList[i])
    print("Completed list:")
    for j in range(0, len(completeList)):
      print(j+1, ":", completeList[j])
  


def addTask(task):
  toDoList.append(task)
  rewrite("Tasks", task)
  

def removeTask(task):
  toDoList.pop(task)

def rewrite(list, task):
  with open("File_IO/txt_files/" + list +".txt", "a") as writer:
    writer.write(task)
    writer.write("\n")
    

def completeTask(task):
  taskToAdd = toDoList[task]
  toDoList.remove(taskToAdd)
  completeList.append(taskToAdd)
  rewrite("completeList", taskToAdd)
  


while(True):
  x = int(input("\nEnter 1 to view tasks \nenter 2 to add a task\nenter 3 to complete a task\nenter 4 to remove a task\nenter -1 to quit:"))
  if(x == -1):
   print("Bye")
   break
  if(x == 1):
    viewTasks()
  if(x == 2):
    task = input("What task do you wanna add?")
    addTask(task)
    rewrite("Tasks", task)
  if(x==3):
    index = int(input("What task do you want to complete(type an index):"))
    if(index>len(toDoList) or index<0):
      print("Try again. Wrong index")
    else:
      completeTask(index-1)
      rewrite("completeList", completeList[index-1])
  if(x == 4):
    index = int(input("What task do you wanna remove(type an index):"))
    if(index>len(toDoList) or index<=0):
      print("Try again. Wrong index")
    else:
      removeTask(index-1)