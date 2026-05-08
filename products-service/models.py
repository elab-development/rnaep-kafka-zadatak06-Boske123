from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


class OrderErrorEvent(BaseModel):
    """JSON payload za Kafka topic-e grešaka (product_not_found_events, out_of_stock_events)."""

    model_config = ConfigDict(extra="forbid")

    order_id: int
    product_id: int
    timestamp: datetime
    error_reason: str