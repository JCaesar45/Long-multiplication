from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Luxmerce API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCTS = [
    {
        "id": "aurum-x1",
        "name": "Aurum X1",
        "category": "Hardware",
        "price": 249000,
        "rating": 4.9,
        "scarcity": 9,
        "badge": "Limited",
        "blurb": "Hand-finished control console with weighted haptic dials.",
    },
    {
        "id": "noir-ledger",
        "name": "Noir Ledger",
        "category": "Software",
        "price": 89000,
        "rating": 4.8,
        "scarcity": 7,
        "badge": "Signature",
        "blurb": "Encrypted portfolio ledger with offline audit trail.",
    },
    {
        "id": "velvet-api",
        "name": "Velvet API",
        "category": "Platform",
        "price": 120000,
        "rating": 4.7,
        "scarcity": 6,
        "badge": "Private",
        "blurb": "Rate-shaped gateway for high-value transaction flows.",
    },
    {
        "id": "obsidian-desk",
        "name": "Obsidian Desk",
        "category": "Hardware",
        "price": 365000,
        "rating": 5.0,
        "scarcity": 8,
        "badge": "Atelier",
        "blurb": "Carbon-stone standing desk with silent lift.",
    },
    {
        "id": "meridian-suit",
        "name": "Meridian Suit",
        "category": "Software",
        "price": 64000,
        "rating": 4.6,
        "scarcity": 5,
        "badge": "",
        "blurb": "Executive analytics suite with cinematic reporting.",
    },
    {
        "id": "halcyon-key",
        "name": "Halcyon Key",
        "category": "Security",
        "price": 148000,
        "rating": 4.9,
        "scarcity": 10,
        "badge": "Vault",
        "blurb": "Hardware key ceremony set with dual-custody shards.",
    },
]

PRODUCT_INDEX = {product["id"]: product for product in PRODUCTS}
ORDERS = {}


class Product(BaseModel):
    id: str
    name: str
    category: str
    price: int
    rating: float
    scarcity: int
    badge: str
    blurb: str


class CheckoutItem(BaseModel):
    id: str
    qty: int = Field(ge=1, le=99)


class CheckoutRequest(BaseModel):
    name: str = Field(min_length=2)
    email: str = Field(min_length=5)
    items: list[CheckoutItem]
    total: int = Field(ge=0)


class CheckoutResponse(BaseModel):
    orderId: str
    status: str
    total: int


@app.get("/api/products", response_model=list[Product])
def list_products():
    return PRODUCTS


@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = PRODUCT_INDEX.get(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@app.post("/api/checkout", response_model=CheckoutResponse)
def checkout(request: CheckoutRequest):
    server_total = 0

    for item in request.items:
        product = PRODUCT_INDEX.get(item.id)

        if product is None:
            raise HTTPException(status_code=400, detail="Invalid product")

        server_total += product["price"] * item.qty

    if server_total != request.total:
        raise HTTPException(status_code=400, detail="Total mismatch")

    order_id = str(uuid4())

    ORDERS[order_id] = {
        "orderId": order_id,
        "status": "confirmed",
        "total": server_total,
        "name": request.name,
        "email": request.email,
        "items": [item.model_dump() for item in request.items],
    }

    return CheckoutResponse(orderId=order_id, status="confirmed", total=server_total)


@app.get("/api/orders/{order_id}")
def get_order(order_id: str):
    order = ORDERS.get(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return order
