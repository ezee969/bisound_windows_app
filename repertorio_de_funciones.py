from math import inf
def inputNumber(mensaje,tipo,min=0,max=inf):
    #input de numero con validacion
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero" and (int(numero)>=min and int(numero)<=max):
                numero = int(numero)
                validado=True
            elif tipo == "real" and (float(numero)>=min and float(numero)<=max):
                numero = float(numero)
                validado=True
        except:
            print("Error. Your number does not match the requirements.")
    return numero

def numVal(num,type,min=0,max=inf):
    #valida un numero segun el tipo y el rango
    
    try:
        if type=="entero" and (int(num)>=min and int(num)<=max):
            num=int(num)
            return True
        elif type=="real" and (float(num)>=min and float(num)<=max):
            num=float(num)
            return True
    except:
        return False

from datetime import date
def formatoFechaVal():
    #FUNCION validacion de formato fecha dd/mm/yyyy                       
    validado=False
    while validado==False:
        try: 
            fecha=input("Enter a date(dd/mm/yyyy): ")
            dia=int(fecha[:2])
            mes=int(fecha[3:5])
            anio=int(fecha[6:10])
            dia=fecha[:2]
            mes=fecha[3:5]
            anio=fecha[6:10]
            if fecha[2]!="/" or fecha[5]!="/":
                print("Make sure to enter the date using the dd/mm/yyyy format you dumb fuck!")
            else:
                validado=True
        except:
            print("Make sure to enter the date using the dd/mm/yyyy format you dumb fuck!")
    return(dia,mes,anio) 

from datetime import date
def formatoFechaValPecho(fecha):
    #FUNCION validacion de formato fecha dd/mm/yyyy                       
    validado=False
    while validado==False:
        try: 
            dia=int(fecha[:2])
            mes=int(fecha[3:5])
            anio=int(fecha[6:10])
            dia=fecha[:2]
            mes=fecha[3:5]
            anio=fecha[6:10]
            if fecha[2]!="/" or fecha[5]!="/":
                print("Make sure to enter the date using the dd/mm/yyyy format you dumb fuck!")
            else:
                validado=True
        except:
            print("Make sure to enter the date using the dd/mm/yyyy format you dumb fuck!")
    return(dia,mes,anio)     

def valFecha(fecha):
    #validacion de fecha.Toma tupla yyyy/mm/dd 
    if int(fecha[1])<1 or int(fecha[1])>12 or int(fecha[0])<1 or int(fecha[0])>31 or ((int(fecha[1])==4 or int(fecha[1])==6 or int(fecha[1])==9 or int(fecha[1])==11) and int(fecha[0])>30) or (int(fecha[0])>29 and int(fecha[1])==2) or ((int(fecha[0])==29 and int(fecha[1])==2) and ((int(fecha[2])%100==0 and int(fecha[2])%400!=0) or (int(fecha[2])%100!=0 and int(fecha[2])%4!=0))):
        result="WRONG DATE."
    else:
        fechaFormato=""
        for x in reversed(fecha):
            fechaFormato=fechaFormato+str(x)+"/"
        result=fechaFormato[:-1]
    return result

from datetime import date
def calculate_age(born):
    today = date.today()
    return today.year - born[6:] - ((today.month, today.day) < (born[3:5], born[0:2]))

def lenValIn(mensaje,min=0,max=inf):    
    #input de strings (validar largo por mínimo y/o máximo)
    vali=False
    while vali==False:
        strIn=input(mensaje)
        if len(strIn)<min or len(strIn)>max:
            print("Non validated.")
        else:
            vali=True
    return strIn

def valHora(mensaje):
    #input de hora con validacion de formato y hora. 
    validado=False 
    while not validado:
        hora=input(mensaje)
        try:
            if (int(hora[0:2])>=00 and int(hora[0:2])<=23) and (int(hora[3:5])>=00 and int(hora[3:5])<=59) and hora[2]==":":
                validado=True
        except:
            print("Hora incorrecta.")
    return hora

def cantRenglones(archivoTxt):
    #lee los dos archivos de texto y cuenta la cantidad de tareas que poseen en conjunto
    cont=0
    with open(archivoTxt) as file:
                line=file.readline()
                while line:
                    line=file.readline()
                    cont+=1
    return cont

def eliminarRenglon(archivoTxt,numeroDeRenglon):
    #Eliminar renglon especifico de Txt
    with open(archivoTxt) as file:    
        lines=file.readlines()
        del lines[numeroDeRenglon-1]
    with open(archivoTxt,"w") as file:
        for line in lines:
            file.write(line)

