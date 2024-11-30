from libs import *
from apps.db.models import async_main
from apps.handlers import *

async def main():
    await async_main()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")