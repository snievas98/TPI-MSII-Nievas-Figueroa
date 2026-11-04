from collections import Counter

from version_refactorizada.application.dto import NuevaSolicitudData
from version_refactorizada.domain.enums import EstadoSolicitud
from version_refactorizada.domain.exceptions import SolicitudNoEncontradaError
from version_refactorizada.domain.models import Estudiante, Responsable, Solicitud
from version_refactorizada.infrastructure.repositories import SolicitudReader, SolicitudRepository


class SolicitudService:
    def __init__(self, repository: SolicitudRepository):
        self.repository = repository

    def registrar(self, data: NuevaSolicitudData) -> Solicitud:
        solicitudes = self.repository.list_all()
        solicitud_id = self._siguiente_id(solicitudes)
        solicitud = self._crear_solicitud(solicitud_id, data)
        solicitudes.append(solicitud)
        self.repository.save_all(solicitudes)
        return solicitud

    def asignar(self, solicitud_id: int, responsable: Responsable) -> Solicitud:
        solicitudes, solicitud = self._obtener_para_actualizar(solicitud_id)
        solicitud.asignar_responsable(responsable)
        self.repository.save_all(solicitudes)
        return solicitud

    def cambiar_estado(self, solicitud_id: int, nuevo_estado: EstadoSolicitud) -> Solicitud:
        solicitudes, solicitud = self._obtener_para_actualizar(solicitud_id)
        solicitud.cambiar_estado(nuevo_estado)
        self.repository.save_all(solicitudes)
        return solicitud

    def buscar(self, campo: str, valor: str) -> list[Solicitud]:
        campos_permitidos = {"estado", "tipo", "prioridad", "area", "responsable"}
        if campo not in campos_permitidos:
            return []
        resultado = []
        for solicitud in self.repository.list_all():
            dato = self._valor_de_campo(solicitud, campo)
            if dato == valor:
                resultado.append(solicitud)
        return resultado

    @staticmethod
    def _siguiente_id(solicitudes: list[Solicitud]) -> int:
        return max((s.id for s in solicitudes), default=0) + 1

    @staticmethod
    def _crear_solicitud(solicitud_id: int, data: NuevaSolicitudData) -> Solicitud:
        estudiante = Estudiante(data.legajo.strip(), data.nombre.strip(), data.email.strip().lower())
        codigo = f"{data.tipo.prefijo}-{solicitud_id:04d}"
        return Solicitud(
            id=solicitud_id,
            codigo=codigo,
            estudiante=estudiante,
            tipo=data.tipo,
            prioridad=data.prioridad,
            descripcion=data.descripcion.strip(),
            area=data.area or "SECRETARIA_ACADEMICA",
        )

    def _obtener_para_actualizar(self, solicitud_id: int) -> tuple[list[Solicitud], Solicitud]:
        solicitudes = self.repository.list_all()
        solicitud = next((s for s in solicitudes if s.id == solicitud_id), None)
        if solicitud is None:
            raise SolicitudNoEncontradaError(f"No existe la solicitud {solicitud_id}")
        return solicitudes, solicitud

    @staticmethod
    def _valor_de_campo(solicitud: Solicitud, campo: str) -> str:
        if campo == "responsable":
            return solicitud.responsable.nombre if solicitud.responsable else ""
        if campo == "prioridad":
            return solicitud.prioridad.name
        valor = getattr(solicitud, campo)
        return valor.value if hasattr(valor, "value") else str(valor)


class ReporteService:
    """Responsabilidad movida fuera de SistemaSolicitudes para aumentar cohesión."""

    def __init__(self, reader: SolicitudReader):
        self.reader = reader

    def generar(self) -> dict:
        solicitudes = self.reader.list_all()
        estados = Counter(s.estado.value for s in solicitudes)
        prioridades = Counter(s.prioridad.name for s in solicitudes)
        return {
            "total": len(solicitudes),
            "por_estado": {
                "PENDIENTE": estados["PENDIENTE"],
                "EN_PROCESO": estados["EN_PROCESO"],
                "RESUELTA": estados["RESUELTA"],
                "RECHAZADA": estados["RECHAZADA"],
            },
            "por_prioridad": {
                "ALTA": prioridades["ALTA"],
                "MEDIA": prioridades["MEDIA"],
                "BAJA": prioridades["BAJA"],
            },
        }
