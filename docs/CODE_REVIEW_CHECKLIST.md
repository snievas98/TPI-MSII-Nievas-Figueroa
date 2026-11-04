# Checklist de Code Review Profesional

| Criterio | Resultado | Evidencia / observación |
|---|---|---|
| Lógica: operaciones requeridas funcionan | Cumple | Pruebas de alta, asignación, estado, búsqueda y reporte |
| Casos de borde y errores | Cumple | Email inválido y solicitud inexistente generan excepciones explícitas |
| Nombres descriptivos y del dominio | Cumple | `SolicitudService`, `NuevaSolicitudData`, `EstadoSolicitud` |
| Funciones pequeñas y una responsabilidad | Cumple | Flujo dividido en métodos privados y servicios específicos |
| SRP | Cumple | Dominio, aplicación, persistencia y presentación separados |
| OCP | Cumple parcialmente | Prefijos encapsulados por tipo; nuevas persistencias no requieren tocar el servicio |
| LSP | Cumple | Repositorio JSON e InMemory respetan el mismo contrato |
| ISP | Cumple | Contratos separados de lectura y escritura (`SolicitudReader`/`SolicitudWriter`) |
| DIP | Cumple | Servicios dependen de Protocols, no de JSON concreto |
| DRY | Cumple | Se elimina lógica repetida de conteos y decisiones dispersas |
| Manejo de errores | Cumple | Excepciones de dominio; no hay `except` vacío/general en la versión final |
| Datos sensibles | Cumple | Se usan datos sintéticos `example.edu`; no hay credenciales |
| Persistencia intercambiable | Cumple | Adaptador JSON + implementación InMemory |
| Tests automatizados | Cumple | Suite `unittest` completa |
| No regresión funcional | Cumple | `test_equivalencia.py` compara antes/después |

## Feedback profesional aplicado

1. Reducir el tamaño y las responsabilidades de la clase inicial -> resuelto mediante separación en dominio, servicios y repositorios.
2. Evitar strings libres para estados/prioridades -> resuelto con enums.
3. Evitar la firma extensa de registro -> resuelto con `NuevaSolicitudData`.
4. Mejorar la testabilidad -> resuelto con repositorio en memoria y dependencia por contrato.
5. No silenciar errores -> resuelto con excepciones de dominio explícitas.

## Criterios de aceptación técnica

- La suite completa debe finalizar sin fallos.
- El comportamiento nominal de la versión final debe coincidir con la inicial.
- No debe haber datos personales reales, credenciales ni secretos.
- Los componentes deben mantener responsabilidades claras y dependencias controladas.
- Los tags de trazabilidad exigidos deben existir antes de publicar el repositorio.
