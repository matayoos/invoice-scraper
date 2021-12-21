"""Create initial tables

Revision ID: 989877ebe0b0
Revises: 
Create Date: 2021-12-09 18:36:08.913994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "989877ebe0b0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "register_number",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cnpj", sa.String(255), nullable=False),
        sa.Column("inscricao_estadual", sa.String(255), nullable=False)
    )

    op.create_table(
        "grocery_store",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("address", sa.String(255), nullable=False),
        sa.Column("register_number_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["register_number_id"], ["register_number.id"])
    )

    op.create_table(
        "invoice_series",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("series_number", sa.String, nullable=False)
    )

    op.create_table(
        "invoice",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("url", sa.Text, nullable=False),
        sa.Column("date_time", sa.DateTime, nullable=False),
        sa.Column("access_key", sa.String(255), nullable=False),
        sa.Column("auth_protocole", sa.String(255), nullable=False),
        sa.Column("nfce_number", sa.String(255), nullable=False),
        sa.Column("final_value", sa.Numeric(10, 2), nullable=False),
        sa.Column("discount", sa.Numeric(10, 2)),
        sa.Column("grocery_store_id", sa.Integer, nullable=False),
        sa.Column("invoice_series_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["grocery_store_id"], ["grocery_store.id"]),
        sa.ForeignKeyConstraint(["invoice_series_id"], ["invoice_series.id"])
    )

    op.create_table(
        "item",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_id", sa.String, nullable=False),        
        sa.Column("grocery_store_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["grocery_store_id"], ["grocery_store.id"])
    )

    op.create_table(
        "category",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False)
    )

    op.create_table(
        "item_category",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_id", sa.Integer, nullable=False),
        sa.Column("category_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["item_id"], ["item.id"]),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"])
    )

    op.create_table(
        "unit",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False)
    )

    op.create_table(
        "item_details",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("unit_id", sa.Integer, nullable=False),
        sa.Column("item_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["item_id"], ["item.id"]),
        sa.ForeignKeyConstraint(["unit_id"], ["unit.id"])
    )

    op.create_table(
        "invoice_item",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_details_id", sa.Integer, nullable=False),
        sa.Column("invoice_id", sa.Integer, nullable=False),
        sa.Column("qty", sa.Numeric(10, 5), nullable=False),
        sa.Column("value", sa.Numeric(10, 2), nullable=False),
        sa.ForeignKeyConstraint(["item_details_id"], ["item_details.id"]),
        sa.ForeignKeyConstraint(["invoice_id"], ["invoice.id"])
    )


def downgrade():
    pass
