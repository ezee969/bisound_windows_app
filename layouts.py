import PySimpleGUI as sg
from repertorio_de_funciones import readFilteredRows,readRowsMinDate,getComprobanteShowRow
from datetime import datetime
##LAYOUTS MAIN MENU
def mainMenuLayout():

    filas = [
        [   
            sg.Text(f"Turnos para el dia {datetime.today().strftime('%d/%m/%Y')}: ",pad=((5,0),(10,30)),background_color="#231F20"),
            sg.T(f"{len(readFilteredRows(datetime.today().strftime('%Y/%m/%d')))}", key="cantidadTurnos0",pad=((10,0),(10,30)),background_color="#231F20")
        ],
        [sg.Image(filename="logoResized.png",pad=((400,0),(90,40)))],
        [sg.Button("Turnos",size=(25,2),border_width=6,font = ("Helvetica", 15,"bold"),pad=((505,0),(0,20)))],
        [sg.Button("Comprobantes",size=(25,2),border_width=6,font = ("Helvetica", 15,"bold"),pad=((505,0),(0,20)))],
        [sg.Button("Salír",size=(25,2),border_width=6,font = ("Helvetica", 15,"bold"),pad=((505,0),(0,0)))],
    ]
    return filas

##LAYOUTS TURNOS
def turnosMainLayout():
    filas = [
        [
            sg.Text(f"Turnos para el dia {datetime.today().strftime('%d/%m/%Y')}: ",pad=((5,0),(10,30)),background_color="#231F20"),
            sg.T(f"{len(readFilteredRows(datetime.today().strftime('%Y/%m/%d')))}", key="cantidadTurnos1",pad=((10,0),(10,30)),background_color="#231F20")
        ],
        [sg.T("BISOUND TURNOS", font = ("Helvetica", 30,"bold"),pad=((490,0),(120,60)),background_color="#231F20")],
        [sg.Button("Agendar nuevo turno",border_width=6,size=(25,2),font = ("Helvetica", 15,"bold"),pad=((520,0),(0,20)))],
        [sg.Button("Ver turnos",border_width=6,size=(25,2),font = ("Helvetica", 15,"bold"),pad=((520,0),(0,20)))],
        [
            sg.Button("<< Atrás",border_width=3,size=(10,1),pad=((26,0),(330,5)),font = ("Helvetica", 14,"bold")),
        ]
    ]
    return filas

def turnosAgendarLayout():
    filas = [
            [
                sg.Text(f"Turnos para el dia {datetime.today().strftime('%d/%m/%Y')}: ",pad=((5,0),(10,30)),background_color="#231F20"),
            sg.T(f"{len(readFilteredRows(datetime.today().strftime('%Y/%m/%d')))}", key="cantidadTurnos2",pad=((10,0),(10,30)),background_color="#231F20")
            ],
            [   
                sg.Text("Fecha del turno:",pad=((5,30),(0,0)),background_color="#231F20"),
                sg.Text("Seleccione fecha en el calendario",key='-CALIN00-',background_color="#231F20"),
                sg.Input(key="-CALIN0-",visible=False,enable_events=True)     
            ],
            [
                sg.CalendarButton('Calendario', target="-CALIN0-",enable_events=True, font=('Helvetica', 12, 'bold'),
                key='_CALENDAR0_', format=('%Y/%m/%d'),border_width=3)
            ],
            [
                sg.T("Hora del turno:",pad=((5,25),(10,0)),background_color="#231F20"),
                sg.Spin([i for i in range(0,24)], initial_value=0,key="-SPIN0-",pad=((0,3),(10,0))),
                sg.T(":",font=("Arial",16,"bold"),pad=((0,0),(5,0)),background_color="#231F20"),
                sg.Spin([i for i in range(0,61,5)], initial_value=0,key="-SPIN1-",pad=((3,0),(10,0)))
            ],
            [sg.Text("Informacion del cliente",font = ("Helvetica", 14,'bold'),pad=((5,0),(20,10)),background_color="#231F20")],
            [sg.Text("Nombre del cliente: ",pad=((5,12),(0,0)),background_color="#231F20"),sg.Input(key="-nombreCliente0-")],
            [sg.Text("Apellido del cliente: ",pad=((5,12),(0,0)),background_color="#231F20"),sg.Input(key="-ApellidoCliente0-")],
            [sg.Text("Numero de contacto:",background_color="#231F20"),sg.Input(key="-celCliente0-")],
            [sg.Text("Informacion del vehiculo",font = ("Helvetica", 14,'bold'),pad=((5,0),(30,10)),background_color="#231F20")],
            [sg.Text("Marca:",pad=((5,13),(0,0)),background_color="#231F20"),sg.Input(key="-marcaAuto0-")],
            [sg.Text("Modelo:",background_color="#231F20"),sg.Input(key="-modeloAuto0-")],
            [sg.Text("Año:",pad=((5,28),(0,0)),background_color="#231F20"),sg.Input(key="-añoAuto0-")],
            [sg.Text("Observaciones: ",background_color="#231F20")],
            [sg.Multiline(size=(120, 10), key="-observacionesAuto0-")],
            [sg.Button("Agendar turno",font = ("Helvetica", 13,'bold'),border_width=3,pad=((10,0),(30,65)))],
            [sg.Button("<< Atrás",size=(10,1),pad=((26,0),(0,0)),font = ("Helvetica", 14,"bold"),border_width=3)]             
    ]
    return filas

