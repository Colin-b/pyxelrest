import multiprocessing

service_processes = []


def start_services(*services):
    service_processes[:] = []
    for service in services:
        service_processes.append(multiprocessing.Process(target=service[0].start_server, args=(service[1],)))

    for service_process in service_processes:
        service_process.start()


def stop_services():
    for service_process in service_processes:
        service_process.terminate()
        service_process.join(timeout=0.5)
    service_processes[:] = []
