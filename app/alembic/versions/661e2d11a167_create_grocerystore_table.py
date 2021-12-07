"""create grocerystore table

Revision ID: 661e2d11a167
Revises: 
Create Date: 2021-12-06 18:14:15.568811

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import false, true


# revision identifiers, used by Alembic.
revision = "661e2d11a167"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "grocerystore",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("cnpj", sa.String(255), nullable=False),
        sa.Column("inscricao_estadual", sa.String(255), nullable=False),
        sa.Column("address", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_column("grocerystore")
