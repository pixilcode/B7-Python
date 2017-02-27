class Quiz:

    def __init__(self, name):
        self.name = name;
        self.score = 0;
        self.questions = [];

    def addQuestion(self, question):
        self.questions.append(question);

class Question:

    def __init__(self, question, numOfOptions, options, correctAnswer):
        self.question = question;
        self.numOfOptions = numOfOptions;
        self.options = options;
        self.correctAnswer = correctAnswer;
