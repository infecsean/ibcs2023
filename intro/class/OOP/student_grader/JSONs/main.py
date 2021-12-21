from getData import Student


def Login():
    StudentID = input("Enter your student ID: ")
    Student(StudentID)


def main():
    Login()


if __name__ == "__main__":
    main()
