# Documento – Sistema de Pedidos Web

**Proyecto:** Sistema de Gestión de Pedidos
**Tecnologías utilizadas:** Python (Flask), HTML, JavaScript, Git
**Metodología:** Enfoque ágil tipo Scrum
**Herramienta de gestión:** Trello

---

# Requerimientos del Cliente

El cliente solicitó un sistema web simple para gestionar pedidos en un local de comida, con las siguientes funcionalidades:

Crear pedidos
Visualizar pedidos
Cambiar el estado de los pedidos (Pendiente, En preparación, Entregado)

### Restricciones:

No requiere autenticación de usuarios
No incluye sistema de pagos
Debe ser simple y fácil de usar

# Casos de Uso

1. Crear pedido
2. Ver pedidos
3. Cambiar estado del pedido

#  Escenarios

### Caso de uso: Crear pedido

 Dado que el usuario está en el sistema
 Cuando ingresa el nombre del cliente y selecciona productos
 Entonces el sistema crea el pedido con el total calculado

### Caso de uso: Ver pedidos

 Dado que existen pedidos registrados
 Cuando el usuario accede a la lista de pedidos
 Entonces el sistema muestra todos los pedidos


### Caso de uso: Cambiar estado del pedido

 Dado que existe un pedido
 Cuando el usuario cambia su estado
 Entonces el sistema actualiza correctamente el estado


#  Planificación del Sprint

Utilice Trello para organizar el trabajo con las siguientes columnas:

 Backlog,To Do ,En progreso,Testing,Done

##  Tickets del Sprint

### Crear pedido

 Ingresar nombre del cliente,agregar productos,calcular total
 Validar pedido

**Estimación:** 3 Story Points

### Ver pedidos

 Mostrar lista de pedidos,mostrar cliente, productos, estado y total

**Estimación:** 2 Story Points

### Cambiar estado del pedido
Cambiar entre estados disponibles
Guardar cambios

**Estimación:** 1 Story Point

### Backend:

Flask (Python)
API REST con endpoints:

  POST /pedidos
  GET /pedidos
  PUT /pedidos/{id}/estado

# Testing

Se realizaron pruebas manuales:

Creación de pedidos
Visualización de pedidos
Cambio de estado

Se verificó el correcto funcionamiento de cada funcionalidad.

#  Implementación 

UtiliCE Git con el siguiente flujo:

Ramas feature para cada funcionalidad
Rama develop para integración
Rama release/1.0.0 para versión final

### Acciones realizadas:

Merge de features
Creación de release
Integración en rama principal (master)

#  Demo

Durante la demostración se presentó:

Creación de pedidos
Visualización de datos
Cambio de estado

El sistema respondió correctamente a las funcionalidades.

#  Feedback del Cliente

El cliente indicó:

El sistema cumple con los requisitos
Se solicita mejorar la visualización de los pedidos
Se recomienda una interfaz más amigable

# Nuevo Sprint

A partir del feedback se definió:

### Nuevo requerimiento:
Mostrar pedidos en formato visual (no JSON)

### Nuevo caso de uso:

Visualizar pedidos en interfaz gráfica

### Nuevo ticket:

 Mostrar pedidos en HTML con mejor presentación

**Estimación:** 3 Story Points