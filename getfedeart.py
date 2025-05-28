from sendmail import Correo
from conectDB import sqlDB
from datetime import datetime

def ejecSQL(leg):
    # Obtener la fecha actual
    fecha_actual = datetime.now().date()

    # Convertir la fecha a una cadena con el formato especificado
    fecha_str = fecha_actual.strftime("%d-%m-%Y")

    # Parsear la cadena a un objeto datetime
    fecha_parseada = datetime.strptime(fecha_str, "%d-%m-%Y")

    # Obtener el mes y el año como enteros
    m = fecha_parseada.month
    a = fecha_parseada.year
    d = fecha_parseada.day

    sql = sqlDB()
    
    sql.connect()
    results = []
    query = "CALL call_reporteByAgent(%s, %s, %s, %s);"

    try:
        sql.cursor.execute(query, (leg, m, a,d))
        results = sql.cursor.fetchall()
        while sql.cursor.nextset():
            pass
        sql.db.commit()
    except Exception as e:
        print("ERROR: SQL -> CALL call_reporteByAgent('%s','%s','%s','%s');" % (leg, m, a, d))
        print("Error de la base de datos:", str(e))  # Muestra el mensaje de error de la base de datos
        return []
    finally:
        sql.close()
    return results


    
  
def createContent(data,title):
    fecha = datetime.now().date().strftime("%d-%m-%Y")
    # Crear una tabla HTML con los datos de la lista de personas
    table_html = "<table cellspacing='4' cellpadding='4' style='border: 1px solid #87CEFA; border-collapse: collapse;'>"
    table_html += "<tr>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Departamento</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Nro de usuario</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>ID</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Nombre</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Tipo</th>"
    table_html += "<th style='background-color: #F0F0F0; text-align: center; border: 1px solid #87CEFA;'>Descripcion</th>"
    table_html += "</tr>"
    for row in data:
        table_html += '<tr>'
        for col in row:
            if (col =="None"): col=""
            table_html += f'<td style="color: #333; border: 1px solid #87CEFA;">{col}</td>'
        table_html += '</tr>'
    table_html += '</table>'
  
    body = f'<h1>{title} - Fecha Reporte: {fecha} </h1><br/>\n\n{table_html}'
    return body
    

  
def sendReporteFede():
    leg=5392
    results = ejecSQL(leg)
    # Convierte los resultados en una lista de listas
    data = [list(row) for row in results]
    title ='Parte diario - Federico Laureano '
    body  = createContent(data,title)
    fecha = datetime.now().date().strftime("%d-%m-%Y")
    subject = f'{title} -   {fecha}'
    sendMial = Correo()
    sendMial.sender ="mlgarcia@unsa.edu.ar"
    sendMial.subject= subject
    sendMial.recipient="mglorena@gmail.com"
    sendMial.body =body
    sendMial.title =title
    sendMial.sendMail()


sendReporteFede()