def proseguirTurnoLayout(palabra):
    filas = [
        [sg.Text(f"¿Desea {palabra} turno?",pad=((0,0),(20,0)),background_color="#231F20")],
        [
            sg.Button("Si",pad=((0,20),(30,0)),size=(5,1),font = ("Helvetica", 12,'bold'),border_width=3,),
            sg.Button("No",pad=((0,0),(30,0)),size=(5,1),font = ("Helvetica", 12,'bold'),border_width=3)]
        ]
    return filas

def verTurnosLayout():
    filas = [
            [
                sg.Text(f"Turnos para el dia {datetime.today().strftime('%d/%m/%Y')}: ",pad=((5,0),(10,30)),background_color="#231F20"),
                sg.T(f"{len(readFilteredRows(datetime.today().strftime('%Y/%m/%d')))}", key="cantidadTurnos3",pad=((10,0),(10,30)),background_color="#231F20")
            ],
            [
                sg.Text("TURNOS:",font = ("Helvetica", 20,'bold'),pad=((520,0),(60,10)),background_color="#231F20"),
                sg.T("TODOS", key="-CALIN02-",font = ("Helvetica", 20,"bold"),pad=((0,0),(60,10)),background_color="#231F20"),
                sg.Input(key="-CALIN2-",visible=False,enable_events=True),    
            ],
            [
                sg.T("Filtros:",font = ("Helvetica", 14,"bold"),pad=((380,0),(0,0)),background_color="#231F20"),    
                sg.CalendarButton('Filtrar por fecha', target='-CALIN2-',
                pad=((30,0),(0,0)), font=('Helvetica', 14,"bold"),
                key='_CALENDAR2_', format=('%Y/%m/%d'),border_width=3),
                sg.Button("Ver todo",size=(11,1),pad=((30,0),(0,0)),font = ("Helvetica", 14,"bold"),border_width=3),
            ],
            [sg.Listbox(values=readRowsMinDate(datetime.today().strftime("%Y/%m/%d")), size=(60, 20), key='-listaTurnos-', enable_events=True,pad=((330,0),(20,20)))],
            [
            sg.Button("Ver",size=(11,1),pad=((365,0),(0,0)),font = ("Helvetica", 14,"bold"),border_width=3),
            sg.Button("Editar",size=(11,1),pad=((30,0),(0,0)),font = ("Helvetica", 14,"bold"),border_width=3),
            sg.Button("Borrar",size=(11,1),pad=((30,0),(0,0)),font = ("Helvetica", 14,"bold"),border_width=3)
            ],  
             [
             sg.Button("<< Atrás",size=(10,1),pad=((30,0),(115,0)),font = ("Helvetica", 14,"bold"),border_width=3)
            ]
    ]
    return filas

##LAYOUTS COMPROBANTES
def comprobantesMainLayout():
    filas = [
        [sg.T("BISOUND COMPROBANTES", font = ("Helvetica", 30,"bold"),pad=((410,0),(160,60)),background_color="#231F20")],
        [sg.Button("Generar comprobante",size=(25,2),font = ("Helvetica", 15,"bold"),pad=((520,0),(0,20)),border_width=6)],
        [sg.Button("Ver comprobantes",size=(25,2),font = ("Helvetica", 15,"bold"),pad=((520,0),(0,20)),border_width=6)],
        [sg.Button("<< Atrás",size=(10,1),pad=((30,0),(380,0)),font = ("Helvetica", 14,"bold"),border_width=3)]
    ]
    return filas

