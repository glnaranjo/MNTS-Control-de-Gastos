import tkinter as tk
from datetime import date
import sqlite3
import os
import sys

class App:

    def get_base_dir(self):
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.dirname(os.path.abspath(__file__))
    
    def run(self):
        self.ventana.mainloop()

    def crear_db(self):
        BASE_DIR = self.get_base_dir()
        self.DB_PATH = os.path.join(BASE_DIR, "gastos.db")

        print("BD en:", self.DB_PATH)

        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dia INTEGER NOT NULL,
                mes INTEGER NOT NULL,
                anio INTEGER NOT NULL,
                categoria TEXT NOT NULL,
                monto REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Ingresos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes INTEGER NOT NULL,
                anio INTEGER NOT NULL,
                monto REAL NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title("MNTS Control de gastos")
        self.ventana.state("zoomed")

        self.crear_db()

        self.frame_actual = None
        self.mostrar_menu()     

    def cambiar_frame(self, frame_nuevo):
        if self.frame_actual:
            self.frame_actual.destroy()
        self.frame_actual = frame_nuevo
        self.frame_actual.pack(fill="both", expand=True)

    def mostrar_menu(self):
        frame = tk.Frame(self.ventana, bg="#212887")
        self.cambiar_frame(frame)

        BASE_DIR = self.get_base_dir()
        self.DB_PATH = os.path.join(BASE_DIR, "gastos.db")

        self.ventana.state("zoomed")
        self.ventana.configure(bg="#212887")

        self.borde = tk.Frame(self.ventana, bg="#f1f1f1", padx=2, pady=2)
        self.borde.place(x=127, y=90)

        self.btn_e = tk.Label(self.borde, text="", bg="#212887", fg="#000000", font=("Gadugi", 16), width=137)
        self.btn_e.pack(pady=10)

        self.btn_e4 = tk.Label(self.borde, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 16), width=137)
        self.btn_e4.pack(pady=1)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ruta_logo = os.path.join(BASE_DIR, "Logo.png")

        self.logo = tk.PhotoImage(file=self.ruta_logo)
        label = tk.Label(self.borde, image=self.logo)
        label.pack(pady=1)

        self.btn_e = tk.Label(self.borde, text="Control de gastos", bg="#f1f1f1", fg="#212887", font=("Gadugi", 22, "bold"), width=20)
        self.btn_e.pack(pady=1)

        self.btn_e4 = tk.Label(self.borde, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 8), width=137)
        self.btn_e4.pack(pady=1)

        self.btn_1 = tk.Button(self.borde, text="Ingresar Gastos", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1,  command=self.ingresar)
        self.btn_1.pack(pady=10)

        self.btn_2 = tk.Button(self.borde, text="Ver resumen mensual", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1, command=self.ver)
        self.btn_2.pack(pady=10)

        self.btn_3 = tk.Button(self.borde, text="Añadir Ingresos/Presupuesto mensual", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1, command=self.AniadirPresupuesto)
        self.btn_3.pack(pady=10)

        self.btn_5 = tk.Button(self.borde, text="Opciones", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1, command=self.opciones)
        self.btn_5.pack(pady=10)

        self.btn_e2 = tk.Label(self.borde, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 8), width=137)
        self.btn_e2.pack(pady=5)

        self.btn_4 = tk.Button(self.borde, text="Salir", bg="#212887", fg="#FFFFFF", activebackground="#212887", font=("Gadugi", 18, "underline"), width=8 , relief="flat", borderwidth=1, highlightthickness=1,command=self.salir)
        self.btn_4.pack(pady=10)

        self.btn_e2 = tk.Label(self.borde, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 4), width=137)
        self.btn_e2.pack(pady=5)
        
        self.btn_e2 = tk.Label(self.borde, text="", bg="#212887", fg="#000000", font=("Gadugi", 16), width=137)
        self.btn_e2.pack(pady=5)

    def ingresar(self):
        self.ventana_ingreso = tk.Toplevel(self.ventana)
        self.ventana_ingreso.title("Ingresar Gastos")
        self.ventana_ingreso.geometry("1024x768")
        self.ventana_ingreso.configure(bg="#3a3f47")
        self.ventana_ingreso.resizable(False, False)

        y = 60

        self.fecha_ingreso = tk.Label(self.ventana_ingreso, text="Ingrese la fecha:", font=("Gadugi", 18))
        self.fecha_ingreso.place(x=424, y=30)

        self.dia = tk.Label(self.ventana_ingreso, text="Dia", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.dia.place(x=431, y=85)
        self.dia_ingreso = tk.Entry(self.ventana_ingreso, width=4, font=("Gadugi", 12))
        self.dia_ingreso.place(x=428, y=120)

        self.mes = tk.Label(self.ventana_ingreso, text="Mes", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.mes.place(x=495, y=85)
        y += 25
        self.mes_ingreso = tk.Entry(self.ventana_ingreso, width=4, font=("Gadugi", 12))
        self.mes_ingreso.place(x=495, y=120)
        y += 35

        self.anio = tk.Label(self.ventana_ingreso, text="Año", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.anio.place(x=562, y=85)
        y += 25
        self.anio_ingreso = tk.Entry(self.ventana_ingreso, width=4, font=("Gadugi", 12))
        self.anio_ingreso.place(x=562, y=120)
        y += 40

        self.barra1 = tk.Label(self.ventana_ingreso, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra1.place(x=475, y=118)
        self.barra2 = tk.Label(self.ventana_ingreso, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra2.place(x=542, y=118)

        ######################

        self.gasto1 = tk.Label(self.ventana_ingreso, text="Comida 🍕", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto1.place(x=374, y=175)
        y += 40
        self.entry_gasto1 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto1.place(x=374, y=205)
        y += 40

        self.gasto2 = tk.Label(self.ventana_ingreso, text="Vivienda 🏠", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto2.place(x=520, y=175)
        y += 28
        self.entry_gasto2 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto2.place(x=520, y=205)
        y += 35

        #######################

        self.gasto3 = tk.Label(self.ventana_ingreso, text="Servicios 🧾", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto3.place(x=374, y=255)
        y += 28
        self.entry_gasto3 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto3.place(x=374, y=285)
        y += 35

        self.gasto4 = tk.Label(self.ventana_ingreso, text="Transporte 🚍", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto4.place(x=520, y=255)
        y += 28
        self.entry_gasto4 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto4.place(x=520, y=285)
        y += 35

        ########################

        self.gasto5 = tk.Label(self.ventana_ingreso, text="Ocio 🎮", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto5.place(x=374, y=335)
        y += 28
        self.entry_gasto5 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto5.place(x=374, y=365)
        y += 35

        self.gasto6 = tk.Label(self.ventana_ingreso, text="Salud 🏥", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto6.place(x=520, y=335)
        y += 28
        self.entry_gasto6 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto6.place(x=520, y=365)
        y += 35

        #############################

        self.gasto7 = tk.Label(self.ventana_ingreso, text="Extras ➕", font=("Gadugi", 12), width=14, bg="#3a3f47", fg="white")
        self.gasto7.place(x=447, y=415)
        y += 28
        self.entry_gasto7 = tk.Entry(self.ventana_ingreso, font=("Gadugi", 12), width=14)
        self.entry_gasto7.place(x=447, y=445)
        y += 45

        ###################################

        botonEnviar = tk.Button(
            self.ventana_ingreso,
            text="    Enviar    ",
            bg="#C7C8CA",
            fg="#000000",
            font=("Tahoma", 14),
            command=self.resultadoTemp
        )
        botonEnviar.place(x=456, y=510)

    def resultadoTemp(self):

        dia_selec=int(self.dia_ingreso.get())
        mes_selec=int(self.mes_ingreso.get())
        anio_selec=int(self.anio_ingreso.get())

        if int(self.dia_ingreso.get())>=32 or int(self.dia_ingreso.get())>=29 and int(self.mes_ingreso.get())==2:
            self.mal = tk.Label(self.ventana_ingreso, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal.place(x=397, y=590)
            self.mal.after(1500, self.mal.destroy)
        elif int(self.mes_ingreso.get())>=13:
            self.mal2 = tk.Label(self.ventana_ingreso, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal2.place(x=397, y=590)
            self.mal2.after(1500, self.mal2.destroy)
        elif int(self.anio_ingreso.get())>=1 and int(self.anio_ingreso.get())<=2000:
            self.mal3 = tk.Label(self.ventana_ingreso, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal3.place(x=397, y=590)
            self.mal3.after(1500, self.mal3.destroy)
        elif int(self.anio_ingreso.get())==0 or int(self.dia_ingreso.get())==0 or int(self.mes_ingreso.get())==0:
            self.mal4 = tk.Label(self.ventana_ingreso, text="Error, Complete el campo de fecha", font=("Gadugi", 12))
            self.mal4.place(x=397, y=590)
            self.mal4.after(1500, self.mal4.destroy)
        else:
            gastos = {
                "Comida": self.entry_gasto1.get(),
                "Vivienda": self.entry_gasto2.get(),
                "Servicios": self.entry_gasto3.get(),
                "Transporte": self.entry_gasto4.get(),
                "Ocio": self.entry_gasto5.get(),
                "Salud": self.entry_gasto6.get(),
                "Extras": self.entry_gasto7.get(),
            }

            BASE_DIR = self.get_base_dir()
            self.DB_PATH = os.path.join(BASE_DIR, "gastos.db")

            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            for categoria, monto in gastos.items():
                if monto.strip():
                    try:
                        cursor.execute("""
                            INSERT INTO gastos (dia, mes, anio, categoria, monto)
                            VALUES (?, ?, ?, ?, ?)
                        """, (dia_selec, mes_selec, anio_selec, categoria, float(monto)))
                    except ValueError:
                        print(f"Valor inválido en {categoria}: {monto}")

            conn.commit()
            conn.close()

            print("Gastos guardados correctamente")
            self.correcto = tk.Label(self.ventana_ingreso, text="Gastos guardados correctamente", font=("Gadugi", 12))
            self.correcto.place(x=389, y=590)
            self.correcto.after(1500, self.correcto.destroy)

    def ver(self):
        self.ventanaVer = tk.Toplevel(self.ventana)
        self.ventanaVer.title("Resumen mensual")
        self.ventanaVer.geometry("1024x768")
        self.ventanaVer.configure(bg="#3a3f47")
        self.ventanaVer.resizable(False, False)

        self.fechaVer = tk.Label(self.ventanaVer, text="Seleccione la fecha:", font=("Gadugi", 14))
        self.fechaVer.place(x=430, y=25)

        self.mesV = tk.Label(self.ventanaVer, text="Mes", font=("Gadugi", 14), bg="#3a3f47", fg="#FFFFFF")
        self.mesV.place(x=463, y=75)
        self.mesV_ingreso=tk.Entry(self.ventanaVer, width=4, font=("Gadugi", 12))
        self.mesV_ingreso.place(x=463, y=110)

        self.anioV = tk.Label(self.ventanaVer, text="Año", font=("Gadugi", 14), bg="#3a3f47", fg="#FFFFFF")
        self.anioV.place(x=530, y=75)
        self.anioV_ingreso=tk.Entry(self.ventanaVer, width=4, font=("Gadugi", 12))
        self.anioV_ingreso.place(x=530, y=110)

        botonEnviar = tk.Button(self.ventanaVer, text="    Ver    ", bg="#C7C8CA", fg="#000000", command=self.MostrarResumen, font=("Tahoma", 12))
        botonEnviar.place(x=478, y=170)

        self.barra1 = tk.Label(self.ventanaVer, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra1.place(x=510, y=108)

    def MostrarResumen(self):

        mesVer = int(self.mesV_ingreso.get())
        anioVer = int(self.anioV_ingreso.get())

        if int(self.mesV_ingreso.get())>=13:
            self.mal2 = tk.Label(self.ventanaVer, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal2.place(x=397, y=250)
            self.mal2.after(1500, self.mal2.destroy)
        elif int(self.anioV_ingreso.get())>=1 and int(self.anioV_ingreso.get())<=2000:
            self.mal3 = tk.Label(self.ventanaVer, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal3.place(x=397, y=250)
            self.mal3.after(1500, self.mal3.destroy)
        else:

            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT categoria, SUM(monto)
                FROM gastos
                WHERE mes = ? AND anio = ?
                GROUP BY categoria
            """, (mesVer, anioVer))

            resumen = cursor.fetchall()

            cursor.execute("""
                SELECT SUM(monto)
                FROM gastos
                WHERE mes = ? AND anio = ?
            """, (mesVer, anioVer))

            total_mes = cursor.fetchone()[0]

            cursor.execute("""
                SELECT SUM(monto)
                FROM Ingresos
                WHERE mes = ? AND anio = ?
            """, (mesVer, anioVer))

            ingresos_mes = cursor.fetchone()[0]

            conn.close()

            if not resumen and total_mes is None and ingresos_mes is None:
                self.noDatos = tk.Label(self.ventanaVer,text="No hay gastos ni ingresos registrados para este mes", font=("Gadugi", 12))
                self.noDatos.place(x=330, y=250)
                self.noDatos.after(1250, self.noDatos.destroy)
                return
            
            if ingresos_mes is None:
                ingresos_mes = 0

            if total_mes is None:
                total_mes = 0

            self.labels_resumen = []

            self.total_mes = float(total_mes)

            diferencia = ingresos_mes - total_mes

            self.textoRes1 = tk.Label(self.ventanaVer, text="Resumen", bg="#3a3f47", fg="#FFFFFF", font=("Gadugi", 14, "underline", "bold"))
            self.textoRes1.place(x=20, y=280)

            y2=320

            for categoria, monto in resumen:
                porcentaje = (monto / total_mes) * 100 if total_mes > 0 else 0

                self.lbl = tk.Label(
                    self.ventanaVer,
                    text=f"{categoria:<12} ${monto:.2f}  ({porcentaje:.3f}%)",
                    font=("Gadugi", 12),
                    bg="#3a3f47",
                    fg="#FFFFFF"
                )
                self.lbl.place(x=20, y=y2)
                self.labels_resumen.append(self.lbl)
                y2 += 30
            
            y2 += 20

            self.textoRes2 = tk.Label(self.ventanaVer, text=f"Gasto total: -${self.total_mes:.2f}", font=("Tahoma", 12), bg="#3a3f47", fg="#FFFFFF")
            self.textoRes2.place(x=20, y=y2)
            y2 += 30

            self.textoRes3 = tk.Label(self.ventanaVer, text=f"Ingreso total: +${ingresos_mes:.2f}", font=("Tahoma", 12), bg="#3a3f47", fg="#FFFFFF")
            self.textoRes3.place(x=20, y=y2)
            y2 += 30

            if diferencia>0:
                self.textoRes4 = tk.Label(self.ventanaVer, text=f"Diferencia: +${diferencia:.2f}", font=("Tahoma", 12), bg="#3a3f47", fg="#42D456")
                self.textoRes4.place(x=20, y=y2)
                y2 += 75
            elif diferencia<0:
                self.textoRes4 = tk.Label(self.ventanaVer, text=f"Diferencia: -${diferencia:.2f}", font=("Tahoma", 12), bg="#3a3f47", fg="#EC6666")
                self.textoRes4.place(x=20, y=y2)
                y2 += 75
            else:
                self.textoRes4 = tk.Label(self.ventanaVer, text=f"Diferencia: ${diferencia:.2f}", font=("Tahoma", 12), bg="#3a3f47", fg="#FFFFFF")
                self.textoRes4.place(x=20, y=y2)
                y2 += 75

            self.botonBorrar = tk.Button(self.ventanaVer, text="    Borrar    ", bg="#C7C8CA", fg="#000000", command=self.Borrar, font=("Tahoma", 12))
            self.botonBorrar.place(x=467, y=y2)

            self.stats()

    def stats(self):

        mesVer = int(self.mesV_ingreso.get())
        anioVer = int(self.anioV_ingreso.get())
        
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()

        self.labels_stats = []

        ########################################################################################################################################################################################################

        cursor.execute("""
            SELECT dia, SUM(monto) AS total_dia
            FROM gastos
            WHERE mes = ? AND anio = ?
            GROUP BY dia
            ORDER BY total_dia DESC
            LIMIT 1
        """, (mesVer, anioVer))

        resultado = cursor.fetchone()

        if resultado:
            dia_mas_gasto, monto_dia = resultado
        else:
            dia_mas_gasto, monto_dia = None, 0

        if dia_mas_gasto:
            self.stat1 = tk.Label(self.ventanaVer, text=f"- El día con mayor gasto fue el {dia_mas_gasto} (${monto_dia:.2f})", font=("Gadugi", 12), bg="#3a3f47", fg="#FFFFFF")
            self.stat1.place(x=450, y=320)
            self.labels_stats.append(self.stat1)

        ########################################################################################################################################################################################################

        cursor.execute("""
            SELECT dia, SUM(monto) AS total_dia
            FROM gastos
            WHERE mes = ? AND anio = ?
            GROUP BY dia
            ORDER BY total_dia ASC
            LIMIT 1
        """, (mesVer, anioVer))

        resultado2 = cursor.fetchone()

        if resultado2:
            dia_menos_gasto, monto_dia2 = resultado2
        else:
            dia_menos_gasto, monto_dia2 = None, 0

        if dia_menos_gasto:
            self.stat2 = tk.Label(self.ventanaVer, text=f"- El día con menor gasto fue el {dia_menos_gasto} (${monto_dia2:.2f})", font=("Gadugi", 12), bg="#3a3f47", fg="#FFFFFF")
            self.stat2.place(x=450, y=350)
            self.labels_stats.append(self.stat2)

        ########################################################################################################################################################################################################

        cursor.execute("""
            SELECT SUM(monto)
            FROM gastos
            WHERE mes = ? AND anio = ?
        """, (mesVer, anioVer))

        mesActual = cursor.fetchone()
        montoMesAct = mesActual[0] if mesActual and mesActual[0] is not None else 0

        ###########################################################################
        
        if mesVer == 1:
            mes_ant = 12
            anio_ant = anioVer - 1
        else:
            mes_ant = mesVer - 1
            anio_ant = anioVer       
        
        cursor.execute("""
            SELECT SUM(monto)
            FROM gastos
            WHERE mes = ? AND anio = ?
        """, (mes_ant, anio_ant))

        mesAnte = cursor.fetchone()
        montoMesAnte = mesAnte[0] if mesAnte and mesAnte[0] is not None else 0

        ##########################################################################

        diferenciaAnterior = montoMesAct - montoMesAnte

        if diferenciaAnterior > 0:
            self.stat3 = tk.Label(self.ventanaVer, text=f"- Se gasto {diferenciaAnterior} mas que el mes anterior", font=("Gadugi", 12), bg="#3a3f47", fg="#EC6666")
            self.stat3.place(x=450, y=380)
            self.labels_stats.append(self.stat3)
        elif diferenciaAnterior < 0:
            self.stat3 = tk.Label(self.ventanaVer, text=f"- Se gasto {diferenciaAnterior} menos que el mes anterior", font=("Gadugi", 12), bg="#3a3f47", fg="#42D456")
            self.stat3.place(x=450, y=380)
            self.labels_stats.append(self.stat3)
        else:
            self.stat3 = tk.Label(self.ventanaVer, text=f"- Se gasto lo mismo que el mes anterior", font=("Gadugi", 12), bg="#3a3f47", fg="#FFFFFF")
            self.stat3.place(x=450, y=380)
            self.labels_stats.append(self.stat3)
        
        ########################################################################################################################################################################################################

    def Borrar(self):

        for self.lbl in self.labels_resumen:
            self.lbl.destroy()
        self.labels_resumen.clear()
        
        for lbl2 in self.labels_stats:
            lbl2.destroy()
        self.labels_stats.clear()
        

        self.labels_resumen.clear()
        self.textoRes1.destroy()
        self.textoRes2.destroy()
        self.textoRes3.destroy()
        self.textoRes4.destroy()
        self.botonBorrar.destroy()

    def salir(self):
        self.ventana.destroy()

    def AniadirPresupuesto(self):
        self.ventanaPresu = tk.Toplevel(self.ventana)
        self.ventanaPresu.title("Añadir Ingresos/Presupuesto mensual")
        self.ventanaPresu.geometry("1024x768")
        self.ventanaPresu.configure(bg="#3a3f47")
        self.ventanaPresu.resizable(False, False)


        self.fecha_ingreso = tk.Label(self.ventanaPresu, text="Ingrese la fecha:", font=("Gadugi", 14))
        self.fecha_ingreso.place(x=440, y=25)


        self.mes = tk.Label(self.ventanaPresu, text="Mes", font=("Gadugi", 14), bg="#3a3f47", fg="#FFFFFF")
        self.mes.place(x=463, y=85)
        self.mes_ingreso = tk.Entry(self.ventanaPresu, width=4, font=("Gadugi", 12))
        self.mes_ingreso.place(x=463, y=120)

        self.barra1 = tk.Label(self.ventanaPresu, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra1.place(x=510, y=118)


        self.anio = tk.Label(self.ventanaPresu, text="Año", font=("Gadugi", 14), bg="#3a3f47", fg="#FFFFFF")
        self.anio.place(x=530, y=85)
        self.anio_ingreso = tk.Entry(self.ventanaPresu, width=4, font=("Gadugi", 12))
        self.anio_ingreso.place(x=530, y=120)

        self.msj1 = tk.Label(self.ventanaPresu, text="¿Que cantidad desea añadir?", font=("Gadugi", 12))
        self.msj1.place(x=412, y=180)
        self.entry_presu = tk.Entry(self.ventanaPresu, font=("Gadugi", 12), width=14)
        self.entry_presu.place(x=450, y=225)

        self.msj2=self.msj1 = tk.Label(self.ventanaPresu, text="$", font=("Gadugi", 12), bg="#3a3f47", fg="white")
        self.msj2.place(x=590, y=225)

        botonEnviar = tk.Button(
            self.ventanaPresu,
            text="    Enviar    ",
            bg="#C7C8CA",
            fg="#000000",
            font=("Tahoma", 12),
            command=self.ResultadoPresu
        )
        botonEnviar.place(x=468, y=300)

    def ResultadoPresu(self):
        
        mes_selec=int(self.mes_ingreso.get())
        anio_selec=int(self.anio_ingreso.get())

        if int(self.mes_ingreso.get())>=13:
            self.mal2 = tk.Label(self.ventanaPresu, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal2.place(x=397, y=400)
            self.mal2.after(1500, self.mal2.destroy)
        elif int(self.anio_ingreso.get())>=1 and int(self.anio_ingreso.get())<=2000:
            self.mal3 = tk.Label(self.ventanaPresu, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal3.place(x=397, y=400)
            self.mal3.after(1500, self.mal3.destroy)
        else:

            gastos = {
                "montoo": self.entry_presu.get()
            }            

            BASE_DIR = self.get_base_dir()
            self.DB_PATH = os.path.join(BASE_DIR, "gastos.db")

            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            for categoria, monto1 in gastos.items():
                if monto1.strip():
                    try:
                        cursor.execute("""
                            INSERT INTO Ingresos (mes, anio, monto)
                            VALUES (?, ?, ?)
                        """, (mes_selec, anio_selec, float(monto1)))
                    except ValueError:
                        print(f"Valor inválido")

            conn.commit()
            conn.close()


            print("Gastos guardados correctamente")
            self.correcto = tk.Label(self.ventanaPresu, text="Presupuesto guardado correctamente", font=("Gadugi", 12))
            self.correcto.place(x=375, y=400)
            self.correcto.after(1500, self.correcto.destroy)

    def opciones(self): 

        frameopciones = tk.Frame(self.ventana, bg="#212887")
        self.cambiar_frame(frameopciones)

        self.borde2 = tk.Frame(frameopciones, bg="#f1f1f1", padx=2, pady=2)
        self.borde2.place(x=127, y=90)

        self.btn_e1 = tk.Label(self.borde2, text="", bg="#212887", fg="#000000", font=("Gadugi", 16), width=137)
        self.btn_e1.pack(pady=10)

        self.btn_e41 = tk.Label(self.borde2, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 16), width=137)
        self.btn_e41.pack(pady=1)

        self.btn_1 = tk.Label(self.borde2, text="Opciones", bg="#f1f1f1", fg="#212887", font=("Gadugi", 22, "bold"), width=20)
        self.btn_1.pack(pady=1)

        self.btn_e4 = tk.Label(self.borde2, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 8), width=137)
        self.btn_e4.pack(pady=1)

        self.btn_12 = tk.Button(self.borde2, text="Borrar gastos", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1,  command=self.AbrirVentanaBorrarGastos)
        self.btn_12.pack(pady=10)

        self.btn_23 = tk.Button(self.borde2, text="Borrar presupuesto/ingresos", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1, command=self.AbrirVentanaBorrarPresu)
        self.btn_23.pack(pady=10)

        self.btn_34 = tk.Button(self.borde2, text="Contacto", bg="#f1f1f1", fg="#000000", font=("Gadugi", 18, "underline"),relief="flat", borderwidth=0, highlightthickness=1, command=self.contacto)
        self.btn_34.pack(pady=10)

        self.btn_e25 = tk.Label(self.borde2, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 8), width=137)
        self.btn_e25.pack(pady=5)

        self.btn_46 = tk.Button(self.borde2, text="Volver", bg="#212887", fg="#FFFFFF", activebackground="#212887", font=("Gadugi", 18, "underline"), width=8 , relief="flat", borderwidth=1, highlightthickness=1,command=self.mostrar_menu)
        self.btn_46.pack(pady=10)

        self.btn_e27 = tk.Label(self.borde2, text="", bg="#f1f1f1", fg="#000000", font=("Gadugi", 4), width=137)
        self.btn_e27.pack(pady=5)
        
        self.btn_e28 = tk.Label(self.borde2, text="", bg="#212887", fg="#000000", font=("Gadugi", 16), width=137)
        self.btn_e28.pack(pady=5)

    def AbrirVentanaBorrarGastos(self):
        self.ventanaBorrarGastos = tk.Toplevel(self.ventana)
        self.ventanaBorrarGastos.title("Borrar gastos")
        self.ventanaBorrarGastos.geometry("1024x768")
        self.ventanaBorrarGastos.configure(bg="#3a3f47")
        self.ventanaBorrarGastos.resizable(False, False)

        self.BorrarGastos()

    def BorrarGastos(self):

        self.fecha_ingreso = tk.Label(self.ventanaBorrarGastos, text="Ingrese la fecha:", font=("Gadugi", 18))
        self.fecha_ingreso.place(x=424, y=30)

        self.dia = tk.Label(self.ventanaBorrarGastos, text="Dia", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.dia.place(x=431, y=85)
        self.dia_ingreso46 = tk.Entry(self.ventanaBorrarGastos, width=4, font=("Gadugi", 12))
        self.dia_ingreso46.place(x=428, y=120)

        self.mes = tk.Label(self.ventanaBorrarGastos, text="Mes", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.mes.place(x=495, y=85)
        self.mes_ingreso46 = tk.Entry(self.ventanaBorrarGastos, width=4, font=("Gadugi", 12))
        self.mes_ingreso46.place(x=495, y=120)

        self.anio = tk.Label(self.ventanaBorrarGastos, text="Año", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.anio.place(x=562, y=85)
        self.anio_ingreso46 = tk.Entry(self.ventanaBorrarGastos, width=4, font=("Gadugi", 12))
        self.anio_ingreso46.place(x=562, y=120)

        self.barra1 = tk.Label(self.ventanaBorrarGastos, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra1.place(x=475, y=118)
        self.barra2 = tk.Label(self.ventanaBorrarGastos, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra2.place(x=542, y=118)

        self.botonEnviar = tk.Button(self.ventanaBorrarGastos, text="    Borrar    ", bg="#C7C8CA", fg="#000000", command=self.EstasSeguro1, font=("Tahoma", 12))
        self.botonEnviar.place(x=465, y=183)

        self.aviso1 = tk.Label(self.ventanaBorrarGastos, text="*AVISO: Esto borrara TODOS los gastos del dia seleccionado*", font=("Gadugi", 12), bg="#3a3f47", fg="white")
        self.aviso1.place(x=300, y=250)

        self.aviso2 = tk.Label(self.ventanaBorrarGastos, text="*En caso de no seleccionar dia se borraran TODOS los registros del mes*", font=("Gadugi", 12), bg="#3a3f47", fg="white")
        self.aviso2.place(x=260, y=290)

        self.q1.destroy()
        self.botonSi.destroy()
        self.botonNo.destroy()
        self.correcto.destroy()
        self.botonOk.destroy()
        self.borradoss.destroy()

    def EstasSeguro1(self):
        self.aviso1.destroy()
        self.aviso2.destroy()
        self.botonEnviar.destroy()

        self.q1 = tk.Label(self.ventanaBorrarGastos, text="¿Estas Seguro?", font=("Gadugi", 12), bg="#3a3f47", fg="white")
        self.q1.place(x=457, y=183)

        self.botonSi = tk.Button(self.ventanaBorrarGastos, text="   Si   ", bg="#C7C8CA", fg="#000000", command=self.ResultadoBorrar, font=("Tahoma", 12))
        self.botonSi.place(x=447, y=223)

        self.botonNo = tk.Button(self.ventanaBorrarGastos, text="   No   ", bg="#C7C8CA", fg="#000000", command=self.BorrarGastos, font=("Tahoma", 12))
        self.botonNo.place(x=527, y=223) 
    
    def ResultadoBorrar(self):
        
        self.aviso1.destroy()
        self.aviso2.destroy()
        self.q1.destroy()
        self.botonSi.destroy()
        self.botonNo.destroy()


        dia_txt = self.dia_ingreso46.get().strip()
        mes_txt = self.mes_ingreso46.get().strip()
        anio_txt = self.anio_ingreso46.get().strip()
        mes_selec = int(mes_txt) if mes_txt != "" else None
        anio_selec = int(anio_txt) if anio_txt != "" else None
        dia_selec = int(dia_txt) if dia_txt != "" else None

        if dia_selec == None and mes_selec == None and anio_selec != None:
            self.mal4 = tk.Label(self.ventanaBorrarGastos, text="Lo lamento, no se pueden borrar todos los gastos de un año", font=("Gadugi", 12))
            self.mal4.place(x=305, y=260)
            self.mal4.after(1500, self.mal4.destroy)
            return
        elif dia_selec == None and mes_selec == None and anio_selec == None:
            self.mal5 = tk.Label(self.ventanaBorrarGastos, text="Error, ingrese la fecha", font=("Gadugi", 12))
            self.mal5.place(x=435, y=260)
            self.mal5.after(1500, self.mal5.destroy)
            return
        elif int(self.dia_ingreso46.get())>=32 or int(self.dia_ingreso46.get())>=29 and int(self.mes_ingreso46.get())==2:
            self.mal = tk.Label(self.ventanaBorrarGastos, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal.place(x=397, y=260)
            self.mal.after(1500, self.mal.destroy)
        elif int(self.mes_ingreso46.get())>=13:
            self.mal2 = tk.Label(self.ventanaBorrarGastos, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal2.place(x=397, y=590)
            self.mal2.after(1500, self.mal2.destroy)
        elif int(self.anio_ingreso46.get())>=1 and int(self.anio_ingreso46.get())<=2000:
            self.mal3 = tk.Label(self.ventanaBorrarGastos, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal3.place(x=397, y=590)
            self.mal3.after(1500, self.mal3.destroy)
        
        else:

            BASE_DIR = self.get_base_dir()
            self.DB_PATH = os.path.join(BASE_DIR, "gastos.db")

            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()
              
            if dia_selec == None:  
                cursor.execute("""
                    DELETE FROM gastos
                    WHERE mes = ? AND anio = ?
                """, (mes_selec, anio_selec))
            else:
                cursor.execute("""
                DELETE FROM gastos
                WHERE dia = ? AND mes = ? AND anio = ?
                """, (dia_selec, mes_selec, anio_selec))

            borrados = cursor.rowcount
            conn.commit()
            conn.close()

            self.correcto = tk.Label(self.ventanaBorrarGastos, text="Gastos eliminados correctamente", font=("Gadugi", 12))
            self.correcto.place(x=395, y=190)

            self.borradoss = tk.Label(self.ventanaBorrarGastos, text=f"Se eliminaron {borrados} gastos", font=("Gadugi", 12))
            self.borradoss.place(x=430, y=230)

            self.botonOk = tk.Button(self.ventanaBorrarGastos, text="   Ok   ", bg="#C7C8CA", fg="#000000", command=self.BorrarGastos, font=("Tahoma", 12))
            self.botonOk.place(x=483, y=280)

    def AbrirVentanaBorrarPresu(self):
        self.ventanaBorrarPresu = tk.Toplevel(self.ventana)
        self.ventanaBorrarPresu.title("Borrar presupuesto/ingreso")
        self.ventanaBorrarPresu.geometry("1024x768")
        self.ventanaBorrarPresu.configure(bg="#3a3f47")
        self.ventanaBorrarPresu.resizable(False, False)

        self.BorrarPresu()

    def BorrarPresu(self): 
        
        self.fecha_ingreso = tk.Label(self.ventanaBorrarPresu, text="Ingrese la fecha:", font=("Gadugi", 18))
        self.fecha_ingreso.place(x=430, y=25)

        self.mes = tk.Label(self.ventanaBorrarPresu, text="Mes", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.mes.place(x=463, y=85)
        self.mes_ingreso46 = tk.Entry(self.ventanaBorrarPresu, width=4, font=("Gadugi", 12))
        self.mes_ingreso46.place(x=463, y=120)

        self.anio = tk.Label(self.ventanaBorrarPresu, text="Año", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.anio.place(x=530, y=85)
        self.anio_ingreso46 = tk.Entry(self.ventanaBorrarPresu, width=4, font=("Gadugi", 12))
        self.anio_ingreso46.place(x=530, y=120)

        self.barra2 = tk.Label(self.ventanaBorrarPresu, text="/", font=("Gadugi", 14), bg="#3a3f47", fg="white")
        self.barra2.place(x=510, y=118)

        self.botonEnviar = tk.Button(self.ventanaBorrarPresu, text="    Borrar    ", bg="#C7C8CA", fg="#000000", command=self.EstasSeguro2, font=("Tahoma", 12))
        self.botonEnviar.place(x=468, y=183)

        self.aviso1 = tk.Label(self.ventanaBorrarPresu, text="*AVISO: Esto borrara TODO el presupuesto del mes seleccionado*", font=("Gadugi", 12), bg="#3a3f47", fg="white")
        self.aviso1.place(x=283, y=250)

        self.q1.destroy()
        self.botonSi.destroy()
        self.botonNo.destroy()
        self.correcto.destroy()
        self.botonOk.destroy()

    def EstasSeguro2(self):
        self.aviso1.destroy()
        self.botonEnviar.destroy()

        self.q1 = tk.Label(self.ventanaBorrarPresu, text="¿Estas Seguro?", font=("Gadugi", 12), bg="#3a3f47", fg="white")
        self.q1.place(x=460, y=183)

        self.botonSi = tk.Button(self.ventanaBorrarPresu, text="   Si   ", bg="#C7C8CA", fg="#000000", command=self.ResultadoBorrar2, font=("Tahoma", 12))
        self.botonSi.place(x=450, y=223)

        self.botonNo = tk.Button(self.ventanaBorrarPresu, text="   No   ", bg="#C7C8CA", fg="#000000", command=self.BorrarPresu, font=("Tahoma", 12))
        self.botonNo.place(x=530, y=223)

    def ResultadoBorrar2(self):

        self.q1.destroy()
        self.botonSi.destroy()
        self.botonNo.destroy()

        mes_txt = self.mes_ingreso46.get().strip()
        anio_txt = self.anio_ingreso46.get().strip()
        mes_selec = int(mes_txt) if mes_txt != "" else None
        anio_selec = int(anio_txt) if anio_txt != "" else None

        if mes_selec == None and anio_selec != None:
            self.mal4 = tk.Label(self.ventanaBorrarPresu, text="Lo lamento, no se pueden borrar todos los gastos de un año", font=("Gadugi", 12))
            self.mal4.place(x=305, y=260)
            self.mal4.after(1500, self.mal4.destroy)
            return
        elif mes_selec == None and anio_selec == None:
            self.mal5 = tk.Label(self.ventanaBorrarPresu, text="Error, ingrese la fecha", font=("Gadugi", 12))
            self.mal5.place(x=435, y=260)
            self.mal5.after(1500, self.mal5.destroy)
            return
        elif int(self.mes_ingreso46.get())>=13:
            self.mal2 = tk.Label(self.ventanaBorrarPresu, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal2.place(x=397, y=590)
            self.mal2.after(1500, self.mal2.destroy)
        elif int(self.anio_ingreso46.get())>=1 and int(self.anio_ingreso46.get())<=2000:
            self.mal3 = tk.Label(self.ventanaBorrarPresu, text="Error, revise el formato de fecha", font=("Gadugi", 12))
            self.mal3.place(x=397, y=590)
            self.mal3.after(1500, self.mal3.destroy)
        
        else:

            BASE_DIR = self.get_base_dir()
            self.DB_PATH = os.path.join(BASE_DIR, "gastos.db")

            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute("""
            DELETE FROM Ingresos
            WHERE mes = ? AND anio = ?
            """, (mes_selec, anio_selec))

            conn.commit()
            conn.close()

            self.correcto = tk.Label(self.ventanaBorrarPresu, text="Presupuesto eliminado correctamente", font=("Gadugi", 12))
            self.correcto.place(x=383, y=190)
            self.botonOk = tk.Button(self.ventanaBorrarPresu, text="   Ok   ", bg="#C7C8CA", fg="#000000", command=self.BorrarPresu, font=("Tahoma", 12))
            self.botonOk.place(x=483, y=240)
    
    def contacto(self):
        self.ventanaContacto = tk.Toplevel(self.ventana)
        self.ventanaContacto.title("Contacto")
        self.ventanaContacto.geometry("1024x768")
        self.ventanaContacto.configure(bg="#3a3f47")
        self.ventanaContacto.resizable(False, False)


        self.btn_e2 = tk.Label(self.ventanaContacto, text="", bg="#3a3f47", fg="#000000", font=("Gadugi", 34), width=137)
        self.btn_e2.pack(pady=60)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ruta_logo = os.path.join(BASE_DIR, "Logo2.png")

        self.logo = tk.PhotoImage(file=self.ruta_logo)
        label = tk.Label(self.ventanaContacto, image=self.logo, bg="#3a3f47")
        label.pack(pady=1)

        self.btn_e2 = tk.Label(self.ventanaContacto, text="", bg="#3a3f47", fg="#000000", font=("Gadugi", 12), width=137)
        self.btn_e2.pack(pady=5)

        self.btn_e = tk.Label(self.ventanaContacto, text="mntssoftware@gmail.com", bg="#3a3f47", fg="#FFFFFF", font=("Gadugi", 14), width=25)
        self.btn_e.pack(pady=1)


if __name__ == "__main__":
    app = App()
    app.crear_db()
    app.run()