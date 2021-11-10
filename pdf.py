from fpdf import FPDF
class PDF(FPDF):

        def __init__(self,name,data,compNum,path,orientation="portrait", unit="mm", format="A4"):

                super().__init__(orientation=orientation, unit=unit, format=format)
                self.data = data
                self.compNum = compNum
                self.path = path
                self.name = name
        
        def setPage(self):

                self.add_page()
                self.set_auto_page_break(auto=True)

        def setLines(self):

                self.set_line_width(0.0)
                self.line(70,30,205,30)
                self.line(5.0,5.0,205.0,5.0) 
                self.line(5.0,292.0,205.0,292.0)
                self.line(5.0,5.0,5.0,292.0) 
                self.line(205.0,5.0,205.0,292.0)
                self.line(115,275,173,275)     

        def setHeader(self):

                self.image("logoResized.png",x=10,y=10,w=70.0,h=25.0)
                self.set_font('Helvetica','B',13)
                self.cell(120)
                self.cell(0,5,f"Comprobante N°{self.compNum}",ln=1,align='C')
                self.cell(120)
                self.cell(0,10,"Fecha: "+self.data[0][0],ln=1,align='C')
                self.ln(15) 
        
        def setBody(self):
                
                self.cell(92,17,txt="Datos del cliente")
                self.cell(0,17,txt="Informacion del vehiculo",ln=1)
                self.cell(23,10,txt="Nombre: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(69,h=10,txt=self.data[0][1],border=1)
                self.set_font('Helvetica','B',13)
                self.cell(23,10,txt="Marca: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(0,10,txt=self.data[0][4],ln=1,border=1)
                self.set_font('Helvetica','B',13)
                self.cell(23,10,txt="Apellido: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(69,h=10,txt=self.data[0][2],border=1)
                self.set_font('Helvetica','B',13)
                self.cell(23,10,txt="Modelo: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(0,10,txt=self.data[0][5],ln=1,border=1)
                self.set_font('Helvetica','B',13)
                self.cell(23,10,txt="Celular: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(69,h=10,txt=str(self.data[0][3]),border=1)
                self.set_font('Helvetica','B',13)
                self.cell(23,10,txt="Año: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(0,10,txt=str(self.data[0][6]),ln=1,border=1)
                self.set_font('Helvetica','B',13)
                self.cell(92,h=10)
                self.cell(23,10,txt="Patente: ",border=1)
                self.set_font('Helvetica','',13)
                self.cell(0,10,txt=self.data[0][7],ln=1,border=1)
                self.ln(10)
                self.set_font('Helvetica','B',13)
                self.cell(23,10,txt="Observaciones: ",ln=1)
                self.set_font('Helvetica','',13)
                self.multi_cell(185,10,txt=(self.data[0][8]).ljust(450),ln=1,border=1)#ln=1
                self.ln(10) 
                self.set_font('Helvetica','B',13)
                self.cell(200,10,txt="Trabajo: ",ln=1)
                self.set_font('Helvetica','',13)
                self.multi_cell(185,h=10,txt=(self.data[0][9]).ljust(450),ln=1,border=1)#ln=1
                self.ln(20)
                self.set_font('Helvetica','B',13)
                self.cell(35,10,txt="Presupuesto: $")
                self.set_font('Helvetica','',13)
                self.cell(45,h=10,txt=str(self.data[0][10]),ln=1,border=1)
                self.ln(30)
                self.cell(120,10)
                self.cell(0,10,txt="Firma cliente",ln=1) 
        
        def pdfOutput(self):

            self.output(rf"{self.path}/{self.name}")