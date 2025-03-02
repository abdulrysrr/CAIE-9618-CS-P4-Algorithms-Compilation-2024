class QuestionClass():
    def __init__(self, QuestionP, AnswerP, DifficultyP):
        self.Question = QuestionP
        self.Answer = AnswerP
        self.Difficulty = DifficultyP

    def GetQuestion(self):
        return self.Question
    def GetAnswer(self):
        return self.Answer
    def GetDiffculty(self):
        return self.Difficulty

class QuizClass():
    def __init__(self):
        self.NumberOfQuestions = 0
        self.CurrentQuestion = 0
        self.Questions = [0]*20

    def AddQuestion(self, Question):
        if self.NumberOfQuestions < 20:
            self.Questions[self.NumberOfQuestions] = Question
            self.NumberOfQuestions += 1
            return True
        else:
            return False
    
    def GetQuestion(self):
        return self.Questions[self.CurrentQuestion]
    
    def CheckAnswer(self, Answer):
        if self.GetQuestion().GetAnswer() == Answer:
            self.CurrentQuestion += 1
            return True
        else:
            return False

FirstQuiz = QuizClass()
Question1 = QuestionClass("What is 100/5?", "20", 1)
FirstQuiz.AddQuestion(Question1)
print(FirstQuiz.CheckAnswer("10"))
print(FirstQuiz.CheckAnswer("20"))