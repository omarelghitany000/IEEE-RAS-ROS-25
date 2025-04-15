def read_scores(filename):
    scores = []
    with open(filename, 'r') as file:
        for line in file:
            score = float(line.strip())  # This may raise ValueError
            scores.append(score)
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores)

def write_result(filename, average):
    with open(filename, 'w') as file:
        file.write(f"Average Score: {average:.2f}")

