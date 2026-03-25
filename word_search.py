def binary_search_word(dictionary, target):
    left = 0
    right = len(dictionary) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_word = dictionary[mid][0]  # get only the word
        
        if mid_word == target:
            return mid
        elif mid_word < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
if __name__ == "__main__":

    words = [

    # A
    ("ability", "The power to do something."),
    ("animal", "A living creature that is not a plant."),

    # B
    ("balance", "A state of stability."),
    ("beauty", "The quality of being pleasing."),

    # C
    ("change", "To make different."),
    ("child", "A young person."),

    # D
    ("danger", "Possibility of harm."),
    ("dream", "Thoughts during sleep."),

    # E
    ("energy", "Power to do work."),
    ("event", "Something that happens."),

    # F
    ("family", "Parents and children."),
    ("future", "Time yet to come."),

    # G
    ("garden", "Place where plants grow."),
    ("growth", "The process of increasing."),

    # H
    ("health", "State of being well."),
    ("hope", "Desire for something good."),

    # I
    ("idea", "A thought or plan."),
    ("improve", "To make better."),

    # J
    ("job", "Work done for money."),
    ("journey", "A trip."),

    # K
    ("kindness", "The quality of being kind."),
    ("knowledge", "Information and skills."),

    # L
    ("learn", "To gain knowledge."),
    ("love", "Deep affection."),

    # M
    ("memory", "Ability to remember."),
    ("music", "Art of sound and rhythm."),

    # N
    ("nature", "The physical world."),
    ("number", "A mathematical value."),

    # O
    ("object", "A thing."),
    ("opinion", "A personal belief."),

    # P
    ("peace", "Freedom from conflict."),
    ("power", "Ability to control."),

    # Q
    ("quality", "Level of excellence."),
    ("question", "Something asked."),

    # R
    ("reason", "A cause or explanation."),
    ("respect", "Feeling of admiration."),

    # S
    ("science", "Study of the natural world."),
    ("success", "Achievement of a goal."),

    # T
    ("truth", "Something real or correct."),
    ("trust", "Belief in reliability."),

    # U
    ("understand", "To comprehend."),
    ("unity", "Being joined together."),

    # V
    ("value", "Worth or importance."),
    ("victory", "Success in competition."),

    # W
    ("wisdom", "Good judgment."),
    ("world", "The Earth."),

    # X
    ("x-ray", "A medical imaging technique."),
    ("xylophone", "A musical instrument."),

    # Y
    ("year", "Twelve months."),
    ("youth", "Period of being young."),

    # Z
    ("zebra", "A striped animal."),
    ("zone", "An area or region.")

    ]

    print("📖 Mini Dictionary (Binary Search Enabled)")
    print("Type a word to search, an index number, or 'exit' to quit.\n")

    while True:
        user_input = input("Enter word or index: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # If user enters a number → search by index
        if user_input.isdigit():
            index = int(user_input)

            if 0 <= index < len(words):
                word, meaning = words[index]
                print(f"\nIndex: {index}")
                print(f"Word: {word}")
                print(f"Meaning: {meaning}\n")
            else:
                print("Index out of range.\n")

        # Otherwise → search by word using binary search
        else:
            result = binary_search_word(words, user_input.lower())

            if result != -1:
                word, meaning = words[result]
                print(f"\nIndex: {result}")
                print(f"Word: {word}")
                print(f"Meaning: {meaning}\n")
            else:
                print(f"'{user_input}' not found in dictionary.\n")