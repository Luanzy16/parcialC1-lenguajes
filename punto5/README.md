Ejecuta el siguiente comando para instalar ANTLR y sus dependencias en Python:

```sh
pip install antlr4-python3-runtime
```


```sh
python3 -m venv mi_entorno
source mi_entorno/bin/activate
```

```sh
pip install antlr4-python3-runtime
```


Antes de ejecutar el programa, debes generar los archivos de ANTLR:

```sh
antlr4 -visitor -Dlanguage=Python3 calculadora.g4
```



## ▶️ Ejecutar la Calculadora

Para iniciar la calculadora, usa el siguiente comando:

```sh
python main.py
```