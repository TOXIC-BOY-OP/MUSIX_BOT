import os
API_ID = int(os.getenv("25374274"))
API_HASH = os.getenv("d0012f0876e6f9308eec2f474e7b9273")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list({int(x) for x in os.environ.get("6109531260", "").split()})
