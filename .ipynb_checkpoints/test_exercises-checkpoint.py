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
        print("Slice in b_b incorrect.")
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






