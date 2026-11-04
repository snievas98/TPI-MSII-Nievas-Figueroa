# Refactorings aplicados

## 1. Extract Method

El método `registrar()` de la versión inicial mezclaba varias tareas. En la versión final se extraen `_siguiente_id`, `_crear_solicitud` y `_obtener_para_actualizar`, dejando el flujo principal más corto y legible.

## 2. Move Method / reubicación de responsabilidad

La generación del reporte deja de pertenecer a la clase que gestiona solicitudes. Se mueve a `ReporteService`, que depende únicamente de un contrato de lectura (`SolicitudReader`).

## 3. Introduce Parameter Object

Los ocho parámetros de alta se reemplazan por `NuevaSolicitudData`, un objeto inmutable que agrupa los datos de entrada y elimina una firma extensa y propensa a errores.

## 4. Extract Class + Dependency Inversion

La persistencia JSON se extrae a `JsonSolicitudRepository`. `SolicitudService` trabaja contra el contrato `SolicitudRepository`, permitiendo usar `InMemorySolicitudRepository` en pruebas sin modificar la lógica de aplicación.

## 5. Replace Magic Strings with Enums / Value-oriented domain model

`TipoSolicitud`, `Prioridad` y `EstadoSolicitud` reemplazan strings libres. `Estudiante`, `Responsable` y `Solicitud` encapsulan datos y validaciones del dominio.

## Seguridad del refactoring

Antes y después se ejecuta el mismo flujo nominal. `test_equivalencia.py` compara los datos funcionales y el reporte de ambas versiones, verificando que el cambio estructural no altere negativamente el comportamiento externo.
