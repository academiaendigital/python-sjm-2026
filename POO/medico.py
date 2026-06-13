from flask import Flask, render_template

app = Flask(__name__)

# Esta es la ruta que el usuario visitará (ej. http://127.0.0.1:5000/)
@app.route('/')
def index():
    # 1. Datos dinámicos: Variables que quieres enviar a la plantilla
    nombre_usuario = "Alex"
    lista_productos = ["Laptop", "Monitor", "Teclado", "Ratón"]
    
    # 2. Renderizar: 
    #    - Llama a la plantilla 'index.html'
    #    - Pasa las variables como argumentos clave-valor
    return render_template(
        'index.html', 
        usuario=nombre_usuario, 
        productos=lista_productos,
        titulo="Mi Tienda Flask"
    )

if __name__ == '__main__':
    app.run(debug=True)