from os import system, name
def clear(): #clear de menu
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
#<<<<<<<----------------INTERFAZ GRAFICA GUI----------------->>>>>>>>>

import PySimpleGUI as sg

def quickWindow(window):
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED,"Cerrar"):
            window.close()
            break

def main(window):
    while True:
        event, values = window.read()
        if event in (None, "Quit"):break
        #print(event, values)

def validate_input(window, values, msg):  # Define la validacion de los datos ingresados
    vD = {"entero": int, "real": float}
    for k, v in values.items():
        tipo = k.split("_")[0]
        if tipo in vD:
            try:
                vD[tipo](v)
                window[msg].update(value="")
            except:
                window[msg].update(value=f"Error: Debe ser un {tipo}")
                window[k].set_focus()
                return False
    return True

def layoutHide(currentLayout,nextLayout):
    currentLayout.update(visible=False)
    nextLayout.update(visible=True)

def backwards(currentLayout,lastLayout):
    currentLayout.update(visible=False)
    lastLayout.update(visible=True)
    

def dateToNumber(date):
    
    def monthToNumber(month):
        if month=="January":
            return "01"
        elif month=="February":
            return "02"
        elif month=="March":
            return "03"
        elif month=="April":
            return "04"
        elif month=="May":
            return "05"
        elif month=="June":
            return "06"
        elif month=="July":
            return "07"
        elif month=="August":
            return "08"
        elif month=="September":
            return "09"
        elif month=="October":
            return "10"
        elif month=="November":
            return "11"
        elif month=="December":
            return "12"

    datePartida=date.split(" ")
    return (f"{datePartida[0]}/{monthToNumber(datePartida[1][:-1])}/{datePartida[2]}")

def posClick(listaDatos,listaDatosParaMostrar):
    for x in listaDatos:
        if listaDatosParaMostrar[0][0] in x and listaDatosParaMostrar[0][1] in x and listaDatosParaMostrar[0][2] in x and listaDatosParaMostrar[0][3] in x:
            pos=listaDatos.index(x)
    return pos
 
def completeTime(time):
    if len(time.split(":")[0])==1:
        time=f"0{time}"
    if len(time.split(":")[1])==1:
        time=f"{time.split(':')[0]}:0{time.split(':')[1]}"        
    return time 

##########------SQLITE3-----#########
import sqlite3 as sql

def createDB(name):
    #crea una base de datos con el nombre que se le pasa
    conn = sql.connect(name)
    conn.close()

def turnoInsertRow(fecha, hora, nombre, apellido, celular, marca, modelo, anio, observaciones):
    conn = sql.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO Turnos VALUES(?,?,?,?,?,?,?,?,?)
        ''', (fecha, hora, nombre, apellido, celular, marca, modelo, anio, observaciones))
    conn.commit()
    conn.close()

def readFilteredRows(filter):
    #reads all rows that match the filter
    conn = sql.connect('database.db')
    c = conn.cursor()
    c.execute('''
        SELECT * FROM Turnos WHERE fecha = ?
        ''', (filter,))
    rows = c.fetchall()
    conn.close()
    return rows

def readTurnDateFilteredRows(filter):
    #reads all rows that match the filter
    conn = sql.connect('database.db')
    c = conn.cursor()
    c.execute('''
        SELECT fecha,hora,nombre,apellido,marca,modelo FROM Turnos WHERE fecha = ?
        ''', (filter,))
    rows = c.fetchall()
    conn.close()
    return rows

def readRowsMinDate(date):
    #sqlite read rows with minium date
    conn=sql.connect('database.db')
    c=conn.cursor()
    c.execute('''SELECT fecha,hora,nombre,apellido,marca,modelo FROM Turnos
                WHERE fecha >= ?
                ORDER BY fecha,hora''',(date,))
    rows=c.fetchall()
    conn.close()
    return rows

def getComprobanteShowRow():
    #selecciona las filas fecha nombre marca modelo presupuesto
    conn=sql.connect('database.db')
    c=conn.cursor()
    c.execute('''SELECT numero,fecha,nombre,apellido,marca,modelo,presupuesto FROM Comprobantes''')
    rows=c.fetchall()
    conn.close()
    return rows

def readCompDateFilteredRow(fecha):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''SELECT numero,fecha,nombre,apellido,marca,modelo,presupuesto FROM Comprobantes WHERE fecha=?''',(fecha,))
        rows=c.fetchall()
        conn.close()
        return rows