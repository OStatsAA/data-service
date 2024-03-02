"""
Server module
"""

import asyncio
import logging
import os

import grpc
from dataservice.config import Config, get_config
from dataservice.proto.dataservice_pb2_grpc import add_DataServiceServicer_to_server
from dataservice.data_service import DataService


async def serve(config: Config) -> None:
    """Service server bootstrap"""
    server = grpc.aio.server()
    add_DataServiceServicer_to_server(DataService(config), server)
    listen_addr = config["LISTEN_ADDR"]
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    _config = get_config(os.getenv("ENVIRONMENT", "DEFAULT"))
    logging.basicConfig(level=logging.INFO)
    if not os.path.exists(f'{_config["DATASETS_DIR"]}/'):
        os.mkdir(f'{_config["DATASETS_DIR"]}/')
    asyncio.run(serve(_config))
