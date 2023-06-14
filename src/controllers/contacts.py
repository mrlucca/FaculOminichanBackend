from src.entities.contact import ContactCreate, ContactListCreate
from src.infrastructures.repositories.contacts import ContactRepository


class ContactController:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    async def create_contact(self, email: str, contact: ContactCreate):
        await self.contact_repository.create(contact.client_email, contact)
        return {"message": "Contact created successfully"}

    async def get_contacts(self, email: str):
        return await self.contact_repository.get_by_email(email)

    async def create_contact_list(self, contact_list: ContactListCreate):
        for contact in contact_list.contacts:
            await self.contact_repository.create(contact_list.email, contact)
        return {"message": "Contact list created successfully"}
