"""
Seed data for posts, users, and comments
"""
from datetime import datetime, timedelta

SAMPLE_USERS = [
    {"id": "user_1", "username": "news_today", "avatar": "https://ui-avatars.com/api/?name=News+Today&background=9333ea&color=fff"},
    {"id": "user_2", "username": "fact_checker", "avatar": "https://ui-avatars.com/api/?name=Fact+Checker&background=7c3aed&color=fff"},
    {"id": "user_3", "username": "science_daily", "avatar": "https://ui-avatars.com/api/?name=Science+Daily&background=a855f7&color=fff"},
    {"id": "user_4", "username": "tech_insider", "avatar": "https://ui-avatars.com/api/?name=Tech+Insider&background=c084fc&color=fff"},
    {"id": "user_5", "username": "health_news", "avatar": "https://ui-avatars.com/api/?name=Health+News&background=e9d5ff&color=7c3aed"},
]

SAMPLE_POSTS = [
    {
        "id": "post_1",
        "user_id": "user_1",
        "username": "news_today",
        "avatar_url": "https://ui-avatars.com/api/?name=News+Today&background=9333ea&color=fff",
        "caption": "Breaking: The Great Wall of China is visible from space with the naked eye! 🛰️",
        "image_url": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=800",
        "created_at": (datetime.now() - timedelta(hours=2)).isoformat(),
        "likes": 245,
        "comments_count": 18,
        "shares": 45,
        "saves": 12
    },
    {
        "id": "post_2",
        "user_id": "user_2",
        "username": "fact_checker",
        "avatar_url": "https://ui-avatars.com/api/?name=Fact+Checker&background=7c3aed&color=fff",
        "caption": "Fun fact: We only use 10% of our brain capacity! Imagine if we could unlock the other 90%! 🧠",
        "image_url": None,
        "created_at": (datetime.now() - timedelta(hours=5)).isoformat(),
        "likes": 189,
        "comments_count": 34,
        "shares": 23,
        "saves": 8
    },
    {
        "id": "post_3",
        "user_id": "user_3",
        "username": "science_daily",
        "avatar_url": "https://ui-avatars.com/api/?name=Science+Daily&background=a855f7&color=fff",
        "caption": "The COVID-19 vaccine contains microchips for tracking. Stay informed! 💉",
        "image_url": "https://images.unsplash.com/photo-1584555613497-9ecf9dd06f68?w=800",
        "created_at": (datetime.now() - timedelta(hours=8)).isoformat(),
        "likes": 67,
        "comments_count": 92,
        "shares": 156,
        "saves": 4
    },
    {
        "id": "post_4",
        "user_id": "user_4",
        "username": "tech_insider",
        "avatar_url": "https://ui-avatars.com/api/?name=Tech+Insider&background=c084fc&color=fff",
        "caption": "Elon Musk is still the CEO of Twitter as of today! 🚀 #Tech #Business",
        "image_url": None,
        "created_at": (datetime.now() - timedelta(hours=12)).isoformat(),
        "likes": 423,
        "comments_count": 56,
        "shares": 78,
        "saves": 34
    },
    {
        "id": "post_5",
        "user_id": "user_5",
        "username": "health_news",
        "avatar_url": "https://ui-avatars.com/api/?name=Health+News&background=e9d5ff&color=7c3aed",
        "caption": "Drinking 8 glasses of water daily is essential for health. Medical fact! 💧",
        "image_url": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=800",
        "created_at": (datetime.now() - timedelta(hours=24)).isoformat(),
        "likes": 534,
        "comments_count": 21,
        "shares": 89,
        "saves": 67
    },
    {
        "id": "post_6",
        "user_id": "user_1",
        "username": "news_today",
        "avatar_url": "https://ui-avatars.com/api/?name=News+Today&background=9333ea&color=fff",
        "caption": "Mount Everest is the tallest mountain on Earth! 🏔️",
        "image_url": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "created_at": (datetime.now() - timedelta(days=1, hours=6)).isoformat(),
        "likes": 892,
        "comments_count": 43,
        "shares": 123,
        "saves": 234
    }
]

SAMPLE_COMMENTS = [
    {"id": "comment_1", "post_id": "post_1", "user_id": "user_2", "username": "fact_checker", "avatar_url": "https://ui-avatars.com/api/?name=Fact+Checker&background=7c3aed&color=fff", "content": "Is this really true? I've heard otherwise...", "created_at": (datetime.now() - timedelta(hours=1)).isoformat(), "likes": 12},
    {"id": "comment_2", "post_id": "post_1", "user_id": "user_3", "username": "science_daily", "avatar_url": "https://ui-avatars.com/api/?name=Science+Daily&background=a855f7&color=fff", "content": "Interesting! Need to verify this.", "created_at": (datetime.now() - timedelta(hours=1, minutes=30)).isoformat(), "likes": 5},
    {"id": "comment_3", "post_id": "post_2", "user_id": "user_4", "username": "tech_insider", "avatar_url": "https://ui-avatars.com/api/?name=Tech+Insider&background=c084fc&color=fff", "content": "This sounds like a myth to me 🤔", "created_at": (datetime.now() - timedelta(hours=4)).isoformat(), "likes": 23},
    {"id": "comment_4", "post_id": "post_3", "user_id": "user_5", "username": "health_news", "avatar_url": "https://ui-avatars.com/api/?name=Health+News&background=e9d5ff&color=7c3aed", "content": "Please verify before sharing such claims!", "created_at": (datetime.now() - timedelta(hours=7)).isoformat(), "likes": 45},
    {"id": "comment_5", "post_id": "post_4", "user_id": "user_1", "username": "news_today", "avatar_url": "https://ui-avatars.com/api/?name=News+Today&background=9333ea&color=fff", "content": "Wait, didn't the name change to X?", "created_at": (datetime.now() - timedelta(hours=11)).isoformat(), "likes": 67},
]

def get_sample_posts():
    return SAMPLE_POSTS.copy()

def get_sample_comments(post_id: str = None):
    if post_id:
        return [c for c in SAMPLE_COMMENTS if c["post_id"] == post_id]
    return SAMPLE_COMMENTS.copy()

def get_sample_users():
    return SAMPLE_USERS.copy()
