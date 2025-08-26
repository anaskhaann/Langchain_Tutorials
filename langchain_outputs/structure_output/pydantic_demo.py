"""Create a student name and always validate the name is in string format"""

from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    name: str

    # set default value
    # name: str = 'sample'

    # set optional: in optional we need to pass a default value
    age: Optional[int] = None


new_std = {"name": "anas", "age": 22}

stud = Student(**new_std)

print(stud)
print("=================")

# now check the validation
# this will throw error saying that the input should be valid string
# new_std2 = {"name": 134}

# example for default value
new_std2 = {"name": "without age person"}
stud2 = Student(**new_std2)

# example for coerce: type conversion
new_std3 = {"name": "person with string age", "age": "43"}
stud3 = Student(**new_std3)


print(stud2)
print("=================")
print(stud3)
