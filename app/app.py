from flask import Flask, render_template
from urllib.request import urlopen

app = Flask(__name__)

@app.route("/")
def index():
    cursos = ['PHP', 'HTML', 'PYTHON']
    data = {
        "titulo": "index",
        "bienvenida": "¡Saludos!",
        "cursos": cursos, 
        "numero_cursos": len(cursos)
    }
    return render_template("index.html", data=data)


def get_data():
    url = 'https://datos.monterrey.gob.mx/api/3/action/datastore_search?resource_id=826aa323-0d03-4839-9b9f-ab262680087c&limit=5'
    with urlopen(url) as fileobj:
        content = fileobj.read()
        return content

if __name__ == "__main__":
    app.run(debug=True)
    get_data()
    