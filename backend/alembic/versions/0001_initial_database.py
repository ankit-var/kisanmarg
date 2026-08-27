"""initial database

Revision ID: 0001_initial
Revises: 
Create Date: 2026-08-27 17:05:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. users
    op.create_table(
        'users',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('email', sa.String(length=255), unique=True, nullable=True),
        sa.Column('phone', sa.String(length=20), unique=True, nullable=False),
        sa.Column('full_name', sa.String(length=100), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('role', sa.String(length=30), nullable=False, server_default='farmer'),
        sa.Column('preferred_language', sa.String(length=20), server_default='hi'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('is_superuser', sa.Boolean(), server_default='false'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_users_id', 'users', ['id'])
    op.create_index('ix_users_phone', 'users', ['phone'], unique=True)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_role', 'users', ['role'])

    # 2. farmer_profiles
    op.create_table(
        'farmer_profiles',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False),
        sa.Column('primary_district', sa.String(length=100), server_default='Nashik'),
        sa.Column('primary_state', sa.String(length=100), server_default='Maharashtra'),
        sa.Column('default_crop', sa.String(length=100), server_default='Tomato'),
        sa.Column('land_size_acres', sa.Float(), server_default='2.0'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_farmer_profiles_id', 'farmer_profiles', ['id'])
    op.create_index('ix_farmer_profiles_user_id', 'farmer_profiles', ['user_id'])
    op.create_index('ix_farmer_profiles_primary_district', 'farmer_profiles', ['primary_district'])

    # 3. farming_records
    op.create_table(
        'farming_records',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('crop_name', sa.String(length=100), nullable=False),
        sa.Column('variety', sa.String(length=100), server_default='Hybrid'),
        sa.Column('area_acres', sa.Float(), server_default='1.5'),
        sa.Column('sowing_date', sa.Date(), nullable=True),
        sa.Column('harvest_expected_date', sa.Date(), nullable=True),
        sa.Column('estimated_yield_kg', sa.Float(), server_default='5000.0'),
        sa.Column('status', sa.String(length=50), server_default='growing'),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_farming_records_id', 'farming_records', ['id'])
    op.create_index('ix_farming_records_user_id', 'farming_records', ['user_id'])
    op.create_index('ix_farming_records_crop_name', 'farming_records', ['crop_name'])
    op.create_index('ix_farming_records_status', 'farming_records', ['status'])

    # 4. conversation_sessions
    op.create_table(
        'conversation_sessions',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('session_title', sa.String(length=200), server_default='मंडी भाव बातचीत (Mandi Query)'),
        sa.Column('language', sa.String(length=20), server_default='hi'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_conversation_sessions_id', 'conversation_sessions', ['id'])
    op.create_index('ix_conversation_sessions_user_id', 'conversation_sessions', ['user_id'])

    # 5. chat_messages
    op.create_table(
        'chat_messages',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('session_id', sa.String(length=36), sa.ForeignKey('conversation_sessions.id', ondelete='CASCADE'), nullable=False),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('sender_type', sa.String(length=30), server_default='user'),
        sa.Column('query_transcript', sa.Text(), nullable=False),
        sa.Column('intent', sa.String(length=50), nullable=True),
        sa.Column('extracted_entities', sa.JSON(), nullable=True),
        sa.Column('response_text', sa.Text(), nullable=True),
        sa.Column('audio_script', sa.Text(), nullable=True),
        sa.Column('audio_duration_seconds', sa.Float(), server_default='0.0'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_chat_messages_id', 'chat_messages', ['id'])
    op.create_index('ix_chat_messages_session_id', 'chat_messages', ['session_id'])
    op.create_index('ix_chat_messages_user_id', 'chat_messages', ['user_id'])

    # 6. mandis
    op.create_table(
        'mandis',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=150), unique=True, nullable=False),
        sa.Column('hindi_name', sa.String(length=150), nullable=False),
        sa.Column('district', sa.String(length=100), nullable=False),
        sa.Column('state', sa.String(length=100), server_default='Maharashtra'),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_mandis_id', 'mandis', ['id'])
    op.create_index('ix_mandis_name', 'mandis', ['name'], unique=True)
    op.create_index('ix_mandis_district', 'mandis', ['district'])

    # 7. commodities
    op.create_table(
        'commodities',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), unique=True, nullable=False),
        sa.Column('hindi_name', sa.String(length=100), nullable=False),
        sa.Column('category', sa.String(length=50), server_default='Vegetables'),
        sa.Column('unit', sa.String(length=20), server_default='kg'),
        sa.Column('image_url', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_commodities_id', 'commodities', ['id'])
    op.create_index('ix_commodities_name', 'commodities', ['name'], unique=True)

    # 8. mandi_prices
    op.create_table(
        'mandi_prices',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('mandi_id', sa.Integer(), sa.ForeignKey('mandis.id', ondelete='CASCADE'), nullable=False),
        sa.Column('commodity_id', sa.Integer(), sa.ForeignKey('commodities.id', ondelete='CASCADE'), nullable=False),
        sa.Column('min_price_quintal', sa.Float(), nullable=False),
        sa.Column('max_price_quintal', sa.Float(), nullable=False),
        sa.Column('modal_price_quintal', sa.Float(), nullable=False),
        sa.Column('price_per_kg', sa.Float(), nullable=False),
        sa.Column('arrivals_tonnes', sa.Float(), server_default='150.0'),
        sa.Column('grade', sa.String(length=20), server_default='Grade A'),
        sa.Column('price_date', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_mandi_prices_id', 'mandi_prices', ['id'])
    op.create_index('ix_mandi_prices_mandi_id', 'mandi_prices', ['mandi_id'])
    op.create_index('ix_mandi_prices_commodity_id', 'mandi_prices', ['commodity_id'])
    op.create_index('ix_mandi_prices_price_per_kg', 'mandi_prices', ['price_per_kg'])
    op.create_index('ix_mandi_prices_price_date', 'mandi_prices', ['price_date'])

    # 9. route_queries
    op.create_table(
        'route_queries',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('crop', sa.String(length=100), nullable=False),
        sa.Column('district', sa.String(length=100), nullable=False),
        sa.Column('quantity_kg', sa.Float(), nullable=False),
        sa.Column('user_language', sa.String(length=20), server_default='hi'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_route_queries_id', 'route_queries', ['id'])
    op.create_index('ix_route_queries_user_id', 'route_queries', ['user_id'])
    op.create_index('ix_route_queries_created_at', 'route_queries', ['created_at'])

    # 10. advice_results
    op.create_table(
        'advice_results',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('query_id', sa.String(length=36), sa.ForeignKey('route_queries.id', ondelete='CASCADE'), unique=True, nullable=False),
        sa.Column('recommended_mandi', sa.String(length=150), nullable=False),
        sa.Column('recommended_mandi_hi', sa.String(length=150), nullable=False),
        sa.Column('mandi_price_per_kg', sa.Float(), nullable=False),
        sa.Column('transport_cost_per_kg', sa.Float(), nullable=False),
        sa.Column('net_price_per_kg', sa.Float(), nullable=False),
        sa.Column('nearby_mandi', sa.String(length=150), nullable=False),
        sa.Column('nearby_mandi_hi', sa.String(length=150), nullable=False),
        sa.Column('nearby_price_per_kg', sa.Float(), nullable=False),
        sa.Column('extra_gain_per_kg', sa.Float(), nullable=False),
        sa.Column('total_extra_gain', sa.Float(), nullable=False),
        sa.Column('distance_km', sa.Float(), nullable=False),
        sa.Column('spoken_text_hi', sa.Text(), nullable=False),
        sa.Column('spoken_text_en', sa.Text(), nullable=False),
        sa.Column('audio_duration_seconds', sa.Float(), server_default='14.0'),
        sa.Column('breakdown', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_advice_results_id', 'advice_results', ['id'])
    op.create_index('ix_advice_results_query_id', 'advice_results', ['query_id'])

    # 11. trader_evaluations
    op.create_table(
        'trader_evaluations',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('crop', sa.String(length=100), nullable=False),
        sa.Column('district', sa.String(length=100), nullable=False),
        sa.Column('offer_price_per_kg', sa.Float(), nullable=False),
        sa.Column('benchmark_mandi_price', sa.Float(), nullable=False),
        sa.Column('target_price_per_kg', sa.Float(), nullable=False),
        sa.Column('target_price_max', sa.Float(), nullable=False),
        sa.Column('is_fair_price', sa.Boolean(), server_default='false'),
        sa.Column('verdict', sa.String(length=50), nullable=False),
        sa.Column('warning_text_hi', sa.Text(), nullable=False),
        sa.Column('warning_text_en', sa.Text(), nullable=False),
        sa.Column('bargaining_script_hi', sa.Text(), nullable=False),
        sa.Column('bargaining_script_en', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_trader_evaluations_id', 'trader_evaluations', ['id'])
    op.create_index('ix_trader_evaluations_user_id', 'trader_evaluations', ['user_id'])
    op.create_index('ix_trader_evaluations_created_at', 'trader_evaluations', ['created_at'])

    # 12. daily_alerts
    op.create_table(
        'daily_alerts',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('crop', sa.String(length=100), nullable=False),
        sa.Column('district', sa.String(length=100), nullable=False),
        sa.Column('channel', sa.String(length=30), server_default='whatsapp_and_audio'),
        sa.Column('scheduled_time', sa.Time(), nullable=False),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_daily_alerts_id', 'daily_alerts', ['id'])
    op.create_index('ix_daily_alerts_user_id', 'daily_alerts', ['user_id'])
    op.create_index('ix_daily_alerts_phone', 'daily_alerts', ['phone'])
    op.create_index('ix_daily_alerts_crop', 'daily_alerts', ['crop'])
    op.create_index('ix_daily_alerts_district', 'daily_alerts', ['district'])
    op.create_index('ix_daily_alerts_is_active', 'daily_alerts', ['is_active'])

    # 13. notification_logs
    op.create_table(
        'notification_logs',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('alert_id', sa.String(length=36), sa.ForeignKey('daily_alerts.id', ondelete='CASCADE'), nullable=False),
        sa.Column('recipient', sa.String(length=50), nullable=False),
        sa.Column('status', sa.String(length=30), server_default='sent'),
        sa.Column('message_content', sa.String(length=500), nullable=False),
        sa.Column('sent_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_notification_logs_id', 'notification_logs', ['id'])
    op.create_index('ix_notification_logs_alert_id', 'notification_logs', ['alert_id'])


def downgrade() -> None:
    op.drop_table('notification_logs')
    op.drop_table('daily_alerts')
    op.drop_table('trader_evaluations')
    op.drop_table('advice_results')
    op.drop_table('route_queries')
    op.drop_table('mandi_prices')
    op.drop_table('commodities')
    op.drop_table('mandis')
    op.drop_table('chat_messages')
    op.drop_table('conversation_sessions')
    op.drop_table('farming_records')
    op.drop_table('farmer_profiles')
    op.drop_table('users')
