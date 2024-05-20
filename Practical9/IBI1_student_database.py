class students:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
    def __str__(self):# The'__str__' is used to return a string representation of an object. This has not been taught in class when I do this practical, and I learned the '_str_' from the search engine.
        return (f"Name: {self.name}, Major: {self.major}, "
                f"Code Portfolio Score: {self.code_portfolio_score}, "
                f"Group Project Score: {self.group_project_score}, "
                f"Exam Score: {self.exam_score}")


#Example provided:
name='Alice'
major='BMI'
code_portfolio_score=93
group_project_score=95
exam_score=93
student_information=students(name, major, code_portfolio_score, group_project_score, exam_score)
print(student_information)

#Let the user input:
name=input('Enter the name:')
major=input('Enter the major, BMI/BMS:')
code_portfolio_score=input('Enter the portfolio score (0-100):')
group_project_score=input('Enter the group project score (0-100):')
exam_score=input('Enter the exam score (0-100):')
student_information=students(name, major, code_portfolio_score, group_project_score, exam_score)
print(student_information)
