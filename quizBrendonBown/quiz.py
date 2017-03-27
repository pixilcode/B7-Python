from quizElements import Quiz, Question
import pickle, os

def getAllQuizzes():
    #If there are not any quizzes, return an empty array
    #Otherwise, open the file and get the quizzes
    if not os.path.isfile('quizzes.dat'):
        return [];
    else:
        file = open('quizzes.dat', 'rb');
        data = pickle.load(file);
        file.close();
        return data;

def createQuiz():
    #Get the name of the quiz
    quiz = Quiz(input('What is the name of the quiz? >>> '));

    #While they still want to ask a question, get the question
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

    #Add the quiz to the collection of quizzes
    quizzes.append(quiz);

def saveQuizzes():
    #Save the quizzes in a .dat file
    file = open('quizzes.dat', 'wb');
    pickle.dump(quizzes, file);
    file.close();

def ask(question):
    #Print the question
    print(question.question + '\n');

    #Print the options
    for option in range(question.numOfOptions):
        print(str(option + 1) + '. ' + question.options[option]);
    print();

    #Ask for the answer and if it is correct, return True, otherwise return False
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
    #Set the quiz score to 0
    quiz.score = 0;

    #Print the quiz name
    print('\n\n\n' + quiz.name);

    #Ask each question
    for question in quiz.questions:
        if ask(question):
            quiz.score += 1;

    #Print the quiz score
    print('\nYour score is ' + str(quiz.score) + ' out of ' + str(len(quiz.questions)));

#Get each of the available quizzes
quizzes = getAllQuizzes();

#Print intro
print('Welcome to Quizzer!');

#While they are still wanting to take the test, keep looping
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
