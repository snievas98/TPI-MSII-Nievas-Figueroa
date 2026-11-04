import tempfile
import unittest
from pathlib import Path

from version_inicial.sistema import SistemaSolicitudes
from version_refactorizada.application.dto import NuevaSolicitudData
from version_refactorizada.application.services import ReporteService, SolicitudService
from version_refactorizada.domain.enums import EstadoSolicitud, Prioridad, TipoSolicitud
from version_refactorizada.domain.models import Responsable
from version_refactorizada.infrastructure.repositories import InMemorySolicitudRepository


class TestEquivalenciaAntesDespues(unittest.TestCase):
    def test_mismo_resultado_externo_en_flujo_nominal(self):
        with tempfile.TemporaryDirectory() as tmp:
            inicial = SistemaSolicitudes(Path(tmp) / "base.json")
            s0 = inicial.registrar(
                "A-200", "Diego Ramos", "diego@example.edu", "EQUIVALENCIA", "MEDIA",
                "Solicitud de equivalencia", "SECRETARIA_ACADEMICA"
            )
            inicial.asignar(s0["id"], "María López", "EQUIVALENCIAS")
            inicial.cambiar_estado(s0["id"], "RESUELTA")

            repo = InMemorySolicitudRepository()
            final = SolicitudService(repo)
            s1 = final.registrar(NuevaSolicitudData(
                legajo="A-200", nombre="Diego Ramos", email="diego@example.edu",
                tipo=TipoSolicitud.EQUIVALENCIA, prioridad=Prioridad.MEDIA,
                descripcion="Solicitud de equivalencia", area="SECRETARIA_ACADEMICA"
            ))
            final.asignar(s1.id, Responsable("María López", "EQUIVALENCIAS"))
            final.cambiar_estado(s1.id, EstadoSolicitud.RESUELTA)

            base_result = inicial.s[0]
            final_result = repo.list_all()[0].to_dict()
            claves = ["codigo", "legajo", "nombre", "email", "tipo", "prioridad", "puntaje",
                      "descripcion", "area", "responsable", "estado"]
            self.assertEqual({k: base_result[k] for k in claves}, {k: final_result[k] for k in claves})
            self.assertEqual(inicial.reporte(), ReporteService(repo).generar())


if __name__ == "__main__":
    unittest.main()
