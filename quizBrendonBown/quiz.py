from quizElements import Quiz, Question
import pickle, os

def getAllQuizzes():
    if not os.path.isfile('quizzes.dat'):
        return [];
    else:
        file = open('quizzes.dat', 'rb');
        data = pickle.load(file);
        file.close();
        return data;

def createQuiz():
    quiz = Quiz(input('What is the name of the quiz? >>> '));
    again = 'Y';
    while not again == 'N':
        print();
        question = input('What is the question? >>> ');
        numOfOps = int(input('How many options will there be? >>> '));
        options = [];
        for i in range(numOfOps):
            options.append(input('Option ' + str(i + 1) + ' >>> '));

        correctAnswer = input('What is the correct answer? (Type the option number) >>> ');
        quiz.addQuestion(Question(question, numOfOps, options, correctAnswer));
        again = input('Add another question? (Y/N) >>> ');

    quizzes.append(quiz);

def saveQuizzes():
    file = open('quizzes.dat', 'wb');
    pickle.dump(quizzes, file);
    file.close();

def ask(question):
    print(question.question + '\n');
    for option in range(question.numOfOptions):
        print(str(option + 1) + '. ' + question.options[option]);
    print();
    answer = int(input('Answer (Type the option number) >>> '));
    if answer == int(question.correctAnswer):
        print('Correct');
        print();
        return True;
    else:
        print('Incorrect');
        print();
        return False;

def takeQuiz(quiz):
    quiz.score = 0;
    print('\n\n\n' + quiz.name);
    for question in quiz.questions:
        if ask(question):
            quiz.score += 1;
    
    print('\nYour score is ' + str(quiz.score) + ' out of ' + str(len(quiz.questions)));

quizzes = getAllQuizzes();
print('Welcome to Quizzer!');
while True:
    print();
    directions = int(input('Would you like to:\n1. Create a quiz\n2. Take a quiz\n3. Save quizzes\n4. Exit\n(Type the option number) >>> '));
    print();
    if directions == 1:
        createQuiz();
    elif directions == 2:
        if len(quizzes) < 1:
            print('There are no available quizzes');
            continue;
        else:
            print('Available Quizzes:');
            for i in range(len(quizzes)):
                print(str(i + 1) + '. ' + quizzes[i].name);
            
            answer = int(input('Which quiz would you like to take? (Type the option number) >>> '));
            if answer < 1 or answer > len(quizzes):
                print('Invalid option');
                continue;
            else:
                takeQuiz(quizzes[answer - 1]);
    elif directions == 3:
        saveQuizzes();
    elif directions == 4:
        print('Thanks for using Quizzer!');
        break;
    else:
        print('Invalid option');
        continue;

saveQuizzes();
