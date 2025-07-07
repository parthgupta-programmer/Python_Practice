# # Dictionary Practice

# # First storing the name of the student along with their marks in three subjects in a dictionary and printing the average of these marks as per the required student.
# if __name__== "__main__":
#     n=int(input())
#     student_marks={}
#     for _ in range(n):
#         name,*line=input().split()
#         marks=list(map(float,line))
#         student_marks[name]=marks
#     query_name=input()
#     if(query_name in student_marks):
#         print(f"{(((student_marks[query_name])[0]+(student_marks[query_name])[1]+(student_marks[query_name])[2] )/3):.2f}")

d1={"Name":"Virat Kohli","Age":29,"Shirt No.":98}
d1["Name"]="MSD"
d2={"One":1,"Two":2}
d1["New"]=d2
print(d1)