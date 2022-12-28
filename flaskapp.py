from flask import Flask, render_template, request

app = Flask(__name__)

lista = ["Menaje", "Textil 11", "Textil 12", "Orden", "Baños", "Iluminacion", "Deco", "Niños", "Actividades"]
listaauto = ["pares", "impares", "fondopar", "fondoimpar", "pax", "2426", "1a3", "zona1", "zona2", "zona3", "zona4"]


@app.route("/")
def archivos():
    return render_template("upload_files.html")


@app.route('/main', methods=['POST'])
def main():
    # Obtener los campos de archivo del formulario
    archivo1 = request.files['file1']
    archivo2 = request.files['file2']
    archivo3 = request.files['file3']

    # Verificar si los archivos han sido enviados
    if archivo1 and archivo2:
        upload_dir = './static/archivos/'
        archivo1.save(upload_dir + "PROPUESTA_FINAL")
        archivo2.save(upload_dir + "PLAN")
        archivo3.save(upload_dir + "SG010")
        import datos

        repo = datos.check_datos()
        tied = datos.check_tie_dormunt()
        aires = datos.aire_total()

        return render_template("datos.html", repo=repo, tied=tied, aire=aires)
    else:
        return 'Debe seleccionar al menos dos archivos para continuar.'

@app.route("/MV0")
def metodoventa0():
    import check_market
    camion = check_market.check_market_repo()
    return render_template("MV0.html", camion=camion, lista=lista)

@app.route("/MV1")
def metodoventa1():
    import repeticiones
    import datos_sgf
    import check_auto
    repo_sfg = datos_sgf.check_repoaire()
    repo_auto = check_auto.repo_auto()
    camion = check_auto.camiones_auto()
    reps = repeticiones.repeticiones_html
    return render_template("MV1.html", repo=repo_auto, lista=listaauto, camion=camion, reposgf=repo_sfg, reps=reps)


if __name__ == '__main__':
    app.run(debug=True)
