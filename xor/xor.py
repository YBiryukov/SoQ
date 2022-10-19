from random import choice


def is_it_one(one, fun_args):
    """ is the first argument equals 1? """
    if one == 1:
        return True
    else:
        return False

def is_it_two(two, fun_args):
    """ is the first argument equals 2? """
    if two == 2:
        return True
    else:
        return False

def is_it_zero(zero, fun_args):
    """ is the first argument equals 0? """
    if zero == 0:
        return True
    else:
        return False


possible_questions = [
    {
        "name": "is_it_one",
        "fun": is_it_one,
        "fun_args": {

        }
    },
    {
        "name": "is_it_two",
        "fun": is_it_two,
        "fun_args": {

        }
    },
    {
        "name": "is_it_zero",
        "fun": is_it_zero,
        "fun_args": {

        }
    }
]

possible_categories = [
    0,
    1
]

train = [
    {
        "args": [0, 0],
        "correct_answer": 0
    },
    {
        "args": [0, 1],
        "correct_answer": 1
    },
    {
        "args": [1, 0],
        "correct_answer": 1
    },
    {
        "args": [1, 1],
        "correct_answer": 0
    }
]

test = [
    {
        "args": [0, 0],
        "correct_answer": 0
    },
    {
        "args": [0, 1],
        "correct_answer": 1
    },
    {
        "args": [1, 0],
        "correct_answer": 1
    },
    {
        "args": [1, 1],
        "correct_answer": 0
    }
]


selected_questions = select_questions(possible_questions)
categorizer = create_categorizer(possible_categories, selected_questions)

print("train results start")
for data in train:
    answers = answer_selected_questions(data, selected_questions)
    categorization_result = categorize(categorizer, answers)
    print(f'correct_answer: {data["correct_answer"]}, categorization_result: {categorization_result}')
print("train results end")

print("test results start")
for data in test:
    answers = answer_selected_questions(data, selected_questions)
    categorization_result = categorize(categorizer, answers)
    print(f'correct_answer: {data["correct_answer"]}, categorization_result: {categorization_result}')
print("test results end")


# print(choice([True, False]))
# print(list(map(lambda q : q["name"], questions)))
