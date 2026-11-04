from pathlib import Path
from tempfile import TemporaryDirectory
from version_inicial.sistema import SistemaSolicitudes


def main():
    with TemporaryDirectory() as tmp:
        sistema = SistemaSolicitudes(Path(tmp) / "solicitudes.json")
        solicitud = sistema.registrar(
            "A-1024", "Ana Pérez", "ana@example.edu", "CERTIFICADO", "ALTA",
            "Solicita certificado de alumno regular", "ALUMNOS"
        )
        sistema.asignar(solicitud["id"], "Laura Gómez", "ALUMNOS")
        sistema.cambiar_estado(solicitud["id"], "EN_PROCESO")
        print("Solicitud registrada:", solicitud["codigo"])
        print("Reporte:", sistema.reporte())


if __name__ == "__main__":
    main()
