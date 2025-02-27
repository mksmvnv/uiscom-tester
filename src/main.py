import aiofiles

from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI(
    title="UIS test",
)


class NotificationData(BaseModel):
    call_session_id: int
    notification_time: str
    contact_phone_number: int


@app.post(
    "/webhook", response_model=NotificationData, status_code=status.HTTP_200_OK
)
async def get_notification_data(data: NotificationData) -> NotificationData:
    formatted_data = data.model_dump()
    async with aiofiles.open("notifications.txt", "a") as f:
        await f.write(f"{formatted_data}\n")
    return NotificationData(**formatted_data)
