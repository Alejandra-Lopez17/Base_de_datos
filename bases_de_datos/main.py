from unittest import result
import mysql.connector

#Nuestra conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "rh"
)

cursor = database.cursor(buffered=True)

#Probamos la conexión
#try:
#    print(f"Felicidades tiene conexión: {database}")
#except:
#    print("Tu conexión esta fallando")

# try:
#     cursor = database.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS coltis_python")
#     cursor.execute("SHOW DATABASES")

#     for basesDatos in cursor:
#         print(basesDatos)
# except:
#     print("La creación de la base de datos a fallado")
#Creación de tablas
# try:
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS estudiante (
#         id int ( 12 ) auto_increment not null ,
#         nombre varchar ( 55 ) not null ,
#         apellido varchar ( 55 ) not null ,
#         celular varchar ( 12 ) not null ,
#         CONSTRAINT pk_estudiante PRIMARY KEY ( id )
#     )
#     """)
#     print("Funcionado")
# except:
#     print("Error al crear la tabla")

# cursor.execute("SHOW TABLES")

# for tables in cursor:
#     print(tables)

#Insertar un dato
# try:
#     cursor.execute("INSERT INTO estudiante VALUES(null, 'Juan' , 'Triana', '3209524521')")
#     print("Dato guardado")
# except:
#     print("Tu inserción de datos ha fallado")

#Insertar multiples
# try:
#     estudiantes = [
#         ('Johan', 'Gordillo', '322222222'),
#         ('Emilia', 'Rubio', '33333333'),
#         ('Cesar', '', '3444444')
#     ]

#     cursor.executemany("INSERT INTO estudiante VALUES(null, %s , %s, %s)",estudiantes)
#     print("Datos guardado")
# except:
#     print("Tu inserción multiple de datos ha fallado")

#Consultas
# try:
#     cursor.execute("SELECT * FROM estudiante")

#     result = cursor.fetchall()

#     print("Estudiantes")
#     for estudiantes in result:
#         print(estudiantes)
# except:
#     print("Fallo de consulta")


#Eliminar simple
# try:
#     cursor.execute("DELETE FROM estudiante WHERE id = 2")
#     database.commit()
#     print("Eliminacion exitosa")
# except:
#     print("Fallo al eliminar")

#Actualizar
try:
    cursor.execute("UPDATE estudiante SET apellido = 'Turmeque' WHERE id = 1")
    database.commit()
    print("Actualizacion exitosa")
except:
    print("Fallo al Actualizacion")
