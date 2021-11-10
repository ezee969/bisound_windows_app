from pdf import PDF
from repertorio_de_funciones import numVal,quickWindow,completeTime,layoutHide,getComprobanteShowRow,turnoInsertRow,readTurnDateFilteredRows,readCompDateFilteredRow,readRowsMinDate,readFilteredRows
from layouts import proseguirTurnoLayout,proseguirComprobanteLayout,layoutMadre
from datetime import datetime
import sqlite3 as sql
import subprocess
import os
import PySimpleGUI as sg

##MAIN FUNC
def main(firstWindow):
    
    def mainMenu(window):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED,"Salír"):break
            elif event==("<< Atrás"):
                layoutHide(window['-COL2-'],window['-COL1-'])
            elif event==("<< Atrás0"):
                layoutHide(window['-COL3-'],window['-COL2-'])
            elif event==("<< Atrás1"):
                layoutHide(window['-COL4-'],window['-COL2-'])
            elif event==("<< Atrás2"):
                layoutHide(window['-COL5-'],window['-COL1-'])
            elif event==("<< Atrás4"):
                layoutHide(window['-COL6-'],window['-COL5-'])
            elif event==("<< Atrás9"):
                layoutHide(window['-COL7-'],window['-COL5-'])
            elif event==("Turnos"):
                layoutHide(window['-COL1-'],window['-COL2-'])
            elif event==("Agendar nuevo turno"):
                layoutHide(window['-COL2-'],window['-COL3-'])
            elif event==("Ver turnos"):
                layoutHide(window['-COL2-'],window['-COL4-'])
            elif event==("Comprobantes"):
                layoutHide(window['-COL1-'],window['-COL5-'])
            elif event==("Generar comprobante"):
                layoutHide(window['-COL5-'],window['-COL6-'])
            elif event==("Ver comprobantes"):
                layoutHide(window['-COL5-'],window['-COL7-'])
            elif event==("Agendar turno"):
                if values['-nombreCliente0-']=="" or values['-ApellidoCliente0-']=="" or values['-CALIN0-']=="" or values['-marcaAuto0-']=="" or values['-añoAuto0-']=="" or values['-observacionesAuto0-']=="" or values['-SPIN0-']=="" or values['-SPIN1-']=="" or values["-modeloAuto0-"]=="" or values["-celCliente0-"]=="":
                    sg.popup("ERROR","Hay campos vacios")
                elif numVal(values['-celCliente0-'],"entero")==False:
                    sg.popup("ERROR","El celular solo puede contener numeros.")
                elif numVal(values['-añoAuto0-'],"entero",max=9999)==False:
                    sg.popup("ERROR","El año solo puede contener numeros.")
                elif numVal(values['-SPIN0-'],"entero",min=0,max=23)==False:
                    sg.popup("ERROR","La hora solo puede contener numeros en el rango de 0-23.")
                elif numVal(values['-SPIN1-'],"entero",min=0,max=59)==False:
                    sg.popup("ERROR","El minuto solo puede contener numeros en el rango de 0-59.")
                else:
                    comprobacionTurno = sg.Window(
                                        "BISOUND - Comprobación",
                                        proseguirTurnoLayout("generar"),
                                        font="Helvetica, 12",
                                        location=(800, 400),
                                        background_color="#231F20",
                                        button_color=('#178B10','#E7E7E7'),
                                        element_justification="c",
                                        size=(400,150)
                                        )
                    if comprobacion(comprobacionTurno)=="si0":
                        turnoInsertRow(values["-CALIN0-"],completeTime(str(values["-SPIN0-"])+":"+str(values["-SPIN1-"]))
                                    ,values["-nombreCliente0-"],values["-ApellidoCliente0-"],values["-celCliente0-"],
                                    values["-marcaAuto0-"],values["-modeloAuto0-"],
                                    values["-añoAuto0-"],values["-observacionesAuto0-"])
                        sg.popup("Turno agendado con exito",background_color="#231F20")
                        window["-listaTurnos-"].update(readRowsMinDate(datetime.today().strftime('%Y/%m/%d')))
                        window["-CALIN00-"].update("Seleccione fecha en el calendario")
                        window["-SPIN0-"].update(0)
                        window["-SPIN1-"].update(0)
                        clearData(values,window)
                        comprobacionTurno.close()
                        cantTurnosUpdate(window)
            elif event==("Generar comprobante3"):
                if values['-nombreCliente1-']=="" or values['-ApellidoCliente1-']=="" or values['-celCliente1-']=="" or values['-CALIN1-']=="" or values['-marcaAuto1-']=="" or values['-modeloAuto1-']=="" or values['-añoAuto1-']=="" or values['-observacionesAuto1-']=="" or values['-trabajoAuto-']=="" or values['-presupuestoAuto-']=="":
                    sg.popup("ERROR","Hay campos vacios",any_key_closes=True,background_color="#231F20")
                elif numVal(values['-celCliente1-'],"entero")==False:
                    sg.popup("ERROR","El celular solo puede contener numeros.",any_key_closes=True,background_color="#231F20")
                elif numVal(values['-añoAuto1-'],"entero",max=9999)==False:
                    sg.popup("ERROR","El año solo puede contener numeros.",any_key_closes=True,background_color="#231F20")
                elif numVal(values["-presupuestoAuto-"],"entero")==False:
                    sg.popup("ERROR","El presupuesto solo puede contener numeros.",any_key_closes=True,background_color="#231F20")            
                else:
                    comprobacionComprobante = sg.Window("BISOUND - Comprobación",
                            proseguirComprobanteLayout("generar"),
                            font="Helvetica",
                            location=(800, 400),
                            background_color="#231F20",
                            button_color=('#178B10','#E7E7E7'),
                            element_justification="c",
                            size=(400,150))
                    if comprobacion(comprobacionComprobante)=="si0":
                        sg.popup("Comprobante generado",any_key_closes=True,background_color="#231F20")
                        comprobacionComprobante.close()
                        comprobanteInsertRow(
                                            values["-CALIN1-"],values["-nombreCliente1-"],
                                            values["-ApellidoCliente1-"],values["-celCliente1-"],
                                            values["-marcaAuto1-"],values["-modeloAuto1-"],
                                            values["-añoAuto1-"],values["-patenteAuto-"],
                                            values["-observacionesAuto1-"],values["-trabajoAuto-"]
                                            ,values["-presupuestoAuto-"],len(getAllComprobantes())+1)
                        window["-listaComprobantes-"].update(getComprobanteShowRow())
                        window["-CALIN01-"].update("Seleccione fecha en el calendario")
                        clearData(values,window)
                    comprobacionComprobante.close()
            elif event=="-CALIN0-":
                window["-CALIN00-"].update(values["-CALIN0-"])
            elif event=="-CALIN1-":
                window["-CALIN01-"].update(values["-CALIN1-"])
            elif event=="-CALIN2-":
                window["-CALIN02-"].update(values["-CALIN2-"])
                window["-listaTurnos-"].update(readTurnDateFilteredRows(values["-CALIN2-"]))
            elif event=="Ver todo":
                window["-listaTurnos-"].update(readRowsMinDate(datetime.today().strftime('%Y/%m/%d')))  
                window["-CALIN02-"].update("TODOS")
            elif event=="-CALIN3-":
                window["-CALIN03-"].update(values["-CALIN3-"])
                window["-listaComprobantes-"].update(readCompDateFilteredRow(values["-CALIN3-"]))       
            elif event=="Ver todo5":
                window["-listaComprobantes-"].update(getComprobanteShowRow())
                window["-CALIN03-"].update("TODOS")
            elif event=="Ver":
                try:
                    expInfo(searchTurnRow(values["-listaTurnos-"])) 
                except:
                   sg.Popup("No selecciono ningun turno",any_key_closes=True,background_color="#231F20")
            elif event=="Borrar":
                try: 
                    comprobacionTurno = sg.Window(
                                        "BISOUND - Comprobación",
                                        proseguirTurnoLayout("eliminar"),
                                        font="Helvetica 14",
                                        location=(400, 300),
                                        element_justification="c",
                                        size=(400,150),background_color="#231F20",
                                            button_color=('#178B10','#E7E7E7')
                                        )
                    if comprobacion(comprobacionTurno)=="si0":
                        deleteTurnRow(values["-listaTurnos-"])
                        window["-listaTurnos-"].update(readRowsMinDate(datetime.today().strftime('%Y/%m/%d')))
                        cantTurnosUpdate(window)
                        window["-CALIN02-"].update("TODOS")
                except:
                    sg.Popup("No selecciono ningun turno",any_key_closes=True,background_color="#231F20")
            elif event=="Ver6":
                try:
                    comprobanteExpInfo(searchCompRow(values["-listaComprobantes-"]))
                except:
                   sg.Popup("No selecciono ningun comprobante",any_key_closes=True,background_color="#231F20")
            elif event=="Editar":
                try:
                    if editInfo(searchTurnRow(values["-listaTurnos-"]))=="si":
                        sg.Popup("Turno editado con exito",any_key_closes=True,background_color="#231F20")
                        window["-listaTurnos-"].update(readRowsMinDate(datetime.today().strftime("%Y/%m/%d")))
                        window["-CALIN02-"].update("TODOS")
                except:
                   sg.Popup("No selecciono ningun turno",any_key_closes=True,background_color="#231F20")
            elif event=="Editar7":
                try:
                    if editCompInfo(searchCompRow(values["-listaComprobantes-"]))=="si":
                        sg.Popup("Comprobante editado con exito",any_key_closes=True,background_color="#231F20")
                        window["-listaComprobantes-"].update(getComprobanteShowRow())
                        window["-CALIN03-"].update("TODOS")
                except:
                    sg.Popup("No seleccionó ningun comprobante",any_key_closes=True,background_color="#231F20")
            elif event=="Borrar8":
                try:
                    comprobacionTurno = sg.Window(
                                            "BISOUND - Comprobación",
                                            proseguirComprobanteLayout("eliminar"),
                                            font="Helvetica 14",
                                            location=(600, 300),
                                            background_color="#231F20",
                                            button_color=('#178B10','#E7E7E7'),
                                            element_justification="c",
                                            size=(400,150)
                                            )
                    if comprobacion(comprobacionTurno)=="si0":
                        deleteCompRow(values["-listaComprobantes-"])
                        window["-listaComprobantes-"].update(getComprobanteShowRow())
                        window["-CALIN03-"].update("TODOS")
                except:
                    sg.Popup("No seleccionó ningun comprobante",any_key_closes=True,background_color="#231F20")
            elif event=="Generar PDF":
                try:
                    if generarPDF(searchCompRow(values["-listaComprobantes-"]))=="si":
                        sg.Popup("PDF generado con exito",any_key_closes=True,background_color="#231F20")
                except:
                    sg.Popup("No seleccionó ningun comprobante",any_key_closes=True,background_color="#231F20")
            
    def clearData(values,window):
        for k in values:
            if k!="-listaTurnos-" and k!="-listaComprobantes-" and k!="_CALENDAR0_" and k!="_CALENDAR1_" and k!="_CALENDAR2_" and k!="_CALENDAR3_" and k!="-SPIN0-" and k!="-SPIN1-" and k!='_CALENDAR01_':
                window[k].update("")                                        

    def comprobacion(window):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED,"No"):
                window.close()
                break
            elif event=="Si":
                window.close()
                return "si0"

    def expInfo(data):
        def expandirTurnoLayout():
            filas=[
                    [
                    sg.Text("Turno:",font = ("Helvetica", 20,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.T(f"{data[0][0]}",font = ("Helvetica", 20,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.T(" - ", font = ("Helvetica", 20),pad=((4,4),(15,25)),background_color="#231F20"),
                    sg.T(f"{data[0][1]}",font = ("Helvetica", 20,"bold"),pad=((5,0),(15,25)),background_color="#231F20")
                    ],
                    [sg.Text("Informacion del cliente",background_color="#231F20",font = ("Helvetica", 18,'bold'),pad=((5,0),(20,10)),)],
                    [sg.Text("Nombre del cliente: ",background_color="#231F20"),sg.T(f"{data[0][2]}",background_color="#231F20")],
                    [sg.Text("Apellido del cliente: ",background_color="#231F20"),sg.T(f"{data[0][3]}",background_color="#231F20")],
                    [sg.Text("Celular del cliente: ",background_color="#231F20"),sg.T(f"{data[0][4]}",background_color="#231F20")],
                    [sg.Text("Informacion del vehiculo",font = ("Helvetica", 18,'bold'),pad=((5,0),(30,10)),background_color="#231F20")],
                    [sg.Text("Marca:",pad=((5,13),(0,0)),background_color="#231F20"),sg.T(f"{data[0][5]}",background_color="#231F20")],
                    [sg.Text("Modelo:",background_color="#231F20"),sg.T(f"{data[0][6]}",background_color="#231F20")],
                    [sg.Text("Año:",pad=((5,28),(0,0)),background_color="#231F20"),sg.T(f"{data[0][7]}",background_color="#231F20")],
                    [sg.Text("Observaciones: ",background_color="#231F20")],
                    [sg.Multiline(f"{data[0][8]}",disabled=True,border_width=5,size=(75,5),pad=((5,0),(10,0)),font=("Helvetica",13))],
                    [sg.Button("Cerrar",size=(11,1),pad=((30,0),(35,0)),font = ("Helvetica", 18),border_width=3)]
                ]
            return filas
    
        expandirTurno = sg.Window(
                        "BISOUND - Informacion de turno",
                        expandirTurnoLayout(),
                        font=("Helvetica",16),
                        background_color="#231F20",
                        location=(250, 80),
                        element_justification="c",
                        size=(900,700),button_color=('#178B10','#E7E7E7')
                        )
        quickWindow(expandirTurno)
            
    def editInfo(data):
        
        def editarTurnoLayout():
            filas=[
                    [
                    sg.Text("Turno:",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.T(f"{data[0][0]}", key="fechaReemplazo4",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.T(" - ", font = ("Helvetica", 16),pad=((4,4),(15,25)),background_color="#231F20"),
                    sg.T(f"{data[0][1]}", key="horaRemplazo4",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.Input(f"{data[0][0]}",key="-CALIN4-",visible=False,enable_events=True)
                    ],
                    [
                    sg.CalendarButton(  'Editar fecha', target='-CALIN4-',
                                        pad=((30,0),(0,0)), font=('Helvetica', 14,"bold"),
                                        key='_CALENDAR4_', format=('%Y/%m/%d') ,border_width=3 ),
                    ],
                    [
                    sg.T("Editar hora del turno:",pad=((5,25),(10,0)),background_color="#231F20"),
                    sg.Spin([i for i in range(0,24)], initial_value=data[0][1][0:2],key="-SPIN2-",pad=((0,3),(10,0))),
                    sg.T(":",font=("Arial",16,"bold"),pad=((0,0),(5,0)),background_color="#231F20"),
                    sg.Spin([i for i in range(0,61,5)], initial_value=data[0][1][3:5],key="-SPIN3-",pad=((3,0),(10,0)))
                    ],
                    [sg.Text("Informacion del cliente",font = ("Helvetica", 14,'bold'),pad=((5,0),(20,10)),background_color="#231F20")],
                    [sg.Text("Nombre del cliente: ",background_color="#231F20"),sg.Input(f"{data[0][2]}",key="nombreTurnoEditar")],
                    [sg.Text("Apellido del cliente: ",background_color="#231F20"),sg.Input(f"{data[0][3]}",key="apellidoTurnoEditar")],
                    [sg.Text("Celular del cliente: ",pad=((0,16),(0,0)),background_color="#231F20"),sg.Input(f"{data[0][4]}",key="celularTurnoEditar")],
                    [sg.Text("Informacion del vehiculo",font = ("Helvetica", 14,'bold'),pad=((5,0),(30,10)),background_color="#231F20")],
                    [sg.Text("Marca:",pad=((5,13),(0,0)),background_color="#231F20"),sg.Input(f"{data[0][5]}",key="marcaTurnoEditar")],
                    [sg.Text("Modelo:",background_color="#231F20"),sg.Input(f"{data[0][6]}",key="modeloTurnoEditar")],
                    [sg.Text("Año:",pad=((5,36),(0,0)),background_color="#231F20"),sg.Input(f"{data[0][7]}",key="añoTurnoEditar")],
                    [sg.Text("Observaciones: ",background_color="#231F20")],
                    [sg.Multiline(f"{data[0][8]}",size=(70, 8), key="observacionesTurnoEditar")],
                    [sg.Button("Cerrar",size=(11,1),pad=((30,0),(35,0)),font = ("Helvetica", 14,"bold"),border_width=3),sg.Button("Guardar",size=(11,1),pad=((30,0),(35,0)),font = ("Helvetica", 14,"bold"),border_width=3)],
                ]
            return filas

        editarTurno = sg.Window(
                        "BISOUND - Editar turno",
                        editarTurnoLayout(),
                        font=("Helvetica",16),
                        background_color="#231F20",
                        location=(150, 80),
                        element_justification="c",
                        size=(1100,800),button_color=('#178B10','#E7E7E7')
                        )

        while True:
            event, values = editarTurno.read()
            if event in (sg.WIN_CLOSED,"Cerrar"):
                editarTurno.close()
                break   
            elif event=="Guardar":
                if values['nombreTurnoEditar']=="" or values['apellidoTurnoEditar']=="" or values['celularTurnoEditar']=="" or values['marcaTurnoEditar']=="" or values["modeloTurnoEditar"]=="" or values['añoTurnoEditar']=="" or values['observacionesTurnoEditar']=="" or values['-SPIN2-']=="" or values['-SPIN3-']=="":
                    sg.popup("ERROR","Hay campos vacios",any_key_closes=True,background_color="#231F20")
                elif numVal(values["celularTurnoEditar"],"entero")==False:
                    sg.popup("ERROR","El celular solo puede contener numeros.",any_key_closes=True,background_color="#231F20")
                elif numVal(values['añoTurnoEditar'],"entero",max=9999)==False:
                    sg.popup("ERROR","El año solo puede contener numeros.",any_key_closes=True,background_color="#231F20")
                elif numVal(values['-SPIN2-'],"entero",min=0,max=23)==False:
                    sg.popup("ERROR","La hora solo puede contener numeros en el rango de 0-23.",any_key_closes=True,background_color="#231F20")
                elif numVal(values['-SPIN3-'],"entero",min=0,max=59)==False:
                    sg.popup("ERROR","El minuto solo puede contener numeros en el rango de 0-59.",any_key_closes=True,background_color="#231F20")
                else:
                    updateTurnRow(data,values)
                    editarTurno.close()
                    return "si"
            elif event=="-CALIN4-":
                editarTurno["fechaReemplazo4"].update(values["-CALIN4-"])
    
    def cantTurnosUpdate(window):
        window["cantidadTurnos0"].update(len(readFilteredRows(datetime.today().strftime('%d/%m/%Y'))))
        window["cantidadTurnos1"].update(len(readFilteredRows(datetime.today().strftime('%d/%m/%Y'))))
        window["cantidadTurnos2"].update(len(readFilteredRows(datetime.today().strftime('%d/%m/%Y'))))
        window["cantidadTurnos3"].update(len(readFilteredRows(datetime.today().strftime('%d/%m/%Y'))))

    def searchTurnRow(listaDeTupla):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''SELECT * FROM Turnos
                    WHERE fecha=? AND hora=? AND nombre=? AND apellido=? AND marca=? AND modelo=?''',(listaDeTupla[0][0],listaDeTupla[0][1],listaDeTupla[0][2],listaDeTupla[0][3],listaDeTupla[0][4],listaDeTupla[0][5]))
        rows=c.fetchall()
        conn.close()
        return rows
    
    def searchCompRow(listaDeTupla):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''SELECT * FROM Comprobantes
                    WHERE numero=? AND fecha=? AND nombre=? AND apellido=? AND marca=? AND modelo=? AND presupuesto=?''',(listaDeTupla[0][0],listaDeTupla[0][1],listaDeTupla[0][2],listaDeTupla[0][3],listaDeTupla[0][4],listaDeTupla[0][5],listaDeTupla[0][6]))
        rows=c.fetchall()
        conn.close()
        return rows
    
    def updateTurnRow(data,values):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''UPDATE Turnos SET fecha=?, hora=?, nombre=?, apellido=?, celular=?, marca=?, modelo=?, anio=?, observaciones=? WHERE fecha=? AND hora=? AND nombre=? AND apellido=? AND celular=? AND marca=? AND modelo=? AND anio=? AND observaciones=?''',(values["-CALIN4-"],completeTime(str(values["-SPIN2-"])+":"+str(values["-SPIN3-"])),values["nombreTurnoEditar"],values["apellidoTurnoEditar"],values["celularTurnoEditar"],values["marcaTurnoEditar"],values["modeloTurnoEditar"],values["añoTurnoEditar"],values["observacionesTurnoEditar"],data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8]))
        conn.commit()
        conn.close()

    def deleteTurnRow(data):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''DELETE FROM Turnos WHERE fecha=? AND hora=? AND nombre=? AND apellido=? AND marca=? AND modelo=?''',(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5]))
        conn.commit()
        conn.close()

    def comprobanteInsertRow(fecha,nombre,apellido,celular,marca,modelo,anio,patente,observaciones,trabajo,presupuesto,numero):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''INSERT INTO Comprobantes (fecha,nombre,apellido,celular,marca,modelo,anio,patente,observaciones,trabajo,presupuesto,numero) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',(fecha,nombre,apellido,celular,marca,modelo,anio,patente,observaciones,trabajo,presupuesto,numero))
        conn.commit()
        conn.close()

    def getAllComprobantes():
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''SELECT * FROM Comprobantes''')
        rows=c.fetchall()
        conn.close()
        return rows

    def comprobanteExpInfo(data):
        
        def expandirComprobanteLayout():
            filas=[
                    [
                    sg.Text("Fecha de ingreso:",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.T(f"{data[0][0]}",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20")
                    ],
                    [sg.Text("Informacion del cliente",font = ("Helvetica", 16,'bold'),pad=((5,0),(20,10)),background_color="#231F20")],
                    [sg.Text("Nombre del cliente: ",background_color="#231F20"),sg.T(f"{data[0][1]}",pad=((5,0),(0,0)),background_color="#231F20")],
                    [sg.Text("Apellido del cliente: ",pad=((22,6),(5,5)),background_color="#231F20"),sg.T(f"{data[0][2]}",pad=((5,0),(5,5)),background_color="#231F20")],
                    [sg.Text("Celular del cliente: ",pad=((54,0),(0,0)),background_color="#231F20"),sg.T(f"{data[0][3]}",pad=((15,0),(0,0)),background_color="#231F20")],
                    [sg.Text("Informacion del vehiculo",font = ("Helvetica", 16,'bold'),pad=((5,0),(30,10)),background_color="#231F20")],
                    [sg.Text("Marca:",pad=((5,14),(0,0)),background_color="#231F20"),sg.T(f"{data[0][4]}",background_color="#231F20")],
                    [sg.Text("Modelo:",pad=((31,4),(0,0)),background_color="#231F20"),sg.T(f"{data[0][5]}",background_color="#231F20")],
                    [sg.Text("Año:",pad=((8,34),(0,0)),background_color="#231F20"),sg.T(f"{data[0][6]}",background_color="#231F20")],
                    [sg.Text("Patente:",pad=((29,3),(0,0)),background_color="#231F20"),sg.T(f"{data[0][7]}",background_color="#231F20")],
                    [sg.Text("Observaciones: ",pad=((0,630),(0,0)),background_color="#231F20")],
                    [sg.Multiline(f"{data[0][8]}",disabled=True,border_width=5,size=(75,5),pad=((5,0),(10,0)),font=("Helvetica",13))],
                    [sg.Text("Trabajo:",pad=((0,700),(15,0)),background_color="#231F20")],
                    [sg.Multiline(f"{data[0][9]}",disabled=True,border_width=5,size=(75,5),pad=((5,0),(10,0)),font=("Helvetica",13))],
                    [sg.Text(f"Presupuesto: {data[0][10]}",pad=(5,15),background_color="#231F20")],
                    
                    [sg.Button("Cerrar",size=(11,1),pad=((30,0),(65,0)),font = ("Helvetica", 14, 'bold'),border_width=3)],
            ]
            return filas 
        
        expandirComprobante = sg.Window(
                                "BISOUND - Informacion de comprobante",
                                expandirComprobanteLayout(),
                                font=("Helvetica",14),
                                location=(230, 10),background_color="#231F20",
                                element_justification="c",
                                size=(900,900),button_color=('#178B10','#E7E7E7')
                                )
        quickWindow(expandirComprobante)

    def editCompInfo(data):
        
        def editarComprobanteLayout():
            filas=[
                    [
                    sg.Text("Fecha de ingreso:",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.T(f"{data[0][0]}", key="fechaReemplazo5",font = ("Helvetica", 16,"bold"),pad=((5,0),(15,25)),background_color="#231F20"),
                    sg.Input(f"{data[0][0]}",key="-CALIN5-",visible=False,enable_events=True)
                    ],
                    [
                    sg.CalendarButton(  'Editar fecha', target='-CALIN5-',
                                        pad=((30,0),(0,0)), font=('Arial', 14),
                                        key='_CALENDAR5_', format=('%Y/%m/%d') ,border_width=3 ),
                    ],
                    [sg.Text("Informacion del cliente",font = ("Helvetica", 14,'bold'),pad=((5,0),(20,10)),background_color="#231F20")],
                    [sg.Text("Nombre del cliente:",background_color="#231F20"),sg.Input(f"{data[0][1]}",key="nombreComproRemp",)],
                    [sg.Text("Apellido del cliente:",background_color="#231F20"),sg.Input(f"{data[0][2]}",key="apellidoComproRemp")],
                    [sg.Text("Celular del cliente:",background_color="#231F20"),sg.Input(f"{data[0][3]}",key="celularComproRemp")],
                    [sg.Text("Informacion del vehiculo",font = ("Helvetica", 14,'bold'),pad=((5,0),(30,10)),background_color="#231F20")],
                    [sg.Text("Marca:",pad=((5,13),(0,5)),background_color="#231F20"),sg.Input(f"{data[0][4]}",key="marcaComproRemp")],
                    [sg.Text("Modelo:",pad=((5,4),(0,5)),background_color="#231F20"),sg.Input(f"{data[0][5]}",key="modeloComproRemp")],
                    [sg.Text("Año:",pad=((5,28),(0,5)),background_color="#231F20"),sg.Input(f"{data[0][6]}",key="añoComproRemp")],
                    [sg.Text("Patente:",pad=((5,3),(0,5)),background_color="#231F20"),sg.Input(f"{data[0][7]}",key="patenteComproRemp")],
                    [sg.Text("Observaciones: ",background_color="#231F20")],
                    [sg.Multiline(f"{data[0][8]}",size=(100, 4), key="observacionesComproRemp")],
                    [sg.Text("Trabajo:",background_color="#231F20")],
                    [sg.Multiline(f"{data[0][9]}",size=(100, 4), key="trabajoComproRemp")],
                    [sg.Text("Presupuesto:",pad=((5,0),(5,0)),background_color="#231F20"),sg.Input(f"{data[0][10]}",key="presupuestoComproRemp")],
                    [sg.Button("Cerrar",size=(11,1),pad=((30,0),(75,0)),font = ("Helvetica", 14,"bold"),border_width=3),sg.Button("Guardar",size=(11,1),pad=((30,0),(75,0)),font = ("Helvetica", 14,"bold"),border_width=3)],
            ]
            return filas
        
        editarComprobante = sg.Window(
                        "BISOUND - Editar comprobante",
                        editarComprobanteLayout(),background_color="#231F20",
                        font="Helvetica",
                        location=(80, 10),
                        element_justification="c",
                        size=(1150,900),
                        button_color=('#178B10','#E7E7E7')
                        )
        
        while True:
            event, values = editarComprobante.read()
            if event in (sg.WIN_CLOSED,"Cerrar"):
                editarComprobante.close()
                break
            elif event=="Guardar":
                if values["nombreComproRemp"]=="" or values["apellidoComproRemp"]=="" or values["celularComproRemp"]=="" or values['marcaComproRemp']=="" or values["modeloComproRemp"]=="" or values['añoComproRemp']=="" or values['observacionesComproRemp']=="" or values['trabajoComproRemp']=="" or values['presupuestoComproRemp']=="":
                    sg.popup("ERROR","Hay campos vacios",any_key_closes=True,background_color="#231F20")
                elif numVal(values["celularComproRemp"],"entero")==False:
                    sg.popup("ERROR","El celular solo puede contener numeros.",any_key_closes=True,background_color="#231F20")
                elif numVal(values['añoComproRemp'],"entero",max=9999)==False:
                    sg.popup("ERROR","El año solo puede contener numeros.",any_key_closes=True,background_color="#231F20")
                else:
                    updateCompRow(data,values)
                    editarComprobante.close()
                    return "si"
            elif event=="-CALIN5-":
                editarComprobante["fechaReemplazo5"].update(values["-CALIN5-"])
            print(event)
    
    def updateCompRow(data,values):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''UPDATE Comprobantes SET fecha=?, nombre=?, apellido=?, celular=?, marca=?, modelo=?, anio=?, patente=?, observaciones=?, trabajo=?, presupuesto=?
                 WHERE fecha=? AND nombre=? AND apellido=? AND celular=? AND marca=? AND modelo=? AND anio=? AND patente=? AND observaciones=? AND trabajo=? AND presupuesto=?''',
                 (values["-CALIN5-"],values["nombreComproRemp"],values["apellidoComproRemp"],values["celularComproRemp"],values["marcaComproRemp"],values["modeloComproRemp"],
                 values["añoComproRemp"],values["patenteComproRemp"],values["observacionesComproRemp"],values["trabajoComproRemp"],values["presupuestoComproRemp"],data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10]))
        conn.commit()
        conn.close()

    def deleteCompRow(data):
        conn=sql.connect('database.db')
        c=conn.cursor()
        c.execute('''DELETE FROM Comprobantes WHERE numero=? AND fecha=? AND nombre=? AND apellido=? AND marca=? AND modelo=? AND presupuesto=?''',(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6]))
        conn.commit()
        conn.close()
    
    def generarPDF(data):

        def generarPdfLayout():
            filas=          [
                            [sg.FolderBrowse("Seleccione carpeta",
                                            key="abrirCarpetaPdf",
                                            size=(15,1),
                                            pad=((5,10),(15,0)),
                                            font=("Helvetica", 14,"bold"),
                                            button_color=('#178B10','#E7E7E7'),
                                            initial_folder=""),
                            sg.Input(key="carpetaPdf",size=(40,1),
                                    pad=((0,0),(15,0)),font=("Helvetica", 14,"bold"),
                                    disabled=True),
                            ],
                            [sg.Button('Generar',font=("Helvetica",14,"bold"),
                                     pad=((60,35),(20,0)),size=(10,1),
                                     button_color=('#178B10','#E7E7E7')),
                             sg.Button('Cancelar',font=("Helvetica",14,"bold"),
                                     pad=((10,0),(20,0)),button_color=('#178B10','#E7E7E7'),
                                     size=(10,1),)]
                            ]
            return filas
        
        generarPdfWindow = sg.Window(
                            'BISOUND - Generar PDF', 
                            generarPdfLayout(),
                            size=(420,120),background_color="#231F20",
                            font=('Helvetica', 14),
                            button_color="#231F20",
                            element_justification='c')
        while True:
            event, values = generarPdfWindow.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                print(values)
                generarPdfWindow.close()
                break
            if event == 'Generar' and values['abrirCarpetaPdf']!="":
                archivo=PDF(f"bisound_comp_{data[0][1]}{data[0][2]}_n{data[0][11]}.pdf",data,data[0][11],values["carpetaPdf"])
                archivo.setPage()
                archivo.setLines()
                archivo.setHeader()
                archivo.setBody()
                archivo.pdfOutput()
                try:
                    os.startfile(f"{values['carpetaPdf']}/bisound_comp_{data[0][1]}{data[0][2]}_n{data[0][11]}.pdf")
                except:
                    subprocess.call(["xdg-open", f"{values['carpetaPdf']}/bisound_comp_{data[0][1]}{data[0][2]}_n{data[0][11]}.pdf"])
                generarPdfWindow.close()
                return "si"
            else:
                sg.popup("ERROR","Seleccione una carpeta",any_key_closes=True,background_color="#231F20")
    mainMenu(firstWindow)

if __name__ == "__main__":
    menuPrincipal = sg.Window("BISOUND - ADMINISTRADOR",
                            layoutMadre(),
                            button_color=('#178B10','#E7E7E7'),
                            background_color="#231F20",
                            location=(0, 0),
                            font=("Helvetica",13),
                            size=(1250,920))
    
    main(menuPrincipal)
    menuPrincipal.close()
