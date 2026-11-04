from dataclasses import dataclass
from version_refactorizada.domain.enums import Prioridad, TipoSolicitud


@dataclass(frozen=True)
class NuevaSolicitudData:
    """Parameter Object: agrupa los datos que antes viajaban como 8 parámetros."""

    legajo: str
    nombre: str
    email: str
    tipo: TipoSolicitud
    prioridad: Prioridad
    descripcion: str
    area: str = "SECRETARIA_ACADEMICA"
