from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_data = quiz_brain
        self.window = Tk()
        self.window.title("Let's Quiz!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score.grid(row=0,column=1, pady=10)
        
        self.question_pane = Canvas(width=300, height=250, bg='white', borderwidth=0, highlightthickness=0)
        self.question_text = self.question_pane.create_text(150, 125, width=280, text='Question', font=('Arial', 20, 'italic'), fill='black', )
        self.question_pane.grid(row=1,column=0,columnspan=2, pady=20)
        self.next_question()
        
        correct_img = PhotoImage(file = 'images/true.png')
        self.correct_btn = Button(image=correct_img, borderwidth=0, highlightthickness=0, command=self.answer_true)
        self.correct_btn.grid(row=2,column=0, pady=10)
        
        false_img = PhotoImage(file = 'images/false.png')
        self.false_btn = Button(image=false_img, borderwidth=0, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2,column=1, pady=10)
        
        self.window.mainloop()
    
    def next_question(self):
        if self.quiz_data.still_has_questions():
            question = self.quiz_data.next_question()
            self.question_pane.itemconfig(self.question_text, text=question)
            self.question_pane.config(bg='white')
        else:
            self.summary_score()
            
    def summary_score(self):
        self.question_pane.itemconfig(self.question_text, 
                                      text=f"You've completed the quiz\n Your final score was: {self.quiz_data.score}/{self.quiz_data.question_number}")
        
    def answer_true(self):
        self.check_answer('true')

    def answer_false(self):
        self.check_answer('false')
        
    def check_answer(self, user_answer):
        is_correct = self.quiz_data.check_answer(user_answer)
        if is_correct:
            self.question_pane.config(bg='green')
            display_text="You got it right!"
        else:
            self.question_pane.config(bg='red')
            display_text="That's wrong."
            
        self.question_pane.itemconfig(self.question_text, text=display_text)
        self.update_score()
        self.window.after(500, self.next_question)
        
    def update_score(self):
        self.get_score = self.quiz_data.score
        self.score.config(text=f'Score: {self.get_score}')
        