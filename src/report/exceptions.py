class ReportError(Exception):
    """Base exception for reporting application errors."""


class CSVValidationError(ReportError):
    """Raised when the input CSV contains invalid data."""


class ReportWriteError(ReportError):
    """Raised when a report cannot be written."""