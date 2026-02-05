from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004",
    database="taskdb"
)

cursor = db.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]
    status = request.form["status"]

    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)",
        (title, description, status)
    )
    db.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
