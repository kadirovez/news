from fastapi import APIRouter, Depends, Request
# from src.services.i18n import i18n

def get_ip_address() -> str:
    """Get IP address from request headers."""
    request = Request
    return request.client.host
