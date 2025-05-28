#!/bin/sh
echo "Borrando archivos de la carpeta backups"
rm -rf /home/lorena/bases/*

echo "Generando archivos .sql"
mysqldump --single-transaction -u root -p0ys4dm1n --opt --routines=TRUE reloj > /home/lorena/bases/relojout.sql;
mysqldump --single-transaction -u root -p0ys4dm1n --opt --routines=TRUE ingreso > /home/lorena/bases/ingresoout.sql;
reloj
