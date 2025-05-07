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



