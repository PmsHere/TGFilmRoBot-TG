import motor.motor_asyncio

from info import AUTH_CHANNEL, DATABASE_NAME, DATABASE_URI


class DB:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.fsub = self.db.fsub

    async def edit_fsub(self, fsub):
        await self.fsub.update_one(
            {"key": "FSUB"}, {"$set": {"value": fsub}}, upsert=True
        )

    async def get_fsub(self):
        data = await self.fsub.find_one({"key": "FSUB"})
        if not data:
            return AUTH_CHANNEL
        return data.get("value")

    async def editJoin(self, status):
        await self.fsub.update_one(
            {"key": "JOIN_REQUEST"}, {"$set": {"value": status}}, upsert=True
        )

    async def getJoin(self):
        data = await self.fsub.find_one({"key": "JOIN_REQUEST"})
        if not data:
            return True
        return data.get("value")


force_sub_db = DB(DATABASE_URI, DATABASE_NAME)
