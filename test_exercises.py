def test_1(num, ls, length, exercises):
    correct = True

    if num == 0:
        check = ['p', 'y', 't', 'h', 'o', 'n']
        ls = [l.lower() for l in ls]
    if num == 1:
        check = [4, 1, 3, 5, 2, 10, 2]
    if num == 2:
        check = [5, 2, 'a', 'python', 3.2, [3, 2, 'd', 1.2]]
    if num == 3:
        if len(ls) == 6:
            print("Length of list correct.")
            exercises[3] = True
            print(f'\nProgress:\n{list(exercises.values()).count(True)} of {len(exercises)} completed')
            return
    if ls == check:
        print("List correct.")
    else:
        print("Recheck list.")
        correct = False
    if length == len(check):
        print("Length correct.")
    else:
        print("Recheck length.")
        correct = False
    if correct:
        exercises[num] = True
        print("Exercise completed successfully.")
    else:
        exercises[num] = False
    print(f'\nProgress:\n{list(exercises.values()).count(True)} of {len(exercises)} completed')


def test_2(num, exercises, *args):
    correct = True
    if num == 4:
        values = [3, 2, 5, 10, 1]
        for i, arg in enumerate(args):
            if arg != values[i]:
                print(f"Incorrect value in el_{i}")
                correct = False
                break
            print("All values correct.")
    if num == 5:
        values = ['p', 'y', 't', 'h', 'o', 'n']
        args[0] = args[0].lower()
        for i, arg in enumerate(args):
            if arg != values[i]:
                print(f"Incorrect value.")
                correct = False
                break
            print("All values correct.")
    if correct:
        exercises[num] = True
        print("Exercise completed successfully.")
    else:
        exercises[num] = False
    print(f'\nProgress:\n{list(exercises.values()).count(True)} of {len(exercises)} completed')


def test_3_1(num, b, b_a, b_b, exercises):
    correct = True
    if b_a == b[2:4]:
        print("Slice in b_a correct.")
    else:
        print("Slice in b_a incorrect.")
        correct = False
    if b == b_b:
        print("Elements match in b and b_b.")
    else:
        print("Mismatched elements in b and b_b.")
        correct = False
    if id(b) == id(b_b):
        print("b and b_b are the same element. b_b should be a copy.")
        correct = False
    if correct:
        exercises[num] = True
        print("Exercise completed successfully.")
    else:
        exercises[num] = False
    print(f'\nProgress:\n{list(exercises.values()).count(True)} of {len(exercises)} completed')


def test_3_2(num, c, c_a, c_b, c_c, c_sublist, c_sublist_copy, exercises):
    correct = True
    if c_a == c[:3]:
        print("Slice in c_a correct.")
    else:
        print("Slice in c_a incorrect.")
        correct = False
    if c[-3:] == c_b:
        print("Slice in c_b correct.")
    else:
        print("Slice in c_a incorrect.")
        correct = False
    if c_c == c[-1][0]:
        print("Value in c_c correct.")
    else:
        print("Value in c_c incorrect.")
        correct = False
    if id(c_sublist) == id(c[-1]):
        print("c_sublist references to the correct list.")
    else:
        print("c_sublist doesn't reference the correct list.")
    if c[-1][0] == c_sublist_copy:
        print("Elements match in c_sublist and c_sublist_copy. Correct.")
    else:
        print("Mismatched elements in c_sublist and c_sublist_copy. Incorrect")
        correct = False
    if id(c[-1][0]) == id(c_sublist_copy):
        print("c_sublist_copy should be a copy.")
        correct = False
    if correct:
        exercises[num] = True
        print("Exercise completed successfully.")
    else:
        exercises[num] = False
    print(f'\nProgress:\n{list(exercises.values()).count(True)} of {len(exercises)} completed')


def test_3_3(num, c_sublist, c_sublist_copy, exercises):
    correct = True

    if c_sublist == [3, 2, 'd', 1.2, 'new']:
        print("c_sublist correct.")
    else:
        print("c_sublist incorrect.")
        correct = False
    if c_sublist_copy == ['other_change', 3, 2, 'd', 1.2]:
        print("c_sublist_copy correct.")
    else:
        print("c_sublist_copy incorrect.")
        correct = False
    if correct:
        exercises[num] = True
        print("Exercise completed successfully.")
    else:
        exercises[num] = False
    print(f'\nProgress:\n{list(exercises.values()).count(True)} of {len(exercises)} completed')







