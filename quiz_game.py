print("\n")
print("\*/\*/\*/\*/Welcome to Computer Quiz Game!\*/\*/\*/\*/")

is_playing = input("Do you want to play? ")

if is_playing.lower() != "yes":
    print("See you next time!")
    quit()

no_of_questions = 4
your_score = 0

your_answer = input("Who is the Father of Java Programming Language? ")
if your_answer.lower() == "james gosling":
    print("Correct!")
    your_score += 1
else:
    print("Incorrect!")

your_answer = input("What does GPU stands for? ")
if your_answer.lower() == "graphics processing unit":
    print("Correct!")
    your_score += 1
else:
    print("Incorrect!")

your_answer = input("What does ROM stands for? ")
if your_answer.lower() == "read only memory":
    print("Correct!")
    your_score += 1
else:
    print("Incorrect!")

your_answer = input("Who is the Father of Computer? ")
if your_answer.lower() == "charles babbage":
    print("Correct!")
    your_score += 1
else:
    print("Incorrect!")

print(f"\nYour score is {your_score}/4.")
print(f"You got {(your_score / no_of_questions) * 100}%.")