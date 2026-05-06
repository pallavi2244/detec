context_scores = []

def update_context(score):
    context_scores.append(score)

    if len(context_scores) > 5:
        context_scores.pop(0)

def get_context_score():
    return sum(context_scores)

def detect_pattern():
    if len(context_scores) < 3:
        return False
    return context_scores[-1] > context_scores[-2] > context_scores[-3]
