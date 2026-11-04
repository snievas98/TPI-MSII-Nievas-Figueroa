import tempfile
import unittest
from pathlib import Path

from version_inicial.sistema import SistemaSolicitudes


class TestVersionInicial(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.sistema = SistemaSolicitudes(Path(self.tmp.name) / "solicitudes.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_flujo_principal(self):
        solicitud = self.sistema.registrar(
            "A-100", "Ana Pérez", "ANA@EXAMPLE.EDU", "CERTIFICADO", "ALTA",
            "Certificado de alumno regular", "ALUMNOS"
        )
        self.assertEqual("CER-0001", solicitud["codigo"])
        self.assertEqual("ana@example.edu", solicitud["email"])
        self.assertTrue(self.sistema.asignar(1, "Laura Gómez", "ALUMNOS"))
        self.assertTrue(self.sistema.cambiar_estado(1, "EN_PROCESO"))
        self.assertEqual(1, len(self.sistema.buscar("estado", "EN_PROCESO")))
        self.assertEqual(1, self.sistema.reporte()["total"])

    def test_persistencia(self):
        self.sistema.registrar(
            "A-101", "Bruno Díaz", "bruno@example.edu", "BECA", "MEDIA",
            "Consulta por beca", "BIENESTAR"
        )
        recargado = SistemaSolicitudes(Path(self.tmp.name) / "solicitudes.json")
        self.assertEqual(1, len(recargado.s))
        self.assertEqual("BEC-0001", recargado.s[0]["codigo"])


if __name__ == "__main__":
    unittest.main()
