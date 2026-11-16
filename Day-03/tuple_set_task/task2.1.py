
def student_marks(marks):
    lowest_mark = min(marks)
    highest_mark = max(marks)
    average_mark = sum(marks) / len(marks)
    
    return (lowest_mark, highest_mark, average_mark)

marks=[40, 50, 60, 70, 80]

lowest, highest, average = student_marks(marks)
print("Lowest mark:", lowest)   
print("Highest mark:", highest)
print("Average mark:", average)
    