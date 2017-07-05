import multiprocessing

from pyxelrest.oauth2_authentication_responses_server import wait_for_port

service_processes = []


def start_services(*services):
    del service_processes[:]
    for service in services:
        p = multiprocessing.Process(target=service[0].start_server, args=(service[1],))
        service_processes.append(p)
        p.start()
        wait_for_port('127.0.0.1', service[1])


def stop_services():
    for service_process in service_processes:
        service_process.terminate()
        service_process.join(timeout=0.5)
    del service_processes[:]
