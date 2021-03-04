from api.utils import auth_func
import asyncio

async def main():
    await auth_func.get_current_active_user()

asyncio.run(main())