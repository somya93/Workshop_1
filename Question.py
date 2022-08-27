class Question:
    question_text: str
    replies: list

    def __init__(self, q_text):
        self.question_text = q_text
        self.replies = []

    def get_num_replies(self):
        return len(self.replies)

    def print_replies(self):
        print("============ Replies ============")
        for reply in self.replies:
            print(f"<< {reply}")

    def __str__(self):
        result = self.question_text + " -- Replies: " + str(self.get_num_replies())
        return result
