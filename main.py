from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        precio_total_sin_descuento = precio_tarro * tarros

        porcentaje_descuento = 0
        if 18 <= edad <= 30:
            porcentaje_descuento = 15
        elif edad > 30:
            porcentaje_descuento = 25
        elif edad < 18:
            porcentaje_descuento = 0

        descuento = porcentaje_descuento / 100 * precio_total_sin_descuento

        precio_total_con_descuento = precio_total_sin_descuento - descuento

        mensaje1 = f'Nombre del cliente: {nombre}'
        mensaje2 = f'Total sin descuento: ${precio_total_sin_descuento}'
        mensaje3 = f'El descuento es: ${descuento}'
        mensaje4 = f'El total a pagar es: ${precio_total_con_descuento}'

        return render_template(
            'ejercicio1.html',
            nombre=nombre,
            edad=edad,
            tarros=tarros,
            mensaje1=mensaje1,
            mensaje2=mensaje2,
            mensaje3=mensaje3,
            mensaje4=mensaje4
        )
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run()
