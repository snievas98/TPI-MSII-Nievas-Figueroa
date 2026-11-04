from pathlib import Path
from tempfile import TemporaryDirectory

from version_refactorizada.application.dto import NuevaSolicitudData
from version_refactorizada.application.services import ReporteService, SolicitudService
from version_refactorizada.domain.enums import EstadoSolicitud, Prioridad, TipoSolicitud
from version_refactorizada.domain.models import Responsable
from version_refactorizada.infrastructure.repositories import JsonSolicitudRepository


def main():
    with TemporaryDirectory() as tmp:
        repo = JsonSolicitudRepository(Path(tmp) / "solicitudes.json")
        service = SolicitudService(repo)
        reporte = ReporteService(repo)

        solicitud = service.registrar(NuevaSolicitudData(
            legajo="A-1024",
            nombre="Ana Pérez",
            email="ana@example.edu",
            tipo=TipoSolicitud.CERTIFICADO,
            prioridad=Prioridad.ALTA,
            descripcion="Solicita certificado de alumno regular",
            area="ALUMNOS",
        ))
        service.asignar(solicitud.id, Responsable("Laura Gómez", "ALUMNOS"))
        service.cambiar_estado(solicitud.id, EstadoSolicitud.EN_PROCESO)
        print("Solicitud registrada:", solicitud.codigo)
        print("Reporte:", reporte.generar())


if __name__ == "__main__":
    main()
