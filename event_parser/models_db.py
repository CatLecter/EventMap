import uuid

from db import Base, engine
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON, TIMESTAMP, UUID


class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    event_id = Column(Integer())
    publication_date = Column(TIMESTAMP())
    dates = Column(JSON)
    title = Column(String())
    slug = Column(String())
    # place: Optional[PlaceBrief] = None
    description = Column(String())
    body_text = Column(String())
    location = Column(JSON)
    # categories: list[str]
    tagline = Column(String())
    # age_restriction: Any
    price = Column(String())
    is_free = Column(Boolean())
    # images: list[dict]
    favorites_count = Column(Integer())
    comments_count = Column(Integer())
    site_url = Column(String())
    short_title = Column(String())
    # tags: list[str]
    disable_comments = Column(Boolean())
    # participants: list

    def __repr__(self):
        return f"ID: {self.id}, title: {self.title}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
