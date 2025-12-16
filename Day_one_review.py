# topics = ["snack game", "jumping", "running"]

def show_progress(items):
    for index, topics in enumerate(items, start=1):
        print(f"Day: {index}: {topics}")
        
        
        
if __name__ == "__main__":
    curriculum = ["Setup & Review", "Functions Deep Dive", "Comprehensions", "OOP Part 1"]
    show_progress(curriculum)



        
        