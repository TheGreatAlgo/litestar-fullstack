import asyncio

from app.lib import log

logger = log.get_logger()


async def system_upkeep(_: dict) -> None:
    await logger.ainfo("Performing system upkeep operations.")
    await logger.ainfo("Simulating a long running operation.  Sleeping for 60 seconds.")
    await asyncio.sleep(60)
    await logger.ainfo("Simulating an even long running operation.  Sleeping for 120 seconds.")
    await asyncio.sleep(120)
    await logger.ainfo("Long running process complete.")
    await logger.ainfo("Performing system upkeep operations.")


async def background_worker_task(_: dict) -> None:
    await logger.ainfo("Performing background worker task.")
    await asyncio.sleep(20)
    await logger.ainfo("Performing system upkeep operations.")


async def system_task(_: dict) -> None:
    await logger.ainfo("Performing simple system task")
    await asyncio.sleep(2)
    await logger.ainfo("System task complete.")