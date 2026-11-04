# Diagnóstico de calidad interna y deuda técnica

La versión inicial mantiene una calidad externa aceptable: permite registrar, asignar, cambiar estado, buscar, reportar y persistir solicitudes. El problema se encuentra en la calidad interna. La clase `SistemaSolicitudes` concentra responsabilidades, usa strings y diccionarios para conceptos de dominio, mezcla persistencia con reglas y repite decisiones.

## Code smells y debilidades

| # | Problema | Evidencia | Impacto | Riesgo | Prioridad |
|---|---|---|---|---|---|
| 1 | Large Class | `SistemaSolicitudes` concentra carga, guardado, negocio, búsqueda y reporte | Baja cohesión | Cambios con efecto dominó | Alta |
| 2 | Long Method | `registrar()` valida, normaliza, genera ID/código, calcula prioridad, crea y persiste | Lectura y prueba difíciles | Regresiones al modificar reglas | Alta |
| 3 | Long Parameter List | `registrar()` recibe 8 parámetros | Firma frágil | Orden incorrecto y difícil evolución | Alta |
| 4 | Primitive Obsession | tipo, prioridad, estado, estudiante y responsable se modelan con strings/dict | Reglas dispersas | Valores inválidos | Alta |
| 5 | Duplicated Code | `guardar()` se invoca desde varias operaciones de modificación con lógica repetitiva de búsqueda | Mantenimiento repetitivo | Inconsistencias | Media |
| 6 | Magic Strings | `PENDIENTE`, `ALTA`, `CERTIFICADO`, áreas, etc. | Errores tipográficos | Bugs silenciosos | Alta |
| 7 | Conditional Complexity | cadenas `if/elif` para prefijos y filtros | Extensión costosa | Cada tipo nuevo obliga a modificar código existente | Media |
| 8 | Broad Exception / Error Silencing | `except Exception: self.s = []` | Oculta errores de archivo/JSON | Pérdida de diagnóstico | Alta |
| 9 | Tight Coupling | la clase conoce directamente JSON y `Path` | Dificulta tests y cambio de persistencia | Evolución costosa | Alta |
| 10 | Feature Envy / responsabilidad mal ubicada | reporte y cálculo agregado viven en la clase operativa | Baja cohesión | Crecimiento de clase | Media |

## Relación con deuda técnica

La versión inicial funciona, pero cada regla nueva obliga a modificar una clase central. Esa velocidad inicial se paga luego como tiempo adicional de lectura, prueba y corrección. La deuda se hace visible cuando una nueva prioridad, un nuevo medio de persistencia o un nuevo reporte requiere tocar lógica no relacionada.
