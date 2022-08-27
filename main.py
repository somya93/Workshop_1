from brain import process_input

# Press the green button in the gutter to run the script.
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
