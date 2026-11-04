import json
from pathlib import Path


class SistemaSolicitudes:
    """Versión inicial: funcional, pero deliberadamente difícil de mantener."""

    def __init__(self, archivo="solicitudes.json"):
        self.archivo = Path(archivo)
        self.s = []
        try:
            if self.archivo.exists():
                with self.archivo.open("r", encoding="utf-8") as f:
                    self.s = json.load(f)
        except Exception:
            self.s = []

    def guardar(self):
        self.archivo.parent.mkdir(parents=True, exist_ok=True)
        with self.archivo.open("w", encoding="utf-8") as f:
            json.dump(self.s, f, ensure_ascii=False, indent=2)

    def registrar(self, legajo, nombre, email, tipo, prioridad, descripcion, area, responsable=""):
        # La lógica de validación, normalización, generación de ID y persistencia
        # se encuentra mezclada en un único método.
        if not legajo or not nombre or not email or "@" not in email or not descripcion:
            return None
        if tipo not in ["CERTIFICADO", "EQUIVALENCIA", "EXAMEN", "BECA"]:
            return None
        if prioridad not in ["BAJA", "MEDIA", "ALTA"]:
            prioridad = "MEDIA"
        if area == "":
            area = "SECRETARIA_ACADEMICA"

        numero = 1
        if len(self.s) > 0:
            numero = max(x["id"] for x in self.s) + 1

        codigo = "SOL-" + str(numero).zfill(4)
        if tipo == "CERTIFICADO":
            codigo = "CER-" + str(numero).zfill(4)
        elif tipo == "EQUIVALENCIA":
            codigo = "EQU-" + str(numero).zfill(4)
        elif tipo == "EXAMEN":
            codigo = "EXA-" + str(numero).zfill(4)
        elif tipo == "BECA":
            codigo = "BEC-" + str(numero).zfill(4)

        if prioridad == "ALTA":
            puntaje = 3
        elif prioridad == "MEDIA":
            puntaje = 2
        else:
            puntaje = 1

        x = {
            "id": numero,
            "codigo": codigo,
            "legajo": legajo,
            "nombre": nombre.strip(),
            "email": email.strip().lower(),
            "tipo": tipo,
            "prioridad": prioridad,
            "puntaje": puntaje,
            "descripcion": descripcion.strip(),
            "area": area,
            "responsable": responsable,
            "estado": "PENDIENTE",
        }
        self.s.append(x)
        self.guardar()
        return x

    def asignar(self, solicitud_id, responsable, area):
        for x in self.s:
            if x["id"] == solicitud_id:
                x["responsable"] = responsable
                x["area"] = area
                self.guardar()
                return True
        return False

    def cambiar_estado(self, solicitud_id, nuevo_estado):
        if nuevo_estado not in ["PENDIENTE", "EN_PROCESO", "RESUELTA", "RECHAZADA"]:
            return False
        for x in self.s:
            if x["id"] == solicitud_id:
                x["estado"] = nuevo_estado
                self.guardar()
                return True
        return False

    def buscar(self, campo, valor):
        r = []
        for x in self.s:
            if campo == "estado" and x["estado"] == valor:
                r.append(x)
            elif campo == "tipo" and x["tipo"] == valor:
                r.append(x)
            elif campo == "prioridad" and x["prioridad"] == valor:
                r.append(x)
            elif campo == "area" and x["area"] == valor:
                r.append(x)
            elif campo == "responsable" and x["responsable"] == valor:
                r.append(x)
        return r

    def reporte(self):
        total = len(self.s)
        pendientes = 0
        en_proceso = 0
        resueltas = 0
        rechazadas = 0
        altas = 0
        medias = 0
        bajas = 0
        for x in self.s:
            if x["estado"] == "PENDIENTE":
                pendientes += 1
            if x["estado"] == "EN_PROCESO":
                en_proceso += 1
            if x["estado"] == "RESUELTA":
                resueltas += 1
            if x["estado"] == "RECHAZADA":
                rechazadas += 1
            if x["prioridad"] == "ALTA":
                altas += 1
            if x["prioridad"] == "MEDIA":
                medias += 1
            if x["prioridad"] == "BAJA":
                bajas += 1
        return {
            "total": total,
            "por_estado": {
                "PENDIENTE": pendientes,
                "EN_PROCESO": en_proceso,
                "RESUELTA": resueltas,
                "RECHAZADA": rechazadas,
            },
            "por_prioridad": {"ALTA": altas, "MEDIA": medias, "BAJA": bajas},
        }
