"""create carts and cart_items tables

Revision ID: c155ec61e363
Revises: 62c4e9ad21a2
Create Date: 2026-02-09 08:32:53.824159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c155ec61e363'
down_revision: Union[str, Sequence[str], None] = '62c4e9ad21a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
