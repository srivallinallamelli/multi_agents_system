from sqlalchemy import create_engine
from configs.settings import DB_URL

engine = create_engine(
    DB_URL,
    echo=False
)