from Question import Question


def not_valid():
    print("Not a valid command.")


def process_input(choice: str, state: dict):
    if choice == 'p':
        question_text = input("What is your question?\n>>")
        new_question = Question(question_text)
        temp_list = state["questions"]
        temp_list.append(new_question)
        state["questions"] = temp_list
        print(f"'{question_text}' has been posted.")
    elif choice == 'l':
        print(f"Listing all questions... {(len(state['questions']))} found \n")
        if len(state['questions']) > 0:
            for index, q in enumerate(state['questions']):
                print(f"[{index + 1}] {q}")
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
    elif choice == 'h':
        print("=================== AskTerminal Help ===================\n"
              "Type 'v:' followed by the question number to reply to that question."
              " E.g. v:16 would allow you to reply to Question 16.\n")
    else:
        not_valid()
