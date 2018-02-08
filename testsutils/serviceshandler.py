import multiprocessing
import socket
import logging

service_processes = []

logger = logging.getLogger(__name__)


def start_services(*services):
    del service_processes[:]
    for service in services:
        p = multiprocessing.Process(target=service[0].start_server, args=(service[1],))
        service_processes.append(p)
        p.start()
        _wait_for_server_to_be_started('127.0.0.1', service[1])


def stop_services():
    for service_process in service_processes:
        service_process.terminate()
        service_process.join(timeout=0.5)
    del service_processes[:]


def cannot_connect_to_server(sock, host, port):
    try:
        sock.connect((host, port))
        return False
    except Exception:
        return True


def _wait_for_server_to_be_started(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while cannot_connect_to_server(sock, host, port):
        logger.info('Server still not started...')
    logger.info('Server is started')