def generarComprobanteLayout():
    filas = [
        [sg.Text("Informacion del cliente",font = ("Helvetica", 14,'bold'),pad=((5,0),(20,10)),background_color="#231F20")],
            [sg.Text("Nombre del cliente:",background_color="#231F20"),sg.Input(key="-nombreCliente1-")],
            [sg.Text("Apellido del cliente:",background_color="#231F20"),sg.Input(key="-ApellidoCliente1-")],
            [sg.Text("Celular del cliente:",background_color="#231F20",pad=((5,11),(0,0))),sg.Input(key="-celCliente1-")],
            
            [   
                sg.Text("Fecha de ingreso:",pad=((5,30),(0,0)),background_color="#231F20"),
                sg.Text("Seleccione fecha en el calendario",key='-CALIN01-',font = ("Helvetica", 12),background_color="#231F20"),
                sg.Input(key="-CALIN1-",visible=False,enable_events=True)     
            ],
            [
                sg.CalendarButton('Calendario', target="-CALIN1-",enable_events=True,pad=((10,0),(8,0)), font=('Helvetica', 12, 'bold'),
                key='_CALENDAR01_', format=('%Y/%m/%d'),border_width=3)
            ],

            [sg.Text("Informacion del vehiculo",font = ("Helvetica", 14,'bold'),pad=((5,0),(30,10)),background_color="#231F20")],
            [sg.Text("Marca:",pad=((5,11),(0,5)),background_color="#231F20"),sg.Input(key="-marcaAuto1-")],
            [sg.Text("Modelo:",pad=((5,5),(0,5)),background_color="#231F20"),sg.Input(key="-modeloAuto1-")],
            [sg.Text("Año:",pad=((5,28),(0,5)),background_color="#231F20"),sg.Input(key="-añoAuto1-")],
            [sg.Text("Patente:",pad=((5,2),(0,5)),background_color="#231F20"),sg.Input(key="-patenteAuto-")],
            [sg.Text("Observaciones: ",background_color="#231F20")],
            [sg.Multiline(size=(120, 6), key="-observacionesAuto1-",border_width=3)],
            [sg.Text("Trabajo:",background_color="#231F20")],
            [sg.Multiline(size=(120, 6), key="-trabajoAuto-",border_width=3)],
            [sg.Text("Presupuesto:",pad=((5,0),(5,0)),background_color="#231F20"),sg.Input(key="-presupuestoAuto-")],
            [sg.Button("Generar comprobante",font = ("Helvetica", 13,'bold'),pad=((5,0),(30,30)),border_width=3)],
            [sg.Button("<< Atrás",size=(10,1),pad=((20,0),(0,0)),font = ("Helvetica", 14, 'bold'),border_width=3)]
    ]
    return filas

def verComprobantesLayout():
    filas = [    
                [
                    sg.Text("COMPROBANTES:",font = ("Helvetica", 20,'bold'),pad=((460,0),(60,10)),background_color="#231F20"),
                    sg.T("TODOS", key="-CALIN03-",font = ("Helvetica", 20,"bold"),pad=((0,0),(60,10)),background_color="#231F20")    
                ],
                [
                    sg.T("Filtros:",font = ("Helvetica", 14,"bold"),pad=((380,0),(0,0)),background_color="#231F20"),    
                    sg.In(key='-CALIN3-', enable_events=True, visible=False),
                    sg.CalendarButton('Filtrar por fecha', target='-CALIN3-',
                    pad=((30,0),(0,0)), font=('Helvetica', 14, 'bold'),
                    key='_CALENDAR3_', format=('%Y/%m/%d'),border_width=3),
                    sg.Button("Ver todo",size=(11,1),pad=((30,0),(0,0)),font = ("Helvetica", 14, 'bold'),border_width=3),
                ],
                [sg.Listbox(values=getComprobanteShowRow(), size=(70, 25), key='-listaComprobantes-', enable_events=True,pad=((290,0),(20,20)))],
                [
                    sg.Button("Ver",size=(11,1),pad=((287,0),(10,0)),font = ("Helvetica", 14, 'bold'),border_width=3),
                    sg.Button("Editar",size=(11,1),pad=((30,0),(10,0)),font = ("Helvetica", 14, 'bold'),border_width=3),
                    sg.Button("Borrar",size=(11,1),pad=((30,0),(10,0)),font = ("Helvetica", 14, 'bold'),border_width=3),
                    sg.Button("Generar PDF",size=(11,1),pad=((30,0),(10,0)),font = ("Helvetica", 14, 'bold'),border_width=3)
                ],  
                [sg.Button("<< Atrás",size=(10,1),pad=((28,0),(94,15)),font = ("Helvetica", 14, 'bold'),border_width=3)]
            ]
    return filas

def proseguirComprobanteLayout(palabra):
    filas = [
            [sg.Text(f"¿Desea {palabra} comprobante?",pad=((0,0),(20,0)),background_color="#231F20")],
            [
            sg.Button("Si",pad=((0,20),(30,0)),size=(5,1),font = ("Helvetica", 12, 'bold'),border_width=3),
            sg.Button("No",pad=((0,0),(30,0)),size=(5,1),font = ("Helvetica", 12, 'bold'),border_width=3)]
            ]
    return filas

def layoutMadre():
    filas=  [
            [
            #sg.TabGroup([
            sg.Column(mainMenuLayout(),visible=True, key='-COL1-',background_color="#231F20"), 
            sg.Column(turnosMainLayout(), visible=False, key='-COL2-',background_color="#231F20"), 
            sg.Column(turnosAgendarLayout(), visible=False, key='-COL3-',background_color="#231F20"),
            sg.Column(verTurnosLayout(), visible=False, key='-COL4-',background_color="#231F20"),
            sg.Column(comprobantesMainLayout(), visible=False, key='-COL5-',background_color="#231F20"),
            sg.Column(generarComprobanteLayout(), visible=False, key='-COL6-',background_color="#231F20"),
            sg.Column(verComprobantesLayout(), visible=False, key='-COL7-',background_color="#231F20"),
            ]
            ]
    return filas

