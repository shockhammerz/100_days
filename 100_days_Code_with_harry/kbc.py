import random

class KBCGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of India?", "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"], "correct_answer": "B"},
            {"question": "Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "correct_answer": "B"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"], "correct_answer": "A"},
            # Add more questions as needed
        ]
        self.prize_money = [0, 1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
        self.current_question_index = 0
        self.lifelines = ["50:50", "Phone a Friend", "Ask the Audience"]
        self.remaining_lifelines = self.lifelines.copy()
        self.user_choice = None

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        print(f"\nQuestion {self.current_question_index + 1}: {question_data['question']}")
        for option in question_data['options']:
            print(option)
        print()

    def get_user_input(self):
        self.user_choice = input("Enter your choice (A/B/C/D) or type 'lifeline' to use a lifeline: ").upper()

    def check_answer(self):
        question_data = self.questions[self.current_question_index]
        return self.user_choice == question_data['correct_answer']

    def use_lifeline(self, lifeline):
        if lifeline in self.remaining_lifelines:
            self.remaining_lifelines.remove(lifeline)
            if lifeline == "50:50":
                correct_answer = self.questions[self.current_question_index]['correct_answer']
                options = self.questions[self.current_question_index]['options']
                options.remove(correct_answer)
                incorrect_option = random.choice(options)
                print(f"\n{incorrect_option} is eliminated.")
                options.remove(incorrect_option)
                print(options)
            elif lifeline == "Phone a Friend":
                print("\nCalling a friend for help...")
                # Implement logic to simulate a friend's response
                print("Your friend suggests: I think the answer is", random.choice(self.questions[self.current_question_index]['options']))
            elif lifeline == "Ask the Audience":
                print("\nAsking the audience for help...")
                # Implement logic to simulate the audience response
                print("The audience thinks the answer is", random.choice(self.questions[self.current_question_index]['options']))

    def start_game(self):
        print("Welcome to Kon Banega Crorepati!")
        while self.current_question_index < len(self.questions):
            self.display_question()
            self.get_user_input()
            if self.user_choice == "LIFELINE":
                lifeline = input("Choose a lifeline (50:50/Phone a Friend/Ask the Audience): ")
                self.use_lifeline(lifeline)
            else:
                if self.check_answer():
                    print("Correct! You won", self.prize_money[self.current_question_index], "Rupees.")
                    self.current_question_index += 1
                else:
                    print("Incorrect! Game over.")
                    break
        print("Congratulations! You won", self.prize_money[self.current_question_index - 1], "Rupees.")

if __name__ == "__main__":
    kbc_game = KBCGame()
    kbc_game.start_game()
