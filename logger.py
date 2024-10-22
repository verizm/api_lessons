import structlog

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, ensure_ascii=True)])
log = structlog.get_logger(__name__)
