from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Notification(BaseModel):
    order_id: int
    product_id: int
    message: str


class OrderErrorEvent(BaseModel):
    """Isti JSON kontakt kao u products-service za greške narudžbine."""

    model_config = ConfigDict(extra="ignore")

    order_id: int
    product_id: int
    timestamp: datetime
    error_reason: str