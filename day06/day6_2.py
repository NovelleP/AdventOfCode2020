if __name__ == '__main__':
    with open('input', 'r') as f:
        groups_answers = f.read().split('\n\n')

    result = 0
    for group_answers in groups_answers:
        questions_answered_yes_by_allgroup = set('abcdefghijklmnopqrstuvwxyz')
        for person_answers in group_answers.split('\n'):
            questions_answered_yes_by_allgroup = questions_answered_yes_by_allgroup.intersection(set(person_answers))
        result += len(questions_answered_yes_by_allgroup)
    print(result)
