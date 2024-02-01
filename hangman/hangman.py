
import random
import time

def display_word_state(guessed_letters):
    print("Current word:", " ".join(guessed_letters))

def main():
    print("Welcome to hangman!")

word_hints = [
    ("programming", "It's the process of creating and maintaining software."),
    ("computer", "An electronic device that processes data."),
    ("algorithm", "A step-by-step procedure for solving a problem."),
    ("programmer", "Someone who writes code to create software."),
    ("debugging", "The process of finding and fixing errors in code."),
    ("code", "Instructions that a computer can execute."),
    ("software", "A set of instructions that tell a computer how to perform specific tasks."),
    ("database", "A structured collection of data."),
    ("javascript", "A programming language commonly used for web development."),
    ("python", "A versatile and easy-to-read programming language."),
    ("compiler", "A program that translates code from one programming language to another."),
    ("variable", "A named storage location that holds a value."),
    ("interface", "A point of interaction between components or systems."),
    ("encryption", "The process of converting information into a code."),
    ("algorithm", "A step-by-step procedure for solving a problem."),
    ("network", "A group of interconnected computers."),
    ("keyboard", "An input device with keys for typing."),
    ("framework", "A pre-built set of tools and libraries for software development."),
    ("version", "A specific release of a software product."),
    ("repository", "A central location for storing and managing source code."),
    ("iteration", "Repeating a process or cycle."),
    ("authentication", "The process of verifying the identity of a user."),
    ("agile", "A software development methodology that emphasizes flexibility and collaboration."),
    ("virtualization", "The creation of a virtual version of a resource, such as a server or network."),
    ("responsive", "Adapting to different screen sizes and devices."),
    ("syntax", "The set of rules that dictate the combinations of symbols allowed in a programming language."),
    ("bug", "An error or flaw in a program that causes it to behave unexpectedly."),
    ("debugger", "A tool used for finding and fixing bugs in code."),
    ("frontend", "The user interface and user experience of a website or application."),
    ("backend", "The server-side of a web application or software system."),
    ("cloud", "A network of remote servers for storing and managing data."),
    ("framework", "A pre-built set of tools and libraries for software development."),
    ("responsive", "Adapting to different screen sizes and devices."),
    ("syntax", "The set of rules that dictate the combinations of symbols allowed in a programming language."),
    ("bug", "An error or flaw in a program that causes it to behave unexpectedly."),
    ("debugger", "A tool used for finding and fixing bugs in code."),
    ("frontend", "The user interface and user experience of a website or application."),
    ("backend", "The server-side of a web application or software system."),
    ("cloud", "A network of remote servers for storing and managing data."),
    ("microservices", "A software architecture pattern where an application is composed of small, independent services."),
    ("responsive", "Adapting to different screen sizes and devices."),
    ("framework", "A pre-built set of tools and libraries for software development."),
    ("responsive", "Adapting to different screen sizes and devices."),
    ("syntax", "The set of rules that dictate the combinations of symbols allowed in a programming language."),
    ("bug", "An error or flaw in a program that causes it to behave unexpectedly."),
    ("debugger", "A tool used for finding and fixing bugs in code."),
    ("frontend", "The user interface and user experience of a website or application."),
    ("backend", "The server-side of a web application or software system."),
    ("cloud", "A network of remote servers for storing and managing data."),
    ("microservices", "A software architecture pattern where an application is composed of small, independent services."),
    ("docker", "A platform for developing, shipping, and running applications in containers."),
    ("machine learning", "A subset of artificial intelligence that involves the development of algorithms that allow computers to learn from data."),
    ("agile", "A software development methodology that emphasizes flexibility and collaboration."),
    ("version control", "A system that tracks changes to code and helps multiple developers work on the same project."),
    ("API", "Application Programming Interface - a set of rules that allows one software application to interact with another."),
    ("framework", "A pre-built set of tools and libraries for software development.")
    }

    # Choose a random word and its corresponding hint
   index = random.randint(0, len(word_hints) - 1)
    hidden_word, word_hint = word_hints[index]

    guessed_letters = ["_"] * len(hidden_word)

    max_attempts = 3
    attempts_left = max_attempts

    # Display initial message with hint and initial state of the word
    print(f"Try to guess the word. Hint: {word_hint}")
    display_word_state(guessed_letters)

    # Start the timer to measure time
    start_time = time.time()

    # Loop until the player guesses the word or runs out of attempts
    while attempts_left > 0:
        user_guess = input("Enter a letter: ").lower()[0]  # Convert to lowercase and take the first character

        if user_guess in hidden_word:
            # Update the guessed letters list with the correctly guessed letter
            guessed_letters = [user_guess if hidden_word[i] == user_guess else guessed_letters[i] for i in range(len(hidden_word))]

            # Display the updated word state
            display_word_state(guessed_letters)

            # Check if the entire word has been guessed
            if "_" not in guessed_letters:
                elapsed_time = time.time() - start_time
                print(f"Congratulations! You guessed the word in {elapsed_time:.2f} seconds!")
                break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Incorrect! You have {attempts_left} attempts left. Try again.")
            else:
                print(f"Sorry, you've run out of attempts. The correct word was: {hidden_word}")

    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()
