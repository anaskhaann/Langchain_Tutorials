# import language so that we can use language specific splitting
from langchain.text_splitter import Language, RecursiveCharacterTextSplitter

my_code = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Anas", 22, 8.9)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

"""

my_markdown = """
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.


## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies

"""

# now create a language specific text splitter object
splitter_python = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=25, chunk_overlap=0
)

splitter_markdown = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=25, chunk_overlap=0
)


result_py = splitter_python.split_text(my_code)
result_md = splitter_markdown.split_text(my_markdown)

print("======= Python Below =======")
print(result_py)
print("=" * 60)
print(result_py[0])
print("======= Markdown Below =======")
print(result_md)
print("=" * 60)
print(result_md[0])
