import pandas as pd
import sqlite3

# 1. Daten aus Moodle-Export laden
df = pd.read_excel("moodle_export.xlsx")

# 2. In SQLite speichern (vereinfacht)
conn = sqlite3.connect("grading_db.sqlite")
df.to_sql("raw_grading", conn, if_exists="replace")

# 3. Abfrage für die Korrektur-Ansicht (Gruppiert nach Zufallsfrage)
# In Moodle heißt die Spalte oft 'Frage 1: [Name der Frage]'
def get_answers_for_question(question_name):
    query = f"SELECT student_id, answer_text FROM raw_grading WHERE question_name = '{question_name}'"
    return pd.read_sql(query, conn)