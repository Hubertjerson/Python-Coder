# <h1 style="text-align: center;">Nuestro primer MVT</h1>

---

## <h3>Crear una web que permite ver los datos de algunos de tus familiares, guardados en un BD.</h3>

#### <li>Deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)</li>
#### <li>La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)</li>
#### <li>Se deberán crear como mínimo 3 familiares</li>
#### <li>Los familiares se deben ver desde la web.</li>

---

<h2>Sugerencia</h2>
<h3> Forma de Guardar Poner Datos de familiares desde la Consola </h3>

    "py manage.py shell"
        // Importamos el modelo de nuestra base de datos
            from familia.models import Familia
                // Forma de agregar familiares
                    family_member = Familia (nombre='nombre de la persona', apellido='apellido de la persona', edad='edad de la persona')
                        // Guardamos en la Base de datos
                            family_member.save()
                                // Salir de Consola
                                    exit()

<h3>Forma de correr el servidor (Consola)</h3>

    //Activamos
        . start.py
            //Correr el servidor
                py manage.py runserver

<h3>Starting development server at http://127.0.0.1:8000/</h3>