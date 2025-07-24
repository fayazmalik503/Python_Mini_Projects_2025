# Step 1: List of questions (each is a dictionary)

quiz = [
    {"question": "What is the capital of Pakistan?", "answer": "Islamabad"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who is the founder of Microsoft?", "answer": "Bill Gates"}
]

# Step 2: Score tracker
score = 0

# Step 3: Loop through each question

for q in quiz:
    print("\n" + q["question"])
    user_answer = input("Your answer: ")
      # Check if correct
    if user_answer.strip().lower() == q["answer"].lower():
        print("✅ Correct!")
        score += 1
    
    else:
        print(f"❌ Wrong. Correct answer is: {q['answer']}")

    # Step 4: Final score
print(f"\n🎯 You got {score} out of {len(quiz)} correct.")