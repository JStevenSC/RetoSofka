import time
import sqlite3


class CNXN_SQL_Manager:
    def __init__(self):
        self.Intentos_CNXNS = 0  # Intentos de conexion

    def __enter__(self):
        self.Intentos_CNXNS = 1
        while 1:
            try:
                self.Cnxn = sqlite3.connect('Naves.sqlite')
                self.Cursor = self.Cnxn.cursor()
                break
            except:
                if self.Intentos_CNXNS <= 3:
                    self.Intentos_CNXNS = self.Intentos_CNXNS + 1
                    time.sleep(0.05)
                else:
                    print("ERROR_CNXN_SQL")

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.Cursor.close()
        self.Cnxn.close()
