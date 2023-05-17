from flask import Flask, jsonify

app = Flask(__name__)
def calcular_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def calcular_super_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        super_fatorial = 1
        for i in range(1, numero + 1):
            super_fatorial *= calcular_fatorial(i)
        return super_fatorial

@app.route('/super_fatorial/<int:numero>', methods=['GET'])
def obter_super_fatorial(numero):
    resultado = calcular_super_fatorial(numero)
    return jsonify({'numero': numero, 'super_fatorial': resultado})

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/fatorial/<int:numero>', methods=['GET'])

def obter_fatorial(numero):
    resultado = calcular_fatorial(numero)
    return jsonify({'numero': numero, 'fatorial': resultado})

if __name__ == '__main__':
    app.run(debug=True)
