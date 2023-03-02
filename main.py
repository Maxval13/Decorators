from task1 import test_1
from task2 import test_2
from task3 import finepeople
import csv

if __name__ == '__main__':
    test_1()
    test_2()

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        new_list = finepeople()
        datawriter.writerows(new_list)

