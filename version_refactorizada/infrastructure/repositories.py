import json
from pathlib import Path
from typing import Protocol

from version_refactorizada.domain.models import Solicitud


class SolicitudReader(Protocol):
    def list_all(self) -> list[Solicitud]: ...
    def get_by_id(self, solicitud_id: int) -> Solicitud | None: ...


class SolicitudWriter(Protocol):
    def save_all(self, solicitudes: list[Solicitud]) -> None: ...


class SolicitudRepository(SolicitudReader, SolicitudWriter, Protocol):
    pass


class JsonSolicitudRepository:
    """Adaptador de persistencia JSON. El servicio depende del contrato, no de esta clase."""

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def list_all(self) -> list[Solicitud]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as file:
            raw = json.load(file)
        return [Solicitud.from_dict(item) for item in raw]

    def get_by_id(self, solicitud_id: int) -> Solicitud | None:
        return next((s for s in self.list_all() if s.id == solicitud_id), None)

    def save_all(self, solicitudes: list[Solicitud]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as file:
            json.dump([s.to_dict() for s in solicitudes], file, ensure_ascii=False, indent=2)


class InMemorySolicitudRepository:
    """Implementación alternativa usada por pruebas; demuestra sustitución por el mismo contrato."""

    def __init__(self):
        self._items: list[Solicitud] = []

    def list_all(self) -> list[Solicitud]:
        return list(self._items)

    def get_by_id(self, solicitud_id: int) -> Solicitud | None:
        return next((s for s in self._items if s.id == solicitud_id), None)

    def save_all(self, solicitudes: list[Solicitud]) -> None:
        self._items = list(solicitudes)
