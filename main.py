import lab3

task_func_dictionary = {
    "1": lab3.task1,
    "2": lab3.task2,
}
if __name__ == '__main__':
    choice = input("Please, choose the task 1-2 (0-EXIT): ")
    while choice != "0":
        if choice in task_func_dictionary.keys():
          task_func_dictionary.get(choice)()
        else:
          print("Wrong task number!")
        choice = input("Please, choose the task again (0-EXIT): ")