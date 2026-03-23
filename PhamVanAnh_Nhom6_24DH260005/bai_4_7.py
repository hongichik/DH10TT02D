student=[{"name":"trường bựa","age":20,"score":9.0},
         {"name":"quỷ sa tăng","age":40,"score":10},
         {"name":"khang","age":19,"score":8.5},]
print(student)
max_student = student[0]
for s in student:
    if s["score"]>max_student["score"]:
         max_student=s
         print("sinh viên có điểm cao nhất là",max_student)
new_student=[]
for s in student:
     new_s ={"name":s["name"],
            "age":s["age"]+1,
            "score":s["score"]
            }
     new_student.append(new_s)
print("danh sách sau khi tăng tuổi",new_student)