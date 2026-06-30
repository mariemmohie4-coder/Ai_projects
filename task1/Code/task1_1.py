
grades =[[85, 78, 92, 88],
[70, 76, 80, 65],
[90, 88, 94, 91],
[60, 65, 58, 62],
[100, 95, 98, 97]] 
##Convert the data into a NumPy array.
import numpy as np
grades_arr = np.array(grades)

##print the shape of the array
arr_shape = grades_arr.shape
print("The shape of the array=", arr_shape)
print("-"*60)

##Compute The mean grade of each student
student_mean = grades_arr.mean(axis=1)
print("The mean grade of each student=",student_mean)
print("-"*60)

##Compute The mean grade of each subject
subject_mean = grades_arr.mean(axis=0)
print("The mean grade of each subject=",subject_mean)
print("-"*60)

##Extract the students whose average grade is greater than 85
student = grades_arr[student_mean>85]
print("The students whose average grade is greater than 85=\n",student)
print("-"*60)

##Add a bonus of 5 marks to all grades
bonus = grades_arr + 5 
print("The grades after bonus of 5 =\n",bonus)
print("-"*60)

##Normalize the grades using Min-Max normalization
max_grade = grades_arr.max(axis = 1)
min_grade = grades_arr.min(axis = 1)
normalize =(grades_arr - min_grade.reshape(5,1))/(max_grade.reshape(5,1)-min_grade.reshape(5,1))
print("Normalize the grades =\n",np.round(normalize, 2))
print("-"*60)

##Flatten the array into a single vector
Flatten = grades_arr.flatten()
print("Flatten the array =\n",Flatten)
print("-"*60)




