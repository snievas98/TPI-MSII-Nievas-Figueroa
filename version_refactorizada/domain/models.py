from dataclasses import dataclass
from version_refactorizada.domain.enums import EstadoSolicitud, Prioridad, TipoSolicitud
from version_refactorizada.domain.exceptions import DatosInvalidosError


@dataclass(frozen=True)
class Estudiante:
    legajo: str
    nombre: str
    email: str

    def __post_init__(self):
        if not self.legajo.strip() or not self.nombre.strip():
            raise DatosInvalidosError("Legajo y nombre son obligatorios")
        if "@" not in self.email:
            raise DatosInvalidosError("El email no tiene un formato válido")


@dataclass(frozen=True)
class Responsable:
    nombre: str
    area: str

    def __post_init__(self):
        if not self.nombre.strip() or not self.area.strip():
            raise DatosInvalidosError("Nombre y área del responsable son obligatorios")


@dataclass
class Solicitud:
    id: int
    codigo: str
    estudiante: Estudiante
    tipo: TipoSolicitud
    prioridad: Prioridad
    descripcion: str
    area: str
    estado: EstadoSolicitud = EstadoSolicitud.PENDIENTE
    responsable: Responsable | None = None

    def __post_init__(self):
        if not self.descripcion.strip():
            raise DatosInvalidosError("La descripción es obligatoria")
        if not self.area.strip():
            raise DatosInvalidosError("El área es obligatoria")

    def asignar_responsable(self, responsable: Responsable) -> None:
        self.responsable = responsable
        self.area = responsable.area

    def cambiar_estado(self, nuevo_estado: EstadoSolicitud) -> None:
        self.estado = nuevo_estado

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "codigo": self.codigo,
            "legajo": self.estudiante.legajo,
            "nombre": self.estudiante.nombre,
            "email": self.estudiante.email,
            "tipo": self.tipo.value,
            "prioridad": self.prioridad.name,
            "puntaje": int(self.prioridad),
            "descripcion": self.descripcion,
            "area": self.area,
            "responsable": self.responsable.nombre if self.responsable else "",
            "estado": self.estado.value,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Solicitud":
        responsable = None
        if data.get("responsable"):
            responsable = Responsable(data["responsable"], data["area"])
        return cls(
            id=int(data["id"]),
            codigo=data["codigo"],
            estudiante=Estudiante(data["legajo"], data["nombre"], data["email"]),
            tipo=TipoSolicitud(data["tipo"]),
            prioridad=Prioridad[data["prioridad"]],
            descripcion=data["descripcion"],
            area=data["area"],
            estado=EstadoSolicitud(data["estado"]),
            responsable=responsable,
        )
