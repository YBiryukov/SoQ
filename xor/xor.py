from random import choice


def answer_selected_questions(data, selected_questions):
    """ answer selected questions """
    answers = []
    for arg in data["args"]:
        for question in selected_questions:
            answer = question["fun"](arg, question["fun_args"])
            answers.append(answer)
    return answers

def assign_next_questions(next_questions, question_index, answers_amount):
    """ assign next questions to categorizer, assign category to each last question """
    question_index += 1
    if question_index < answers_amount:
        next_questions["true"] = {
            "next_questions": {}
        }
        next_questions["false"] = {
            "next_questions": {}
        }
        assign_next_questions(next_questions["true"]["next_questions"], question_index, answers_amount)
        assign_next_questions(next_questions["false"]["next_questions"], question_index, answers_amount)
    else:
        next_questions["true"] = {
            "next_questions": None,
            "category": choice(possible_categories)
        }
        next_questions["false"] = {
            "next_questions": None,
            "category": choice(possible_categories)
        }

def categorize(categorizer, answer_index, answers):
    """ categorize answers """
    if answers[answer_index] == True:
        current_question = categorizer["true"]
    elif answers[answer_index] == False:
        current_question = categorizer["false"]
    if current_question["next_questions"] != None:
        answer_index += 1
        return categorize(current_question["next_questions"], answer_index, answers)
    else:
        return current_question["category"]

def create_categorizer(possible_categories, answers_amount):
    """ create categorizer """
    categorizer = {}
    assign_next_questions(categorizer, 0, answers_amount)
    return categorizer

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

def select_questions(possible_questions):
    """ get list of questions selected from possible questions """
    selected_questions = []
    for i in range(questions_amount):
        selected_questions.append(choice(possible_questions))
    return selected_questions


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


args_amount = 2
questions_amount = 1
answers_amount = args_amount * questions_amount

for i in range(1000):
    selected_questions = select_questions(possible_questions)
    for question in selected_questions:
        print(question)
    categorizer = create_categorizer(possible_categories, answers_amount)
    print(categorizer)

    print("train results start")
    results_correct = True
    for data in train:
        answers = answer_selected_questions(data, selected_questions)
        print(answers)
        categorization_result = categorize(categorizer, 0, answers)
        print(f'correct_answer: {data["correct_answer"]}, categorization_result: {categorization_result}')
        if data["correct_answer"] != categorization_result:
            results_correct = False
    print("train results end")
    print(i)
    if results_correct == True:
        break

print("test results start")
for data in test:
    answers = answer_selected_questions(data, selected_questions)
    categorization_result = categorize(categorizer, 0, answers)
    print(f'correct_answer: {data["correct_answer"]}, categorization_result: {categorization_result}')
print("test results end")
