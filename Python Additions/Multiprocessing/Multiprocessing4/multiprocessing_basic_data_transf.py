import multiprocessing


def sender(conn):
    conn.send('Hello from sender')
    conn.close()


def receiver(conn):
    msg = conn.recv()
    print(f'Received: {msg}')


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(child_conn,))
    p2 = multiprocessing.Process(target=receiver, args=(parent_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
