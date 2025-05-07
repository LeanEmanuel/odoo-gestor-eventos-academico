# Gestor de Eventos - Módulo Odoo

Este módulo ha sido desarrollado para la práctica **M10-UF2-PR01** del ciclo DAM. Permite gestionar eventos para una asociación de vecinos, incluyendo creación de entradas, asistencia, ingresos y gastos, así como generación de tickets con código QR.

## ✨ Funcionalidades principales

- Gestión completa de eventos: nombre, fechas, ubicación, capacidad, cartel, categoría y etiquetas.
- Gestión de entradas (tickets) con códigos QR únicos.
- Generación masiva de entradas por evento.
- Generación de PDF personalizado con código QR e imagen del evento.
- Control de ingresos y gastos asociados a eventos.
- Validación de entradas mediante API pública (usando Postman o app móvil).
- Seguridad granular por grupos de usuario (usuarios y gestores de eventos).

## 🚀 Instalación

1. Copia la carpeta `gestor_eventos` dentro de `custom_addons/`.
2. Reinicia el servidor de Odoo.
3. Activa el modo desarrollador.
4. Ve a **Apps > Actualizar lista**.
5. Busca **Gestor de Eventos** e instala el módulo.

## 🔐 Seguridad

El módulo define dos grupos:
- `Event User` (`gestor_eventos.group_event_user`): puede ver los eventos.
- `Event Manager` (`gestor_eventos.group_event_manager`): puede crear y modificar todo.

Los permisos se configuran mediante `security.xml` e `ir.model.access.csv`.

## 🧾 API de validación de tickets

Puedes validar tickets escaneando un código QR con esta URL: </br>
GET /gestor_eventos/api/ticket/validate/<ticket_code>

### ✅ Ejemplo de respuesta (válido)
```json
{
    "jsonrpc": "2.0",
    "id": null,
    "result": {
        "message": "Ticket successfully validated"
    }
}
```

<div align="center">
    
### 🛠️ Tecnologías y Herramientas 🛠️

</br>

<img alt="github" src="https://user-images.githubusercontent.com/25181517/192108374-8da61ba1-99ec-41d7-80b8-fb2f7c0a4948.png" width="80"/>  
<img alt="unity" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/unity.png" width="80"/>
<img alt="pycharm" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/pycharm.png" width="80"/>
<img alt="c#" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/c%23.png" width="80"/>
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

