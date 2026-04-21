from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.model import ClasificadorSoporte
from app.schemas import ConsultaEntrada, RespuestaSalida

app = FastAPI(
    title="Asistente Virtual de Soporte Técnico",
    description="API para clasificar incidencias técnicas y ofrecer recomendaciones.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

modelo = ClasificadorSoporte()
modelo.entrenar()


@app.get("/")
def inicio():
    return {"mensaje": "La API del asistente funciona correctamente."}


@app.get("/chat", response_class=HTMLResponse)
def mostrar_chat(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={}
    )


@app.post("/diagnosticar", response_model=RespuestaSalida)
def diagnosticar(consulta: ConsultaEntrada):
    mensaje = consulta.mensaje.strip()

    if not mensaje:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")

    resultado = modelo.predecir(mensaje)
    return resultado