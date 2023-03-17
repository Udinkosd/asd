from prettytable import PrettyTable
import os
os.system("cls")

class LinkedList:
    def __init__(self, exercise_number, exercise_type, duration, calories):
        self.exercise_number = exercise_number
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories = calories
        self.next = None

class FitnessTracker:
    def __init__(self):
        self.head = None

    def add_exercise(self, exercise_number, exercise_type, duration, calories):
        new_node = LinkedList(exercise_number, exercise_type, duration, calories)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def show_exercise(self):
        current = self.head
        if current != None:
            current.exercise_number
            print('Exercise Type:', current.exercise_type)
            print('Duration:', current.duration, 'minutes')
            estimation = current.calories * current.duration
            print('Calories Burned Estimation:', estimation, 'calories')
            my_exercise = {1:['Jumping jacks', 4, 10], 
                        2:['Toy soldiers', 5, 5], 
                        3:['Backward lunge', 6, 10]}
            my_exercise[current.exercise_number] = [current.exercise_type, current.calories, current.duration]
            my_training = PrettyTable()
            my_training.title = 'My Training'
            my_training.field_names = ['No', 'Exercise', 'Burned Calories Estimation']
            for k, v in my_exercise.items():
                my_training.add_row([k,v[0],v[1]])
            print(my_training)
        else:
            my_exercise = {1:['Jumping jacks', 4, 10], 
                        2:['Toy soldiers', 5, 5], 
                        3:['Backward lunge', 6, 10]}
            my_training = PrettyTable()
            my_training.title = 'My Training'
            my_training.field_names = ['No', 'Exercise', 'Burned Calories Estimation per minutes']
            for k, v in my_exercise.items():
                my_training.add_row([k,v[0],v[1]])
            print(my_training)
            return my_exercise

    def table(self):
        available_exercise = {4:['Straight-arm Plank',4], 
                              5:['Standing Bicycle Crunches',5], 
                              6:['High Stepping',6]}
        exercise_table = PrettyTable()
        exercise_table.title = 'Available Exercise'
        exercise_table.field_names = ['No','Exercise', 'Burned Calories Estimation per minutes']
        exercise_table.align = 'l'
        for k, v in available_exercise.items():
            exercise_table.add_row([k,v[0],v[1]])
        return available_exercise, exercise_table
    
    def beginner(self):
        beginner_day = {'DAY 1':{'Mountain climber':30, 'Squats':'15x', 'High stepping':16, 'Push-ups':'5x', 'Reverse Crunches':'16x', 
                        'Plank':15, 'Cobra strect':30},
                        'DAY 2':{'Mountain climber':30, 'Triceps dips':'16x', 'Jumping jacks':30, 'Long arm crunches':'16x', 
                        'Bicycle crunches':'16x', 'Plank':15, 'Cobra strect':30}}
        training_table = PrettyTable()
        training_table.title = 'Beginner Training'
        training_table.field_names = ['DAY']
        training_table.align = 'c'
        for k, v in beginner_day.items():
            training_table.add_row([k])
        print(training_table)

def menu():
    node = FitnessTracker()
    os.system("cls")
    available_exercise, exercise_table = node.table()
    my_exercise = node.show_exercise()

    def delete():
        print(my_exercise)
        input_choice = int(input('Select / Input which one you want to delete: '))
        if input_choice in my_exercise:
            del my_exercise[input_choice]
            print("Exercise deleted successfully!")
        else:
            print('Error! exercise already deleted or does not exist')
        add_new()

    def add_new():
        while True:
            input_choice = str(input('Press enter to continue or "+" to add new exercise and "-" to delete existed exercise '))
            if input_choice == '+':
                print(exercise_table)
                new_exercise = int(input('Insert new exercise: '))
                for k, v in available_exercise.items():
                    if new_exercise == k:
                        new_duration = float(input('Insert exercise duration (in minutes): '))
                        new_calories = v[1]
                        print()
                        os.system("cls")
                        print(f"You added '{v[0]}' exercise with an estimated {v[1]} calories burned per minutes.")
                        print()
                        node.add_exercise(k, v[0], new_duration, new_calories)
                        node.show_exercise()
                        menu()
                else:
                    print('Invalid exercise, please choose from the available exercise list.')
            elif input_choice == '-':
                delete()
            else:
                menu()

    print()
    print('30 DAYS FITNESS PLAN')
    print('================')
    print('[1]. BEGINNER')
    print('[2]. MY TRAINING')
    input_number = int(input('Select: '))
    if input_number == 1:
        node.beginner()
    elif input_number == 2:
        node.show_exercise()
        add_new()
    else:
        print('Error! choice isnt available!')
        
menu()
