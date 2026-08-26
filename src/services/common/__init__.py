
from src.services.common.application import create_application


class ApplicationService():
    upload_application = staticmethod(create_application)

application_service = ApplicationService()