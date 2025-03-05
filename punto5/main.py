import sys
from antlr4 import *
from calLexer import calLexer
from calParser import calParser
from calvisitor import calvisitor

def parse_expression(expression):
    input_stream = InputStream(expression)
    lexer = calLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = calParser(token_stream)
    tree = parser.expr()

    visitor = calvisitor()
    return visitor.visit(tree)

def main():
    if len(sys.argv) > 1:  # Si se proporciona un archivo como argumento
        file_path = sys.argv[1]
        try:
            with open(file_path, "r") as file:
                expression = file.read().strip()
            print(f"Expresión desde archivo: {expression}")
            result = parse_expression(expression)
            print(f"Resultado: {result}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {file_path}")
    else:  # Entrada manual por teclado
        while True:
            expression = input("Ingrese una expresión matemática (o 'salir' para terminar): ").strip()
            if expression.lower() == "salir":
                break
            try:
                result = parse_expression(expression)
                print(f"Resultado: {result}")
            except Exception as e:
                print(f"Error en la expresión: {e}")

if __name__ == "__main__":
    main()