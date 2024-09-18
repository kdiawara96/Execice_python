import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Création de la table employees
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    name TEXT,
    salary INTEGER
)
''')

# Insertion de données dans la table employees
employees = [
    ('Alice', 60000),
    ('Bob', 45000),
    ('Charlie', 70000),
    ('David', 30000)
]

cursor.executemany('INSERT INTO employees (name, salary) VALUES (?, ?)', employees)

# Récupération et affichage des employés ayant un salaire supérieur à 50000
cursor.execute('SELECT name, salary FROM employees WHERE salary > 50000')
high_salary_employees = cursor.fetchall()

print("Employés avec un salaire supérieur à 50000 :")
for employee in high_salary_employees:
    print(f"Nom: {employee[0]}, Salaire: {employee[1]}")

# Fermeture de la connexion
conn.commit()
conn.close()
