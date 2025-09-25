def sort_scores(scores):
    """
    Sort a dictionary of names and scores.
    
    Sorting rules:
    - Primary: score (ascending)
    - Secondary: name (alphabetical, if scores are equal)
    
    Args:
        scores (dict): Dictionary with {name: score} pairs.
    
    Returns:
        list: Sorted list of (name, score) tuples.
    """
    return sorted(scores.items(), key=lambda x: (x[1], x[0]))


if __name__ == "__main__":
    # Example datasets
    exam_scores = {
        "Alice": 88,
        "Bob": 95,
        "Clara": 75,
        "David": 95,
        "Eve": 62,
    }

    game_scores = {
        "Shadow": 320,
        "Blaze": 450,
        "Nova": 410,
        "Echo": 450,
    }

    coding_challenge = {
        "Zara": 120,
        "Milo": 200,
        "Kai": 150,
        "Nina": 180,
    }

    print("Exam scores sorted:")
    print(sort_scores(exam_scores))

    print("\nGame scores sorted:")
    print(sort_scores(game_scores))

    print("\nCoding challenge scores sorted:")
    print(sort_scores(coding_challenge))
