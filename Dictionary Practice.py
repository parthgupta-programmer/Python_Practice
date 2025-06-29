# Dictionary Practice
if __name__== "__main__":
    n=int(input())
    student_marks={}
    for _ in range(n):
        name,*line=input().split()
        marks=list(map(float,line))
        student_marks[name]=marks
    query_name=input()
    if(query_name in student_marks):
        print(f"{(((student_marks[query_name])[0]+(student_marks[query_name])[1]+(student_marks[query_name])[2] )/3):.2f}")