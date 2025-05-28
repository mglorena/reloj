from sendmail import Correo
from conectDB import sqlDB
import datetime
from datetime import timedelta

def ejecSQL():
    sql = sqlDB()
    sql.connect()
    query = "CALL personas_getReporteTarde();"
    try:
        sql.cursor.execute(query)
        results = sql.cursor.fetchall()
        while sql.cursor.nextset():
            pass
        sql.db.commit()
    except:
        print("ERROR: SQL -> " + query)
        sql.db.rollback()
    sql.close()
    return results


    
  
def createContent(data,turno, title,t1,t2,t3):
    fecha = datetime.datetime.now().strftime("%d-%m-%Y")

    # Crear una tabla HTML con los datos de la lista de personas
    table_html = "<table cellspacing='4' cellpadding='4' style='border: 1px solid #87CEFA; border-collapse: collapse;'>"
    table_html += "<tr>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Nombre</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Legajo</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Cargo</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Categoría</th>"
    if(t1 == ""):
        table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Articulo</th>"
        table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Descripcion</th>"
        table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Fecha Articulo</th>"
    if(t1 != ""):
        table_html += f'<th style="background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;"">{t1}</th>'
        table_html += f'<th style="background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;"">{t2}</th>'
        table_html += f'<th style="background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;"">{t3}</th>'
    table_html += "</tr>"
    for row in data:
        table_html += '<tr>'
        for col in row:
            if (col =="None"): col=""
            table_html += f'<td style="color: #333; border: 1px solid #87CEFA;">{col}</td>'
        table_html += '</tr>'
    table_html += '</table>'
  
    body = f'<h1>{title} - Fecha Reporte: {fecha} </h1><br/><h2>Turno {turno}:</h2>\n\n{table_html}'
    return body
    

  
def sendReporte7horas():
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    restar = timedelta(days=1)
    # Restar un día a la fecha actual
    fecha_anterior = fecha_actual - restar

# Obtener el día de la semana de la fecha anterior (0 es lunes, 6 es domingo)
    dia_semana = fecha_anterior.weekday()
    if dia_semana == 5 or dia_semana == 6:
        print("El día anterior fue sábado o domingo. No se ejecutará el script.")
    # Aquí podrías evitar ejecutar el resto del código o hacer otras acciones necesarias
    else:
        print("El día anterior no fue sábado ni domingo. Se puede ejecutar el script.")
        # Aquí puedes poner el código que deseas ejecutar si no es sábado ni domingo
        results = ejecSQL()
        # Convierte los resultados en una lista de listas
        data = [list(row) for row in results]
        turno_actual = "Todos"
        title ='Horas cumplidas dia de ayer '
        body  = createContent(data,turno_actual,title,"Entrada","Salida","Horas cumplidas")
        fecha = datetime.datetime.now().strftime("%d-%m-%Y")
        subject = f'{title} -   {fecha}'
        sendMial = Correo()
        sendMial.sender ="mlgarcia@unsa.edu.ar"
        sendMial.subject= subject
        sendMial.recipient="mglorena@gmail.com"
        sendMial.body =body
        sendMial.title =title
        sendMial.sendMail()


sendReporte7horas()