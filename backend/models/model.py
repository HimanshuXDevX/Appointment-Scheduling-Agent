from pydantic import BaseModel
from typing import  Optional

class Patient(BaseModel):
    name: str
    email: str
    phone: str

class BookingRequest(BaseModel):
    appointment_type: str
    date: str
    start_time: str
    patient: Patient
    reason: Optional[str] = None

class Slot(BaseModel):
    start_time: str
    end_time: str
    available: bool