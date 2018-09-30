Git Graph Sequence

### Versiones usadas:
- Python 3.7.0
- Selenium 3.14.1
- geckodriver 0.22.0
- Firefox 61
- GitGraph 1.13.0

### Instrucciones
- Abrir directamente `index.html` en el navegador para ver el resultado final.
- Modificar el fichero init.js para configurar GitGraph.
- Modificar el fichero sentences.js para generar el grafo que se desee.
- (Si no se ha hecho todavía) Ejecutar `source venv/bin/activate` para activar el entorno virtual de Python.
- Ejecutar `python generate.py` para crear las imágenes.

### Instalación
```
python -m venv venv
cp /path/to/geckodriver venv/bin
source venv/bin/activate
pip install -r requirements.txt
```

### Variable window
Selenium no puede ejecutar `var foo = 42` y después ejecutar `foo`, no crea variables. Hay que hacer uso de `window` para crear las variables.


### TODO
- [ ] Quitar variable window
- [ ] Quitar duplicidad index.html/selenium.html
- [ ] Quitar la limitación de usar el sentences.js
- [ ] No exportar imágenes en los pasos que no generan cambios, p.e. creación de ramas
- [ ] Inglés
- [ ] Añadir licencia y comprobar las de las dependencias
