# M7-L7 Consultas

Este proyecto de Django implementa dos aplicaciones principales que trabajan con consultas ORM y SQL. Su propósito es proporcionar ejemplos claros y funcionales de cómo interactuar con una base de datos en Django utilizando ambas técnicas.

## Estructura del Proyecto

```
M7-L7-Consultas/
├── consultas_orm/
│   ├── models.py        # Modelos relacionados con el ORM
│   ├── views.py         # Vistas para consultas ORM
│   ├── urls.py          # Rutas de la aplicación ORM
│   └── templates/       # Plantillas para consultas ORM
├── consultas_sql/
│   ├── models.py        # Modelos relacionados con consultas SQL
│   ├── views.py         # Vistas para consultas SQL
│   ├── urls.py          # Rutas de la aplicación SQL
│   └── templates/       # Plantillas para consultas SQL
├── dataShell.py         # Script para poblar las tablas de la base de datos
├── manage.py            # Script de administración de Django
└── README.md            # Documentación del proyecto
```

---

## Funcionalidades

### Aplicación `consultas_orm`
- **Modelos**:
  - `Cliente`: Representa a un cliente con los campos `nombre`, `apellidos`, `fecha_nacimiento` y `activo`.
- **Vistas**:
  - `todos_clientes`: Muestra todos los clientes.
  - `clientes_activos`: Lista solo los clientes activos.
  - `clientes_rango_fechas`: Filtra clientes nacidos entre 1980 y 2000.
- **Plantillas**:
  - Tablas HTML para mostrar los datos de los clientes.

### Aplicación `consultas_sql`
- **Modelos**:
  - `Factura`: Representa una factura con los campos `cliente_id`, `importe` y `pagada`.
- **Vistas**:
  - `todas_facturas`: Muestra todas las facturas.
  - `facturas_pagadas`: Lista solo las facturas pagadas.
  - `facturas_por_cliente`: Filtra facturas por el ID de un cliente.
- **Plantillas**:
  - Tablas HTML para visualizar las facturas.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/M7-L7-Consultas.git
   cd M7-L7-Consultas
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos en `settings.py`:
   - Asegúrate de tener una base de datos configurada correctamente (por defecto, SQLite).

5. Aplica las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Población de la base de datos:
   ```bash
   python manage.py shell < dataShell.py
   ```

---

## Uso

1. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

2. Accede a las rutas principales:

   - Consultas ORM:
     - Todos los clientes: [http://localhost:8000/consultas-orm/todos/](http://localhost:8000/consultas-orm/todos/)
     - Clientes activos: [http://localhost:8000/consultas-orm/activos/](http://localhost:8000/consultas-orm/activos/)
     - Clientes por rango de fechas: [http://localhost:8000/consultas-orm/rango-fechas/](http://localhost:8000/consultas-orm/rango-fechas/)

   - Consultas SQL:
     - Todas las facturas: [http://localhost:8000/consultas-sql/todas/](http://localhost:8000/consultas-sql/todas/)
     - Facturas pagadas: [http://localhost:8000/consultas-sql/pagadas/](http://localhost:8000/consultas-sql/pagadas/)
     - Facturas por cliente: [http://localhost:8000/consultas-sql/cliente/?cliente_id=1](http://localhost:8000/consultas-sql/cliente/?cliente_id=1)

---

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Django**: Framework web para manejar el backend.
- **SQLite**: Base de datos predeterminada (puedes usar PostgreSQL o MySQL si lo configuras).
- **HTML**: Para las vistas y plantillas.

---

## Mejoras Futuras

- Implementar paginación en las vistas de listados grandes.
- Agregar autenticación para proteger las rutas.
- Crear una interfaz de administración personalizada para manejar los datos.
- Usar formularios para filtrar datos más dinámicamente.

---

## Autor

**Bastián Landskron**  
Desarrollador de software y entusiasta de tecnologías backend.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
