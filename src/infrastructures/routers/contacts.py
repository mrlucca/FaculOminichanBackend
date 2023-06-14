from fastapi import APIRouter

from src.controllers.contacts import ContactController
from src.entities.contact import ContactCreate, ContactListCreate
from src.infrastructures.repositories.contacts import ContactRepository


def get_contacts_router(repository_session) -> APIRouter:
    contacts_api = APIRouter(prefix='/contacts')

    @contacts_api.post("")
    async def create_contact(contact: ContactCreate):
        contact_repository = ContactRepository(repository_session())
        controller = ContactController(contact_repository)
        return await controller.create_contact(contact)

    @contacts_api.get("")
    async def get_contacts(email: str):
        contact_repository = ContactRepository(repository_session())
        controller = ContactController(contact_repository)
        return await controller.get_contacts(email)

    @contacts_api.post("/list")
    async def create_contact_list(contact_list: ContactListCreate):
        contact_repository = ContactRepository(repository_session())
        controller = ContactController(contact_repository)
        return await controller.create_contact_list(contact_list)
    
    return contacts_api