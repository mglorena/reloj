#!/bin/sh
echo "Backups apps"
cd /home/lorena/backups
rm -rf back-*.tgz 

echo "Iniciando copia de carpeta reloj"
    if tty -s
       then
        if (tar -zcf back-reloj-$(date +%F).tgz /home/lorena/reloj/*)
        then 
                :
                else 
                    echo Error comprimiendo /home/lorena/reloj 1>&2
        fi
    fi
echo "Iniciando copia de carpeta scripts"
    if tty -s
       then
       if (tar -zcf back-scripts-$(date +%F).tgz /home/lorena/scrips/*)
       then 
               :
               else 
                   echo Error comprimiendo scripts 1>&2
       fi
    fi
echo "Iniciando copia de carpeta ingreso"
    if tty -s
       then
       if (tar -zcf back-ingreso-$(date +%F).tgz /home/lorena/ingreso/*)
       then 
               :
               else 
                   echo Error comprimiendo ingreso 1>&2
       fi
    fi

exit 1