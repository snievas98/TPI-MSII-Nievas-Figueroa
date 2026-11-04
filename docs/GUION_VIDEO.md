# Guion para video de defensa (10-15 minutos)

## 0:00-0:40 - Presentación

**Santiago:** nombre completo, materia y objetivo del TPI.  
**Ignacio:** nombre completo y breve descripción del caso seleccionado.

## 0:40-2:00 - Sistema base

Mostrar la versión inicial ejecutándose. Explicar las operaciones: registrar, asignar, cambiar estado, buscar y reportar. Aclarar que la calidad externa es aceptable porque el usuario puede completar el flujo.

## 2:00-4:00 - Diagnóstico

Mostrar `version_inicial/sistema.py` y la tabla de `docs/DIAGNOSTICO.md`. Seleccionar 4 o 5 ejemplos visibles: clase grande, método largo, lista extensa de parámetros, strings mágicos y acoplamiento a JSON. Explicar que los smells no son necesariamente bugs, pero aumentan el costo del cambio.

## 4:00-7:30 - SOLID, Clean Code y refactoring

Mostrar la estructura `version_refactorizada/`. Explicar:

- `NuevaSolicitudData`: Introduce Parameter Object.
- Métodos privados en `SolicitudService`: Extract Method.
- `ReporteService`: Move Method/reubicación de responsabilidad.
- `SolicitudRepository` + `JsonSolicitudRepository`: DIP y separación de infraestructura.
- Enums y dataclasses: eliminación de primitive obsession/magic strings.

## 7:30-9:30 - Pruebas y no regresión

Ejecutar:

```bash
python -m unittest discover -s tests -v
```

Mostrar que pasan los tests de la versión inicial, final y equivalencia. Explicar que el refactoring cambia estructura interna, pero conserva el comportamiento externo esperado.

## 9:30-11:00 - Code review

Abrir `docs/CODE_REVIEW_CHECKLIST.md`. Mostrar criterios de lógica, legibilidad, diseño, seguridad, tests y aceptación técnica. Indicar qué observaciones fueron corregidas.

## 11:00-12:30 - Git y trazabilidad

Mostrar `git log --oneline --decorate --graph` y `git tag`. Explicar `estado-inicial`, hitos por etapa y `estadorefactorizado`.

## 12:30-14:00 - Conclusiones

**Santiago:** la principal mejora fue reducir el costo de cambio separando responsabilidades.  
**Ignacio:** las pruebas permitieron refactorizar con mayor seguridad y el code review convirtió observaciones en criterios verificables.  
**Ambos:** mencionar como mejora futura una interfaz web/API y persistencia en base de datos sin cambiar la lógica central.
