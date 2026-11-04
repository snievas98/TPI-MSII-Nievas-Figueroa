# Publicación del repositorio en GitHub

El repositorio local ya tiene historial y tags. Para conservarlos, no conviene subir los archivos arrastrándolos desde el navegador.

1. Crear en GitHub un repositorio vacío, por ejemplo `tpi-msii-nievas-figueroa` (sin README ni .gitignore iniciales).
2. Desde esta carpeta ejecutar:

```bash
git remote add origin <URL_REAL_DEL_REPOSITORIO>
git push -u origin main
git push origin --tags
```

3. Verificar en GitHub que se vean los commits y tags.
4. Copiar la URL real y reemplazar `[ENLACE_REPOSITORIO]` en el informe final.
5. Cuando el video esté publicado, reemplazar `[ENLACE_VIDEO]`.

## Verificación antes de entregar

```bash
git status
git log --oneline --decorate --graph --all
git tag --list
python -m unittest discover -s tests -v
```
