from pydantic import BaseModel


class ConsultaEntrada(BaseModel):
    mensaje: str


class RespuestaSalida(BaseModel):
    categoria: str
    respuesta: str
    pasos: list[str]
    confianza: float