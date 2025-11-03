# Appointment Scheduling Agent (Calendly-like API)

An appointment scheduling backend built with **FastAPI**.  
It supports mock Calendly-like APIs for checking availability and booking appointments, with easy extensibility for integration with real Calendly or similar systems.


## 🚀 1. Setup Instructions
Make sure you have the following installed:
- **Python 3.9+**
- **pip** (Python package manager)
- **virtualenv** (recommended)

## 🧰 Project Setup

# Clone the repository
git clone https://github.com/HimanshuXDevX/Appointment-Scheduling-Agent.git
cd appointment-scheduling-agent/backend

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


## 2. System Design
backend/
│
├── main.py                # Entry point; initializes FastAPI app
│
├── api/
│   └── mock_calendly      # Availability & booking endpoints
│
├── models/
│   └── model.py           # Pydantic models for validation
│
└── data/
    └── slots.json         # Mock slot data source


- FastAPI	Framework for API creation
- Pydantic Models	Validates booking and slot data
- JSON Mock Data	Simulates available time slots
- BackgroundTasks	Mimics async external API calls
- Logging	Tracks requests and internal activity
- CORS Middleware	Enables access from any frontend

3. Scheduling Logic
- Each date in data/slots.json contains appointment types.
- Each appointment type holds a list of time slots:

- The /api/calendly/availability endpoint checks if slots exist for that date and type.
- If found, it returns all available time slots; otherwise, returns a 404.

⚙️ Appointment Type Handling
- Appointment types (e.g., consultation, follow-up) are keys in the JSON structure.
- Each can have independent schedules and slot lists.

🚫 Conflict Prevention
- When /api/calendly/book is called:
- The system verifies that the slot is still marked as available: true.
- It then marks that slot as available: false.
- Returns a unique booking ID and confirmation code.
- Future enhancement ideas:
- Use database persistence (MongoDB/PostgreSQL) instead of in-memory JSON.
- Implement transaction locks to handle concurrent booking attempts.


4. Testing
Manual Testing (via Postman)
GET /api/calendly/availability → Check available slots.
POST /api/calendly/book → Create a mock booking.

Edge Cases Covered
- Invalid date- Returns 404 with a descriptive message
- Missing appointment type- Returns 400 (validation error)
- Double booking same slot- Marks slot unavailable after first booking
- Empty slot data file- Returns 500 with “Failed to fetch availability”
- Background task simulation- Non-blocking request (uses BackgroundTasks)