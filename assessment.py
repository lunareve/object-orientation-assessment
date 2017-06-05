"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Polymorphism: makes code interchangeable and behave predictably
   Abstraction: we don't have to understand the inner workings of the code to use it
   Encapsulation: keeps related parts together, ie attributes and methods

2. What is a class?
   A class is a factory that makes instances.
   It can also be thought of as a type of something.

3. What is an instance attribute?
   An instance attribute is a postit that describes
   the chracteristics of an instance.

4. What is a method?
   A method is an action that can be used on a related instance,
   but not on other types.

5. What is an instance in object orientation?
   An instance in oo would be an instanciation of a class.
   If a class is a blueprint,
   an instance would be the physical building
   that gets constructed from that blueprint.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is more abstract.
   An instance attribute takes precedence over class attributes
   when the program is running.
   A class attribute could be used to make sure child instances have consistency.
   For example, if you want to add a bunch of shoes to your online store,
   you could make sure each listing has a shoe name, description, price, and color.
   To make each shoe listing unique, you could use instance attributes
   to specify exactly the shoe name, color, etc.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Student info with first last name and address."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions and their correct answers."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def quiz(self):
        """Prompts user for answer to question and evaluates."""
        user_answer = raw_input(self.question + " > ")
        print user_answer == self.correct_answer
        return user_answer == self.correct_answer


class Exam(object):
    """An exam filled with questions."""

    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question):
        """Adds a question to the exam."""
        self.questions.append(question)

    def administer(self):
        """Administers questions in the exam and returns percent of correct answers."""
        count = 0
        for question in self.questions:
            if question.quiz():
                count += 1

        return count * 100.0 / len(self.questions)


class StudentExam(object):
    """Stores a student, an exam, and student's score."""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()
        print "The {} exam score for {} {} is: {}".format(
            self.exam.exam_name,
            self.student.first_name,
            self.student.last_name,
            self.score
            )


def example():
    """An example of using the above classes to administer an exam to a student."""

    exam1 = Exam("Python")
    question1 = Question("What is your name?", "Lancelot")
    question2 = Question("What is your quest?", "Holy Grail")
    question3 = Question("What is your favorite color?", "blue")
    questions = [question1, question2, question3]

    for question in questions:
        exam1.add_question(question)

    student1 = Student("Sir", "Lancelot", "Camelot")
    student_exam1 = StudentExam(student1, exam1)

    student_exam1.take_test()





