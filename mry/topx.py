import pickle
import heapq
import os

# max number of elements in a list
MAX_PER_FILE = 10000

def get_filename(i):
    return "%d.dat" % i

file_number = 0
# function to save pickled data to file
def save_to_file(s):
    global file_number
    file_name = get_filename(file_number)

    with open(file_name, "wb") as file:
        pickle.dump(len(s), file)
        for item in s:
            pickle.dump(item, file)
    file_number += 1

# funtion to load pickled data from file
def load_pickle_file(l):
    file_name = get_filename(l)
    with open(file_name, "rb") as file:
        count = pickle.load(file)
        for _ in range(count):
            yield pickle.load(file)

# function to delete temp pickle file
def delete_pickle_file(d):
    file_name = get_filename(d)
    if file_name:
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print(f"Not found: {file_name}")

int_list = []
# read input file, strip spaces and new lines into lists
with open('datafile','rb') as file:
    for line in file:
        try:
            value = int(line.strip())
            int_list.append(value)
        except ValueError:
            print(f"Non-integer line: {line}")     

        if len(int_list) == MAX_PER_FILE:
            int_list.sort(reverse=True)
            save_to_file(int_list)
            del int_list[:]

if int_list:
    int_list.sort(reverse=True)
    save_to_file(int_list)     

# merge temp pickle files, sort and save to a file
with open('datafile_sorted', 'w') as output_file:
    for x in heapq.merge(*(load_pickle_file(i) for i in range(file_number)),reverse=True):
        output_file.write(str(x)+ '\n')

# delete all temp files
for i in range(file_number):
    delete_pickle_file(i)
