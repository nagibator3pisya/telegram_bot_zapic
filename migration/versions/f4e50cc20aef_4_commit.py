"""4 commit

Revision ID: f4e50cc20aef
Revises: d7241c357180
Create Date: 2025-06-02 15:28:38.768936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4e50cc20aef'
down_revision: Union[str, None] = 'd7241c357180'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Убедитесь, что столбец `id` в таблице `users` имеет индекс
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)

    # Создайте таблицу `profile`
    op.create_table('profile',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=True),
        sa.Column('last_name', sa.String(length=50), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Создайте уникальное ограничение для столбца `telegram_id` в таблице `users`
    op.create_unique_constraint(None, 'users', ['telegram_id'])

def downgrade() -> None:
    """Downgrade schema."""
    # Удалите уникальное ограничение для столбца `telegram_id` в таблице `users`
    op.drop_constraint(None, 'users', type_='unique')

    # Удалите таблицу `profile`
    op.drop_table('profile')

    # Удалите индекс для столбца `id` в таблице `users`
    op.drop_index(op.f('ix_users_id'), 'users')

