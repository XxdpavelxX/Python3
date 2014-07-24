Here are your instructions:

 



Create a Python3_Homework13 project and assign it to your Python3_Homework working set. In the Python3_Homework13/src 
folder, create a program named mathquiz.py. In this program, you will create a math quiz. This quiz will ask the user 
five addition questions adding random integers between 1 and 10 inclusive. Each answer will be timed so you can generate
the following time results:
•Time for each question 
•Total time for all questions 
•Average time per question

This program needs to generate random numbers using Python's random library. 


Your project should meet the following conditions:

You must include a working test_mathquiz.py unittest file that tests at least one function. Each time the test runs, it 
must present random integers.

Your code must generate output that looks like this:


What is the sum of 6 and 6? 1212 is right!What is the sum of 5 and 4? 99 is right!What is the sum of 4 and 2? 66 is right!
What is the sum of 1 and 1? 22 is right!What is the sum of 9 and 2? 111111 is wrong!Question #1 took about 1 seconds to 
complete and was right.Question #2 took about 1 seconds to complete and was right.Question #3 took about 1 seconds to 
complete and was right.Question #4 took about 2 seconds to complete and was right.Question #5 took about 2 seconds to 
complete and was wrong.You took 9 seconds to finish the quizYour average time was 1.8 seconds per question
Submit mathquiz.py and test_mathquiz.py when your programs are working to your satisfaction.

###############################################################################################################################################################################################################


import random
from datetime import datetime
   
def get_random_number():
    return random.randrange(1, 10)

def input_answer(num1, num2):
    try:
        return int(input("What is the sum of %d and %d? " % (num1, num2)))
    except ValueError:
        print("Answer must be integer. Pleases try again.")
        return input_answer(num1, num2)

def get_answer(num1, num2, answer):
    if (answer == num1 + num2):
        return "right!"
    else:
        return "wrong!"
    
def print_answer(num1, num2, answer):
    print("%d is %s" % (answer, get_answer(num1, num2, answer)))

def time_difference(time1, time2):
    delta = time2 - time1
    return delta.seconds
    
class MathQuiz:
    
    def __init__(self):
        self.quiz_num = 5
        self.quiz_time = []
        self.quiz_ans = []
            
    def run(self):
        for count in range(self.quiz_num):
            num1 = get_random_number()
            num2 = get_random_number()
            start_time = datetime.now()
            answer = input_answer(num1, num2)
            end_time = datetime.now()
            print_answer(num1, num2, answer)
            
            self.quiz_ans.append(get_answer(num1, num2, answer))
            self.quiz_time.append(time_difference(start_time, end_time)) 
     
    def __str__(self):
        result = ""
        for count in range(self.quiz_num):
            result += "Question #%d took about %d seconds to complete and was %s.\n" % (count+1, self.quiz_time[count], self.quiz_ans[count])
        result += "You took %d seconds to finish the quiz\n" % sum(self.quiz_time)
        result += "Your average time was %0.1f seconds per question\n" % (sum(self.quiz_time) / self.quiz_num)
        return result
    
    def print_result(self):
        print(self)
    
if __name__ == "__main__":
    quiz = MathQuiz()
    quiz.run()
    quiz.print_result()
