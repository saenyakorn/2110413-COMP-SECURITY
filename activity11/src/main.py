from essential_generators import DocumentGenerator
from essential_generators import MarkovTextGenerator
from essential_generators import MarkovWordGenerator
import clean_text
import manage_result
import os
from time import time
import readchar
import sys
import numpy as np


def clear(): return os.system('cls')


help_information = \
    """
help\t- show this help
exit\t- exit the program
store\t- store the result
load\t- load the result
remove\t- remove the result file
clear\t- clear the result
gen\t- generate text
create\t- create a new user
"""

if __name__ == '__main__':
    gen = DocumentGenerator(text_generator=MarkovTextGenerator(),
                            word_generator=MarkovWordGenerator())
    result = None

    while True:
        try:
            clear()
            print("State: ", result)
            cmd = input('Enter a command (type "help" for explaination): ')
            if cmd == "exit":
                if result != None:
                    ck = input(
                        "Digraph already in memory, are you sure you want to exit? (y/n): ")
                    if ck == "y":
                        break
                    else:
                        continue
                break

            elif cmd == "help":
                print(help_information)
                print("Press any key to continue...")
                readchar.readchar()

            elif cmd == "store":
                if result == None:
                    print("No result to store, please load or create dict first")
                    print("Press any key to continue...")
                    readchar.readchar()
                    continue
                name = input("Enter a name: ")
                manage_result.store_result(result, name)
                result = None

            elif cmd == "load":
                if result != None:
                    ck = input(
                        "Digraph already in memory, are you sure you want to load? (y/n): ")
                    if ck == "y":
                        name = input("Enter a name: ")
                        result = manage_result.load_result(name)
                        print("Loaded result")
                    else:
                        print("Cancelled")

                    print("Press any key to continue...")
                    readchar.readchar()
                name = input("Enter a name: ")
                result = manage_result.load_result(name)

            elif cmd == "remove":
                name = input("Enter a name: ")
                ck = input("Are you sure to remove? (y/n): ")
                if ck == "y":
                    manage_result.remove_result(name)
                    print("Removed")
                else:
                    print("Cancelled")
                print("Press any key to continue...")
                readchar.readchar()

            elif cmd == "clear":
                ck = input("Are you sure to clear? (y/n): ")
                if ck == "y":
                    result = None
                else:
                    print("Cancelled")
                    print("Press any key to continue...")
                    readchar.readchar()

            elif cmd == "gen":
                if result == None:
                    print("Please load or create dict first")
                    print("Press any key to continue...")
                    readchar.readchar()
                    continue

                sentence = gen.sentence()
                clean_sentence = clean_text.clean_text(sentence)
                print("Type the follwing sentence")
                print(clean_sentence)

                t1 = time()
                prev_char = None
                buffer = []
                sub_result = []
                while True:

                    # TODO: fix stdout of this line
                    print("".join(buffer), end="\r")

                    typed_char = readchar.readchar()
                    t2 = time()
                    if typed_char == "\r" or ord(typed_char) == 10:
                        break
                    elif typed_char == "\b":
                        if len(buffer) >= 1:
                            buffer.pop()
                            if len(sub_result) >= 1:
                                sub_result.pop()

                            prev_char = None
                    else:
                        buffer.append(typed_char)
                        if prev_char != None:
                            sub_result.append((prev_char+typed_char, t2-t1))
                        prev_char = typed_char

                    t1 = t2

                for k, v in sub_result:
                    if k not in result:
                        result[k] = (v, 1)
                    else:
                        result[k] = ((result[k][0]*result[k][1] + v) /
                                     (result[k][1]+1), result[k][1]+1)

            elif cmd == "create":
                if result != None:
                    ck = input(
                        "Digraph already in memory, are you sure you want to create? (y/n)")
                    if ck == "y":
                        result = {}
                    else:
                        print("Cancelled")
                        continue
                result = {}

            elif cmd == "identify":
                sentence = gen.sentence()
                clean_sentence = clean_text.clean_text(sentence)
                print("Type the follwing sentence")
                print(clean_sentence)

                t1 = time()
                prev_char = None
                buffer = []
                unk_sub_result = []
                while True:

                    # TODO: fix stdout of this line
                    print("".join(buffer), end="\r")

                    typed_char = readchar.readchar()
                    t2 = time()
                    if typed_char == "\r" or ord(typed_char) == 10:
                        break
                    elif typed_char == "\b":
                        if len(buffer) >= 1:
                            buffer.pop()
                            if len(unk_sub_result) >= 1:
                                unk_sub_result.pop()

                            prev_char = None
                    else:
                        buffer.append(typed_char)
                        if prev_char != None:
                            unk_sub_result.append((prev_char+typed_char, t2-t1))
                        prev_char = typed_char

                    t1 = t2
                
                # print(unk_sub_result)
                # readchar.readchar()
                
                unk_result = {}
                for k, v in unk_sub_result:
                    if k not in unk_result:
                        unk_result[k] = (v, 1)
                    else:
                        unk_result[k] = ((unk_result[k][0]*unk_result[k][1] + v) /
                                     (unk_result[k][1]+1), unk_result[k][1]+1)
                        
                # print(unk_result)
                # readchar.readchar()
                        
                # TODO: identify the user (loop over all user in database -> assume we have 2 users in database)
                ree_result = manage_result.load_result("ree")
                yu_result = manage_result.load_result("yu")
                user_results = [ree_result, yu_result]
                # We define the most similar user as the user with the smallest distance
                user_score = [0]*len(user_results)
                for idx, result in enumerate(user_results):
                    # Get distance for all typing pattern
                    for k, v in unk_result:
                        if k in result:
                            user_score[idx] += abs(result[k][0] - v[0])
                
                # Get min score
                pos = np.argmin(user_score)
                if pos == 0:
                    print("\nYou are ree")
                else:
                    print("\nYou are yu")
                
                result = None
                readchar.readchar()
                pass

            elif cmd == "authenticate":
                name = input("Enter a name: ")
                result = manage_result.load_result(name)

                sentence = gen.sentence()
                clean_sentence = clean_text.clean_text(sentence)
                print("Type the follwing sentence")
                print(clean_sentence)

                t1 = time()
                prev_char = None
                buffer = []
                unk_sub_result = []
                while True:

                    # TODO: fix stdout of this line
                    print("".join(buffer), end="\r")

                    typed_char = readchar.readchar()
                    t2 = time()
                    if typed_char == "\r":
                        break
                    elif typed_char == "\b":
                        if len(buffer) >= 1:
                            buffer.pop()
                            if len(unk_sub_result) >= 1:
                                unk_sub_result.pop()

                            prev_char = None
                    else:
                        buffer.append(typed_char)
                        if prev_char != None:
                            unk_sub_result.append((prev_char+typed_char, t2-t1))
                        prev_char = typed_char

                    t1 = t2
                
                unk_result = {}
                for k, v in unk_sub_result:
                    if k not in unk_result:
                        unk_result[k] = (v, 1)
                    else:
                        unk_result[k] = ((unk_result[k][0]*unk_result[k][1] + v) /
                                     (unk_result[k][1]+1), unk_result[k][1]+1)

                print()
                # TODO: compare similarity between result and unk_result
                user_score = 0
                cnt = 0
                for k in unk_result:
                    v = unk_result[k]
                    if k in result:
                        cnt += 1
                        user_score += abs(result[k][0] - v[0])
                threshold = 0.13
                user_th = user_score/cnt
                print("Score:", user_th)
                if user_th < threshold:
                    print("Authentication successful")
                
                result = None
                readchar.readchar()
                pass

        except KeyboardInterrupt:
            continue
