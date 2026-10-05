import pickle
with open("marks.dat", "rb") as f:
    found = False
    try:
        while True:
            record = pickle.load(f)

            if record[0] == 20:
                print("Record:", record)
                found = True
                break
    except EOFError:
        pass
    if found == False:
        print("Roll no. not found")

2. write a program on searching

import pickle
import os

def delete_record():
    rollno = int(input("Enter roll no. to delete: "))
    found = False

    try:
        with open("student.dat", "rb") as f, open("temp.dat", "wb") as temp:

            try:
                while True:
                    rec = pickle.load(f)

                    if rec[0] == rollno:
                        found = True
                    else:
                        pickle.dump(rec, temp)

            except EOFError:
                pass

        if found:
            os.replace("temp.dat", "student.dat")
            print("Record deleted successfully")
        else:
            os.remove("temp.dat")
            print("Record not found")

    except FileNotFoundError:
        print("File not found")

delete_record()import pickle
with open("marks.dat", "rb") as f:
    found = False
    try:
        while True:
            record = pickle.load(f)

            if record[0] == 20:
                print("Record:", record)
                found = True
                break
    except EOFError:
        pass
    if found == False:
        print("Roll no. not found")

2. write a program on searching

import pickle
import os

def delete_record():
    rollno = int(input("Enter roll no. to delete: "))
    found = False

    try:
        with open("student.dat", "rb") as f, open("temp.dat", "wb") as temp:

            try:
                while True:
                    rec = pickle.load(f)

                    if rec[0] == rollno:
                        found = True
                    else:
                        pickle.dump(rec, temp)

            except EOFError:
                pass

        if found:
            os.replace("temp.dat", "student.dat")
            print("Record deleted successfully")
        else:
            os.remove("temp.dat")
            print("Record not found")

    except FileNotFoundError:
        print("File not found")

delete_record()import pickle
with open("marks.dat", "rb") as f:
    found = False
    try:
        while True:
            record = pickle.load(f)

            if record[0] == 20:
                print("Record:", record)
                found = True
                break
    except EOFError:
        pass
    if found == False:
        print("Roll no. not found")

2. write a program on searching

import pickle
import os

def delete_record():
    rollno = int(input("Enter roll no. to delete: "))
    found = False

    try:
        with open("student.dat", "rb") as f, open("temp.dat", "wb") as temp:

            try:
                while True:
                    rec = pickle.load(f)

                    if rec[0] == rollno:
                        found = True
                    else:
                        pickle.dump(rec, temp)

            except EOFError:
                pass

        if found:
            os.replace("temp.dat", "student.dat")
            print("Record deleted successfully")
        else:
            os.remove("temp.dat")
            print("Record not found")

    except FileNotFoundError:
        print("File not found")

delete_record()
