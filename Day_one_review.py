def show_progress(items, current_day):
    """
    Displays the curriculum and highlights where we are.
    """
    print(f"\n{'='*10} 30-DAY PYTHON MASTERY {'='*10}")
    
    for index, topic in enumerate(items, start=1):
        # We use a conditional to mark our current spot
        if index == current_day:
            status = "⬅️ CURRENT"
        elif index < current_day:
            status = "✅ DONE"
        else:
            status = "⏳ UPCOMING"
            
        print(f"Day {index:02}: {topic:<35} {status}")

if __name__ == "__main__":
    # This list represents our data
    curriculum = [
        "Project Setup & Review",
        "Functions (*args, **kwargs)",
        "List Comprehensions",
        "OOP Part 1: Classes",
        "OOP Part 2: Inheritance"
    ]
    
    # We call the function and tell it we are on Day 1
    show_progress(curriculum, current_day=1)