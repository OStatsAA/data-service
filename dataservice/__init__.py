import asyncio
import logging

import grpc
from dataservice.proto.dataservice_pb2_grpc import add_DataServiceServicer_to_server
from dataservice.data_service import DataService


async def serve() -> None:
    """Service server bootstrap"""
    server = grpc.aio.server()
    add_DataServiceServicer_to_server(DataService(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
