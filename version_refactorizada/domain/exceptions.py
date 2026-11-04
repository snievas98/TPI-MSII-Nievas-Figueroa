class SolicitudError(Exception):
    """Error base del dominio de solicitudes."""


class DatosInvalidosError(SolicitudError):
    pass


class SolicitudNoEncontradaError(SolicitudError):
    pass
