from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["students"]

def menu():
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))
    collection.insert_one({ "name": name, "age": age, "course": course, "marks": marks })
    print("✅ Student added successfully.")



def view_students():
    for student in collection.find():
        print(student)



def update_student():
    name = input("Enter student name to update: ")
    new_marks = float(input("Enter new marks: "))
    result = collection.update_one({ "name": name }, { "$set": { "marks": new_marks } })
    if result.modified_count > 0:
        print("✅ Student updated.")
    else:
        print("❌ No match found.")



def delete_student():
    name = input("Enter student name to delete: ")
    result = collection.delete_one({ "name": name })
    if result.deleted_count > 0:
        print("✅ Student deleted.")
    else:
        print("❌ No student found.")


        
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("👋 Exiting...")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
