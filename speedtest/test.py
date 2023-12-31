import time
import random
import sys

class TypingSpeedTest:
    def __init__(self):
        self.paragraphs = [
            "The quick brown fox jumps over the lazy dog.",
            "To be or not to be, that is the question.",
            "In the beginning, God created the heavens and the earth.",
            "All that glitters is not gold.",
            "Two roads diverged in a wood, and I— I took the one less traveled by."
        ]
        self.reset_game()

    def get_paragraph(self):
        return random.choice(self.paragraphs)

    def reset_game(self):
        self.paragraph = self.get_paragraph()
        self.input_text = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = 0
        self.wpm = 0
        self.end = False

    def show_results(self):
        if not self.end:
            # Calculate time
            self.total_time = time.time() - self.time_start
            
            # Calculate accuracy
            correct_characters = sum(1 for a, b in zip(self.paragraph, self.input_text) if a == b)
            total_characters = len(self.paragraph)
            self.accuracy = correct_characters / total_characters * 100
            
            # Calculate words per minute
            self.wpm = len(self.input_text.split()) * 60 / (5 * self.total_time)
            
            print("\nResults:")
            print(f"Time: {round(self.total_time)} seconds")
            print(f"Accuracy: {round(self.accuracy)}%")
            print(f"Words per Minute (WPM): {round(self.wpm)}")
            
            self.end = True

    def run(self):
        print("Type the following paragraph:")
        print(self.paragraph)
        input("Press Enter when you are ready to start typing...")

        self.time_start = time.time()

        while not self.end:
            user_input = input("Type here: ")

            if user_input.strip() == self.paragraph:
                print("Congratulations! You typed it correctly.")
            else:
                print("Oops! Your typing is not correct.")

            self.input_text = user_input
            self.show_results()

            reset_choice = input("Do you want to try again? (y/n): ")
            if reset_choice.lower() == 'y':
                self.reset_game()
            else:
                sys.exit("Thank you for playing!")

if __name__ == "__main__":
    TypingSpeedTest().run()

