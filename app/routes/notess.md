-->What is APIRouter?
APIRouter helps us group related API endpoints into separate files.

---

from fastapi import APIRouter

router = APIRouter()

- Because we're defining the endpoint inside a separate router file rather than directly inside the main FastAPI application.

@router.get("/health")

def health_check():
return {"status": "healthy"}

---

-->health_router - contains the health-check endpoint.
prefix="/api/v1" adds /api/v1 before the endpoint's path.
/health + /api/v1 = /api/v1/health

-->Q. Why are we using Supabase in our Live Chat Support System?

We use Supabase to store and retrieve chat messages. Our FastAPI backend will communicate with the Supabase database to manage the application's data.
