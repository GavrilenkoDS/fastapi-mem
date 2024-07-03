import unittest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from ..app.core.db import get_db
from ..app.services.meme_service import get_memes, get_meme, create_meme, update_meme, delete_meme

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)

class TestMemeService(unittest.TestCase):

    def setUp(self):
        self.session = AsyncSession(engine)

    async def test_get_memes(self):
        async with self.session() as session:
            memes = await get_memes(session)
            self.assertIsInstance(memes, list)

    async def test_get_meme(self):
        async with self.session() as session:
            meme = await get_meme(session, meme_id=1)
            self.assertIsNotNone(meme)

    # Другие тесты для create_meme, update_meme, delete_meme

    def tearDown(self):
        self.session.close()

if __name__ == "__main__":
    unittest.main()
