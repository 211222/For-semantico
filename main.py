import re
import tkinter as tk
from tkinter import messagebox, filedialog
from ply import lex, yacc



tokens = (
    'FOR',
    'INT',
    'SYSTEM',
    'OUT',
    'PRINTLN',
    'ID',
    'NUM',
    'STRING',
    'PLUS',
    'LESS',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'DOT',
    'EQUALS',
    'LEQ',
    'MENORQ',
    'MAYORQ'  
)

t_PLUS = r'\+'
t_LESS = r'\-'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_DOT = r'\.'
t_EQUALS = r'='
t_LEQ = r'<=' 
t_MENORQ = r'<' 
t_MAYORQ = r'>'

def load_file():
    archivo = filedialog.askopenfilename(filetypes=[('Archivo de texto', '*.txt')])
    if archivo:
        with open(archivo, 'r') as f:
            contenido = f.read()
            print(contenido)
            code_text.delete("1.0", tk.END)
            code_text.insert(tk.END, contenido)
            result_text.delete("1.0", tk.END)
            
def clean_process():
    code_text.delete("1.0", tk.END)
    result_sintactico.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1] 
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value == 'for':
        t.type = 'FOR'
    elif t.value == 'int':
        t.type = 'INT'
    elif t.value == 'system':
        t.type = 'SYSTEM'
    elif t.value == 'out':
        t.type = 'OUT'
    elif t.value == 'println':
        t.type = 'PRINTLN'
    return t


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    error_message(f"Token desconocido '{t.value[0]}'", t.lineno)
    t.lexer.skip(1)

lexer = lex.lex()


def p_for_loop(p):
    '''for_loop : FOR LPAREN INT ID EQUALS NUM SEMICOLON ID LEQ NUM SEMICOLON ID PLUS PLUS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[4] != p[8] or p[4] != p[12]:
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta")

def p_for_loop_m(p):
    '''for_loop : INT ID SEMICOLON FOR LPAREN ID EQUALS NUM SEMICOLON ID LEQ NUM SEMICOLON ID PLUS PLUS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[2] != p[6] or p[2] != p[10] or p[2] != p[14]:
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta")

def p_for_loop_m1(p):
    '''for_loop : INT ID EQUALS NUM SEMICOLON FOR LPAREN ID SEMICOLON ID LEQ NUM SEMICOLON ID PLUS PLUS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[2] != p[8] or p[2] != p[10] or p[2] != p[14]:
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta")

def p_for_loop_m2(p):
    '''for_loop : INT ID SEMICOLON INT ID SEMICOLON FOR LPAREN ID EQUALS NUM SEMICOLON ID LEQ NUM SEMICOLON ID PLUS PLUS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[2] != p[9] or p[2] != p[13] or p[2] != p[17]:
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta") 

def p_for_loop_m2(p):
    '''for_loop : INT ID SEMICOLON FOR LPAREN INT ID EQUALS NUM SEMICOLON ID LEQ NUM SEMICOLON ID PLUS PLUS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[7] != p[11] or p[7] != p[15]:
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta") 

def p_for_loop_m3(p):
    '''for_loop : INT ID SEMICOLON INT ID SEMICOLON FOR LPAREN INT ID EQUALS NUM SEMICOLON ID LEQ NUM SEMICOLON ID PLUS PLUS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[10] != p[14] or p[10] != p[18] :
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta") 

def p_for_loopt(p):
    '''for_loop : FOR LPAREN INT ID EQUALS NUM SEMICOLON ID LEQ NUM SEMICOLON ID LESS LESS RPAREN LBRACE SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUM RPAREN SEMICOLON RBRACE'''
    if p[4] != p[8] or p[4] != p[12]:
        error_message("Todos los IDENTIFICADORES deben ser iguales en la sentencia FOR", p.lineno(2))
    else:
        result_sintactico.insert("1.0", "Estructura FOR correcta")




def p_error(p):
    if p:
        error_message(f"Error de sintaxis en '{p.value}'", p.lineno)
    else:
        error_message("Error de sintaxis: final inesperado del código", len(code_text.get("1.0", "end-1c").split('\n')))

parser = yacc.yacc()

def lex_analyzer(code):
    lexer.input(code)
    tokens = []
    global flag
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append((token.lineno, token.type, token.value))
    return tokens

def parse_code(code):
    parser.parse(code, lexer=lexer)

def error_message(message, line_number):
    messagebox.showerror("Error de sintaxis", f"{message}\nEn la línea {line_number}")
    result_sintactico.insert("end", "Error de sintaxis de la Estructura FOR")

def process_code():
    result_text.delete("1.0", "end")
    result_sintactico.delete("1.0", "end")
    code = code_text.get("1.0", "end-1c")
    tokens = lex_analyzer(code)
    result_text.delete("1.0", "end")
    for token in tokens:
        line_number, token_type, token_value = token
        result_text.insert("end", f"Línea ->: {token_type} -> {token_value}\n")
    parse_code(code)
    

window = tk.Tk()
window.title("Analizador Léxico y Semantico")
window.geometry("790x440")
window.configure(bg="#5F9EA0")

code_label = tk.Label(window, text="Texto", bg="#5F9EA0", font=('Helveica',13,'bold'), foreground='white')
code_label.place(x=10, y=0)

code_text = tk.Text(window, height=10, width=95)
code_text.place(x=10, y=22)

process_button = tk.Button(window, text="Analizar",bg="#3498DB",foreground='white', font=('Helveica',9,'bold'), command=process_code)
process_button.place(x=300, y=395)

clean_button = tk.Button(window, text="Limpiar",bg="#3498DB",foreground='white',  font=('Helveica',9,'bold'), command=clean_process)
clean_button.place(x=450, y=395)

boton_cargar = tk.Button(window, text="Cargar archivo", bg="#3498DB", foreground='white', font=('Helveica',9,'bold'), command=load_file)
boton_cargar.place(x=125, y=395)

result_label = tk.Label(window, text="Análisis Léxico",bg="#5F9EA0", font=('Helveica',13,'bold'), foreground='white')
result_label.place(x=10, y=190)

result_text = tk.Text(window, height=10, width=45)
result_text.place(x=10, y=220)

result_label = tk.Label(window, text="Análisis Semantico", bg="#5F9EA0", font=('Helveica',13,'bold'), foreground='white')
result_label.place(x=410, y=190)

result_sintactico = tk.Text(window, height=10, width=45)
result_sintactico.place(x=410, y=220)

window.mainloop()


