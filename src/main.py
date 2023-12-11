from aio_utils import main
import asyncio
import logging
import sys


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
asyncio.run(main())
