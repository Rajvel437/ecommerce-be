from sqlalchemy import Column, String, DateTime, func, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.base import Base

class Cart(Base):
    __tablename__ = "carts"

    id = Column(String(50), primary_key=True, index=True)

    user_id = Column(
        String(100),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    status = Column(
        String(20),
        nullable=False,
        server_default="active"
    )

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Optional but STRONGLY recommended:
    # Ensures only one ACTIVE cart per user
    __table_args__ = (
        UniqueConstraint("user_id", "status", name="uq_user_cart_status"),
    )

    # Relationships
    items = relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete-orphan"
    )

    user = relationship("User", back_populates="carts")
