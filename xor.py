def is_it_one(one, other_args):
    """ check if the first argument equals 1 """
    if one == 1:
        return True
    else:
        return False

def is_it_zero(zero, other_args):
    """ check if the first argument equals 0 """
    if zero == 0:
        return True
    else:
        return False

def is_it_two(two, other_args):
    """ check if the first argument equals 2 """
    if two == 2:
        return True
    else:
        return False


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
