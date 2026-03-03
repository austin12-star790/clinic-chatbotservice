import sqlite3

def add_appointment(name, date, service):
    conn = sqlite3.connect("clinic.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO appointments (patient_name, date, service) VALUES (?, ?, ?)",
        (name, date, service),
    )
    conn.commit()
    conn.close()

def get_appointments():
    conn = sqlite3.connect("clinic.db")
    c = conn.cursor()
    c.execute("SELECT * FROM appointments")
    rows = c.fetchall()
    conn.close()
    return rows