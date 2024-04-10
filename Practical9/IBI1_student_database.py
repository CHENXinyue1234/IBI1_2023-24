class students:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
name=input('Enter the name:')
major=input('Enter the major, BMI/BMS:')
code_portfolio_score=input('Enter the portfolio score (0-100):')
group_project_score=input('Enter the group project score (0-100):')
exam_score=input('Enter the exam score (0-100):')
student_information=students(name, major, code_portfolio_score, group_project_score, exam_score)
print("Name:",student_information.name," ","Major:",student_information.major," ", "Code portfolio score:",student_information.code_portfolio_score," ", "Group project score:",student_information.group_project_score," ", "Exam score:",student_information.exam_score)