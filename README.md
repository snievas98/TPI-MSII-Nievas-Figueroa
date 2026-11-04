# TPI - Metodología de Sistemas II
## Sistema de Gestión de Solicitudes Académicas

**Integrantes:** Santiago Nievas e Ignacio Figueroa  
**Carrera:** Tecnicatura Universitaria en Programación a Distancia - UTN  
**Año:** 2026

Este repositorio contiene un caso acotado diseñado para demostrar diagnóstico de calidad, deuda técnica, code smells, aplicación de SOLID/Clean Code, refactoring seguro, pruebas y code review profesional.

## Estructura

- `version_inicial/`: implementación funcional con problemas de diseño intencionalmente conservados para el diagnóstico.
- `version_refactorizada/`: versión mejorada con dominio, servicios y persistencia separados.
- `tests/`: pruebas de la versión inicial, de la versión final y de equivalencia antes/después.
- `docs/`: diagnóstico, checklist, decisiones técnicas, evidencias y guía de defensa.

## Funcionalidades verificables

1. Registrar una solicitud académica.
2. Asignar responsable y área.
3. Cambiar el estado de una solicitud.
4. Buscar/filtrar solicitudes.
5. Generar un reporte resumido.
6. Persistir datos en JSON en la implementación de infraestructura final.

## Requisitos

- Python 3.11 o superior.
- No requiere dependencias externas.

## Ejecución

Desde la raíz del repositorio:

```bash
python -m version_inicial.demo
python -m version_refactorizada.presentation.cli
```

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Trazabilidad Git esperada

El repositorio local entregado incluye los tags requeridos por la consigna:

- `estado-inicial`
- `etapa-diagnostico`
- `etapa-refactoring`
- `etapa-pruebas`
- `etapa-docs`
- `estadorefactorizado`

> Antes de la entrega final, el equipo debe publicar este repositorio en GitHub y reemplazar en el informe el marcador del enlace por la URL real.
