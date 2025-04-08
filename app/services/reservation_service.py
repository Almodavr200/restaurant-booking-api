from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.reservation import Reservation

def is_conflict(db: Session, table_id: int, start_time: datetime, duration_minutes: int) -> bool:
    end_time = start_time + timedelta(minutes=duration_minutes)

    reservations = db.query(Reservation).filter(Reservation.table_id == table_id).all()

    for r in reservations:
        r_start = r.reservation_time
        r_end = r_start + timedelta(minutes=r.duration_minutes)
        if not (end_time <= r_start or start_time >= r_end):
            return True
    return False
