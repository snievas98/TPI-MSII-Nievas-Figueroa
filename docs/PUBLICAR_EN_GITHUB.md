# Publicación del repositorio en GitHub

El repositorio local conserva el historial completo y los tags exigidos por la consigna. El remoto `origin` ya está configurado para:

`https://github.com/snievas98/TPI-MSII-Nievas-Figueroa.git`

## Paso 1 - Crear el repositorio vacío

Desde la cuenta `snievas98`, crear en GitHub un repositorio público llamado exactamente:

`TPI-MSII-Nievas-Figueroa`

No agregar README, `.gitignore` ni licencia desde GitHub.

## Paso 2 - Publicar historial y tags

Desde la raíz de esta carpeta ejecutar:

```bash
git push -u origin main
git push origin --tags
```

## Paso 3 - Verificar

```bash
git status
git log --oneline --decorate --graph --all
git tag --list
python -m unittest discover -s tests -v
```

Deben verse los tags:

- `estado-inicial`
- `etapa-diagnostico`
- `etapa-refactoring`
- `etapa-pruebas`
- `etapa-docs`
- `estadorefactorizado`

El commit más reciente de Santiago está preparado con una identidad GitHub asociable a la cuenta `snievas98`. Ignacio debe realizar mañana su propia contribución real desde su cuenta antes de la entrega definitiva.
