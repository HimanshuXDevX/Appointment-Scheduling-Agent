from fastapi import APIRouter, HTTPException, BackgroundTasks, Query
from models.model import Patient, BookingRequest, Slot
import json, time, uuid, logging

router = APIRouter(prefix="/api/calendly", tags=["Calendly API"])

with open("data/slots.json", "r") as f:
    slots_data = json.load(f)

logger = logging.getLogger(__name__)

def simulate_availability_check(date: str, appointment_type: str):
    time.sleep(1.5)
    logger.info(f"Fetched availability for {appointment_type} on {date}")


@router.get("/availability")
def get_availability(
    background_tasks: BackgroundTasks,
    date: str = Query(..., description="Date in YYYY-MM-DD"),
    appointment_type: str = Query(..., description="Type of appointment"),
):
    try:
        background_tasks.add_task(simulate_availability_check, date, appointment_type)
        slots = slots_data.get(date, {}).get(appointment_type)
        if not slots:
            raise HTTPException(
                status_code=404,
                detail=f"No availability found for '{appointment_type}' on {date}"
            )
        return {"date": date, "available_slots": slots}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch availability: {str(e)}")


@router.post("/book")
def book_appointment(request: BookingRequest):
    booking_id = f"APPT-{request.date.replace('-', '')}-{uuid.uuid4().hex[:3].upper()}"
    confirmation_code = uuid.uuid4().hex[:6].upper()
    
    if request.date in slots_data and request.appointment_type in slots_data[request.date]:
        for slot in slots_data[request.date][request.appointment_type]:
            if slot["start_time"] == request.start_time:
                slot["available"] = False
    
    return {
        "booking_id": booking_id,
        "status": "confirmed",
        "confirmation_code": confirmation_code,
        "details": request.dict()
    }
