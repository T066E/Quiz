questions = [
    {
        "question": "Which of the following languages has the longest alphabet?",
        "options": ["A: Greek", "B: Russian", "C: Arabic", "D: Chinese"],
        "answer": "B"
    },
    
    {
        "question": "What is the most populated city in the world?",
        "options": ["A: Washington DC", "B: Moscow ", "C: Tokyo", "D: Peking"],
        "answer": "C"
    },

    {
        "question": "Who is generally considered the inventor of the motor car?",
        "options": ["A: Karl Benz", "B: Henry Ford", "C: Henry M. Leland", "D: Walter Owen Bentley"],
        "answer": "B"
    },

    {
        "question": "Which of the following is NOT a fruit?",
        "options": ["A: Rhubarb", "B: Tomatoes", "C:Avocados", "D: Oranges"],
        "answer": "A"
    },

    {
        "question": "The fear of insects is known as what?",
        "options": ["A: Entomophobia", "B: Arachnophobia", "C:Ailurophobia", "D: Trypophobia"],
        "answer": "A" 
    },

    {
        "question": "How long did dinosaurs live on the earth?",
        "options": ["A: 100-150 million years", "B: 150-200 million years", "C: 200+ million years", "D: 50-100 million years"],
        "answer": "B"
    },
]




# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")