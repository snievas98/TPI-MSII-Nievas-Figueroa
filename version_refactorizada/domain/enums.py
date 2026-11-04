from enum import Enum, IntEnum


class TipoSolicitud(str, Enum):
    CERTIFICADO = "CERTIFICADO"
    EQUIVALENCIA = "EQUIVALENCIA"
    EXAMEN = "EXAMEN"
    BECA = "BECA"

    @property
    def prefijo(self) -> str:
        return {
            TipoSolicitud.CERTIFICADO: "CER",
            TipoSolicitud.EQUIVALENCIA: "EQU",
            TipoSolicitud.EXAMEN: "EXA",
            TipoSolicitud.BECA: "BEC",
        }[self]


class Prioridad(IntEnum):
    BAJA = 1
    MEDIA = 2
    ALTA = 3


class EstadoSolicitud(str, Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROCESO = "EN_PROCESO"
    RESUELTA = "RESUELTA"
    RECHAZADA = "RECHAZADA"
