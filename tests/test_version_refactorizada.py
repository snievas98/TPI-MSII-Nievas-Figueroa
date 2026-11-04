import unittest

from version_refactorizada.application.dto import NuevaSolicitudData
from version_refactorizada.application.services import ReporteService, SolicitudService
from version_refactorizada.domain.enums import EstadoSolicitud, Prioridad, TipoSolicitud
from version_refactorizada.domain.exceptions import DatosInvalidosError, SolicitudNoEncontradaError
from version_refactorizada.domain.models import Responsable
from version_refactorizada.infrastructure.repositories import InMemorySolicitudRepository


class TestVersionRefactorizada(unittest.TestCase):
    def setUp(self):
        self.repo = InMemorySolicitudRepository()
        self.service = SolicitudService(self.repo)
        self.reporte = ReporteService(self.repo)

    def _data(self):
        return NuevaSolicitudData(
            legajo="A-100",
            nombre="Ana Pérez",
            email="ANA@EXAMPLE.EDU",
            tipo=TipoSolicitud.CERTIFICADO,
            prioridad=Prioridad.ALTA,
            descripcion="Certificado de alumno regular",
            area="ALUMNOS",
        )

    def test_flujo_principal(self):
        solicitud = self.service.registrar(self._data())
        self.assertEqual("CER-0001", solicitud.codigo)
        self.assertEqual("ana@example.edu", solicitud.estudiante.email)
        self.service.asignar(1, Responsable("Laura Gómez", "ALUMNOS"))
        self.service.cambiar_estado(1, EstadoSolicitud.EN_PROCESO)
        self.assertEqual(1, len(self.service.buscar("estado", "EN_PROCESO")))
        self.assertEqual(1, len(self.service.buscar("tipo", "CERTIFICADO")))
        self.assertEqual(1, len(self.service.buscar("prioridad", "ALTA")))
        self.assertEqual(1, self.reporte.generar()["total"])

    def test_validacion_de_email(self):
        data = NuevaSolicitudData(
            legajo="A-102", nombre="Carla", email="correo-invalido",
            tipo=TipoSolicitud.EXAMEN, prioridad=Prioridad.MEDIA,
            descripcion="Inscripción", area="EXAMENES"
        )
        with self.assertRaises(DatosInvalidosError):
            self.service.registrar(data)

    def test_error_explicito_si_no_existe(self):
        with self.assertRaises(SolicitudNoEncontradaError):
            self.service.cambiar_estado(999, EstadoSolicitud.RESUELTA)


if __name__ == "__main__":
    unittest.main()
