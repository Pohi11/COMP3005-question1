import psycopg2

# Connects to the PostgreSQL database
def connect_db():
    return psycopg2.connect(
        dbname="student_db",
        user="postgres",
        password="postgres",  
        host="localhost"
    )

# Retrieves and prints all student records
def getAllStudents():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY student_id")
    students = cur.fetchall()
    print("Current students in the database:")
    for student in students:
        print(student)
    cur.close()
    conn.close()

# Adds a new student record
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, enrollment_date))
        conn.commit()
        print(f"Student {first_name} {last_name} added successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

# Updates the email for a specific student
def updateStudentEmail(student_id, new_email):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        conn.commit()
        print(f"Student ID {student_id}'s email updated to {new_email}.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

# Deletes a specific student record
def deleteStudent(student_id):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        print(f"Student ID {student_id} deleted from the database.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

# Example function calls
if __name__ == "__main__":
    #getAllStudents()
    #addStudent('Alice', 'Wonderland', 'alice@example.com', '2023-09-03')
    #updateStudentEmail(1, 'john.updated@example.com')
    #deleteStudent(2)
    getAllStudents()
