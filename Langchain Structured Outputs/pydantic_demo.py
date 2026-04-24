from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name : str = 'User' #Default Value
    age : Optional[int] = None #if no value is given 
    email : EmailStr #email validation
    cgpa : float = Field(gt=0 , lt=10 , default = 5,description = "A decimal value indicating cgpa of a student") #greater than 0 and less than 10
#Above is the Schema 

new_student = {'name':'akshita','age':'32','email':'abc@some.com','cgpa' :7.25} #implicit typecast conversion of age-str to int 
#raw data


student = Student(**new_student) 
# **-> unpack dict into keyword arguments 
'''Student(**new_student) ->becomes-> Student(name='nitesh') '''
print(student)
print(type(student))
print(student.name, student.age,student.email,student.cgpa)
print(type(student.age))

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student)