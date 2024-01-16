import sqlite3

conn = sqlite3.connect("TruckingApp.db")
c = conn.cursor()

def read_data():
    return c.execute("""SELECT * FROM equipment_type""").fetchall()

def run_process():
    return read_data()
    # COMMIT CHANGES
    conn.commit()
    # CLOSE THE CONNECTION
    conn.close()

if __name__ == '__main__':
    run_process()