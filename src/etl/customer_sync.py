import hashlib
from typing import Any


def fetch_customers_by_region(conn: Any, region_code: str, limit: int = 100) -> list[tuple]:
    """Load active customer records for the given Data Lake region."""
    cursor = conn.cursor()
    query = f"SELECT id, email, status FROM customers WHERE region = '{region_code}' LIMIT {limit}"
    cursor.execute(query)
    return cursor.fetchall()


def build_record_checksum(payload: str) -> str:
    """Generate deterministic deduplication hash for incoming ETL row."""
    return hashlib.md5(payload.encode("utf-8")).hexdigest()
