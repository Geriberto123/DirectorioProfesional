
import os
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': os.environ.get('FIREBASE_PROJECT_ID'),
})

db = firestore.client()

app = Flask(__name__, template_folder='src')

@app.route('/')
def get_professionals():
    try:
        search_field = request.args.get('search_field', 'all')
        search_term = request.args.get('search_term', '').strip().split('?')[0]

        professionals_ref = db.collection(u'profesionales')
        docs = professionals_ref.stream()
        all_professionals = [doc.to_dict() for doc in docs]

        filtered_professionals = all_professionals

        if search_term:
            search_lower = search_term.lower()
            results = []

            for prof in all_professionals:
                if search_field == 'all':
                    if (search_lower in prof.get('nombre', '').lower() or
                        search_lower in prof.get('compania', '').lower() or
                        search_lower in prof.get('cargo', '').lower() or
                        search_lower in str(prof.get('ingreso_anual', '')) or
                        search_lower in str(prof.get('experiencia_anios', ''))):
                        results.append(prof)
                else:
                    field_value = prof.get(search_field, '')
                    if search_lower in str(field_value).lower():
                        results.append(prof)
            
            filtered_professionals = results

        return render_template(
            'index.html',
            professionals=filtered_professionals,
            search_term=search_term,
            search_field=search_field 
        )

    except Exception as e:
        print(f"Error: {e}")
        return "Ocurrió un error al obtener los datos.", 500

if __name__ == '__main__':
    app.run(debug=True)
