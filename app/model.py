from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from app.data import consultas_entrenamiento, etiquetas_entrenamiento, respuestas_soporte


class ClasificadorSoporte:
    def __init__(self):
        self.pipeline = Pipeline([
            ("vectorizer", TfidfVectorizer(ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=1000))
        ])
        self.entrenado = False

    def entrenar(self):
        self.pipeline.fit(consultas_entrenamiento, etiquetas_entrenamiento)
        self.entrenado = True

    def predecir(self, consulta):
        if not self.entrenado:
            raise ValueError("El modelo no ha sido entrenado.")

        etiqueta = self.pipeline.predict([consulta])[0]
        probabilidades = self.pipeline.predict_proba([consulta])[0]
        confianza = float(max(probabilidades))

        info = respuestas_soporte.get(etiqueta, {
            "respuesta": "No he podido clasificar la consulta.",
            "pasos": ["Derivar la incidencia a soporte humano."]
        })

        if confianza < 0.45:
            return {
                "categoria": "desconocida",
                "respuesta": "No tengo suficiente seguridad para clasificar esta consulta.",
                "pasos": [
                    "Reformula el problema con más detalle.",
                    "Si continúa, deriva la incidencia a un técnico."
                ],
                "confianza": round(confianza, 3)
            }

        return {
            "categoria": etiqueta,
            "respuesta": info["respuesta"],
            "pasos": info["pasos"],
            "confianza": round(confianza, 3)
        }