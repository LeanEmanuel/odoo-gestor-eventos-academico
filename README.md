# Gestor de Eventos - Modulo Odoo academico

> Estado del repositorio: proyecto academico / educativo.
>
> Este addon fue desarrollado como practica del ciclo DAM. Se publica como muestra de aprendizaje y portfolio tecnico, no como solucion production-ready.

## Descripcion

`gestor_eventos` es un modulo para Odoo orientado a la gestion basica de eventos para una asociacion o entidad similar. Incluye gestion de eventos, tickets con QR, asistentes, categorias, etiquetas e informacion economica asociada.

El objetivo de este repositorio es documentar una implementacion academica funcional y entendible. Por eso se prioriza la claridad del codigo, la coherencia del modulo y la facilidad de revision por encima de requisitos tipicos de un entorno productivo.

## Alcance funcional

- Alta y gestion de eventos con nombre, fechas, ubicacion, capacidad, categoria y etiquetas.
- Generacion de tickets con codigo unico y QR.
- Generacion masiva de tickets desde el evento.
- Registro de asistentes.
- Control de ingresos y gastos vinculados a eventos.
- Generacion de PDF de tickets.
- Endpoint JSON para validar tickets.

## Aviso importante

Este repo NO pretende cubrir un hardening completo para produccion. Antes de usarlo en un entorno real habria que revisar, entre otras cosas:

- autenticacion y autorizacion de la API publica;
- validaciones funcionales adicionales y manejo de errores;
- estrategia de tests automatizados;
- dependencias, despliegue y observabilidad.

## Nombre tecnico del modulo

El nombre tecnico esperado del addon es `gestor_eventos`.

Aunque el repositorio de GitHub pueda tener otro nombre, la carpeta que copies dentro de `custom_addons` debe llamarse exactamente `gestor_eventos`, porque las referencias internas del modulo usan ese identificador.

Ejemplo recomendado:

```text
custom_addons/
└── gestor_eventos/
```

## Instalacion

1. Copia o clona este repositorio dentro de tu ruta de addons personalizados.
2. Renombra la carpeta a `gestor_eventos` si el checkout local tiene otro nombre.
3. Reinicia el servidor de Odoo.
4. Activa el modo desarrollador.
5. Ve a `Apps > Update Apps List`.
6. Busca `Gestor de Eventos` e instala el modulo.

## Seguridad

El modulo define dos grupos principales:

- `Event User` (`gestor_eventos.group_event_user`): acceso de lectura a la informacion principal del modulo.
- `Event Manager` (`gestor_eventos.group_event_manager`): acceso completo de gestion sobre los modelos del modulo.

Los permisos se declaran en `security/security.xml` y `security/ir.model.access.csv`.

## API de validacion de tickets

La implementacion actual expone un endpoint JSON con metodo `POST`:

```text
/api/ticket/validate
```

Cuerpo esperado:

```json
{
  "code": "ABC1234567"
}
```

Respuesta exitosa:

```json
{
  "message": "Ticket successfully validated"
}
```

Posibles respuestas de error:

```json
{
  "error": "Ticket code is required"
}
```

```json
{
  "error": "Ticket not found"
}
```

```json
{
  "error": "Ticket is not in a valid state for validation"
}
```

Nota: el endpoint esta pensado como demostracion academica. Si se fuera a publicar en un entorno real, convendria protegerlo con autenticacion, rate limiting y validaciones adicionales.

## Estructura principal

- `models/`: modelos de negocio del addon.
- `views/`: vistas y menus de Odoo.
- `controllers/`: controlador HTTP/JSON para validacion de tickets.
- `security/`: grupos y reglas de acceso.
- `static/`: recursos estaticos e imagenes.

## Material academico incluido

El repositorio incluye documentacion y recursos complementarios del trabajo academico, como una memoria en PDF y un video demo. Se mantienen como contexto del proyecto, no como artefactos necesarios para instalar el modulo.

</br>

<div align="center">
  
## 🛠️ Tecnologías y Herramientas 🛠️

</br>

<img alt="odoo" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/odoo.png" width="80"/>  
<img alt="pycharm" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/pycharm.png" width="80"/>
<img alt="python" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png" width="80"/>
<img alt="postman" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/postman.png" width="80"/>
<img alt="postgres" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/postgresql.png" width="80"/>
<img alt="github" src="https://user-images.githubusercontent.com/25181517/192108374-8da61ba1-99ec-41d7-80b8-fb2f7c0a4948.png" width="80"/>


<br>


</div>


---


<table align="center">
  <tr>
    <td>
      <table align="center">
        <tr>
          <td align="center">
            <a href="https://github.com/LeanEmanuel">
              <img src="https://github.com/LeanEmanuel/Images/blob/main/Leandro.png" alt="Mini Leandro" width="80">
            </a>
          </td>
        </tr>
        <tr>
          <td>
            <a href="https://github.com/LeanEmanuel">
              <img src="https://img.shields.io/badge/LeanEmanuel-Git?style=flat&logo=github&logoColor=white&labelColor=black&color=50e520&label=GitHub" alt="Badge">
            </a>
          </td>
        </tr>
    </td>
  </tr>
</table>
