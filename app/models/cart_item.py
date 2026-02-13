from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    DECIMAL,
    ForeignKey,
    func,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from app.models.base import Base

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(String(50), primary_key=True, index=True)

    cart_id = Column(
        String(50),
        ForeignKey("carts.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    product_id = Column(
        String(100),
        ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    quantity = Column(Integer, nullable=False)

    unit_price = Column(DECIMAL(10, 2), nullable=False)
    currency = Column(String(10), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("cart_id", "product_id", name="uq_cart_product"),
    )

    # Relationships
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product",back_populates="cart_items")
