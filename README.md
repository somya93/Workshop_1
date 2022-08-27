# Workshop 1 - Basic Python
For this workshop we will be creating a terminal application that allows users to ask, reply, and view questions.

There are three files: main.py, Question.py, and brain.py

Question.py contains the code for the Question class. main.py is where the application begins running and holds the event loop. brain.py holds the function responsible for parsing user input and handling the application logic.

## Question.py 

```
class Question:
    question_text: str
    replies: list

    def __init__(self, q_text):
        self.question_text = q_text
        self.replies = []
```

The Question class has two class attributes, question_text and replies. Python by default does not have static typing. However, we can make use of 'type hints' to resolve this issue.

The constructor takes one paramter, q_text.

```
def __str__(self):
    result = self.question_text + " -- Replies: " + str(self.get_num_replies())
    return result
```
This method overrides the built-in __str__ method that is available to all Python objects. It is similar to the toString() method in Java. In essence, whenever you would want to convert an object of type Question into its string representation, Python will call this method. Therefore, if we ever pass a Question object to a print() statement, the object will be represented in the manner described. E.g. "What is the capital of France? -- Replies: 0" for a Question object with a question_text = "What is the capital of France" and no replies

## main.py
```
if __name__ == '__main__':
    main_prompt = "Type 'p' if you'd like to post a question. Type 'l' to list all questions. Type 'exit' to quit.\n" \
                  "Type 'h' for more information on how to view/reply to a question.\n" \
                  ">>"
    state_dictionary = {
        'questions': []
    }
    print("=================== Welcome to AskTerminal. ===================")
    user_input = input(main_prompt)

    while user_input != "exit":
        process_input(user_input, state_dictionary)
        user_input = input(main_prompt)
```
In the main function, we have our main_prompt variable which holds the text for our user prompt. We also have a state_dictionary, a Python dictionary, that is used to manage the application's state as Questions are posted and answered. The main event loop is a while loop that makes sure the application terminates when the the user enters 'exit'. Otherwise, it passes on the user input to process_input(), from brain.py, to handle the application's behavior.
## brain.py 
```
def process_input(choice: str, state: dict):
```
process_input takes two parameters, a string (the user input), and a dictionary representing the application's state. This function is called in main.py.

```
if choice == 'p':
    question_text = input("What is your question?\n>>")
    new_question = Question(question_text)
    temp_list = state["questions"]
    temp_list.append(new_question)
    state["questions"] = temp_list
    print(f"'{question_text}' has been posted.")
```
The function includes a series of conditional statements (if/if-else/else). Here, we want to make sure the application behaves according to the user's desires. If users type 'p' when prompted, the application asks them to enter their question. It then converts the string the user just entered into a Question object, which is then appended to the list in the state dictionary. The user is then informed that their question was accepted and posted.
```
elif choice.split(':')[0] == 'v':
    try:
        the_question_number = int(choice.split(':')[1])
        if 0 < the_question_number <= len(state["questions"]):
            the_index = the_question_number - 1
            print(state["questions"][the_index])
            state["questions"][the_index].print_replies()
            reply = input("Enter your reply... type 'stop' to stop answering\n>>")
            if reply != 'stop':
                state["questions"][the_index].replies.append(reply)
        else:
            print("Not a valid question number.\n")
    except TypeError:
        not_valid()
    except ValueError:
        not_valid()
```
Here, we are taking the user's input and checking if it can be split into two parts, the part before a ':' and the part after. 
This code is a little tricky because we've introduced a try-catch block. The try is necessary here because we are parsing a string to find a number in string format, and then converting that would-be number into an integer. During this process, we may receive a TypeError or ValueError if the text following the ':' cannot be represented as a number. If this case is not handled appropriately, our application would terminate prematurely. Python offers a catch-all 'finally', but it catches all exceptions, including the ones we haven't planned for. 