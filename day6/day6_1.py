if __name__ == '__main__':
    with open('input', 'r') as f:
        groups_answers = f.read().split('\n\n')

    result = 0
    for group_answers in groups_answers:
        questions_answered_yes = set(group_answers.replace('\n', '').strip())
        result += len(questions_answered_yes)
    print(result)
