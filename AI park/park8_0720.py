import multiprocessing as mp
import time

def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")


if __name__ == "__main__":
    # main process
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid) #운영체제서 정해준 아이디

    # process spawning
    p = mp.Process(name="SubProcess", target=worker) #프로세스 만들고 이름지어주고, 무슨일 할건지 worker에. 함수네?
    p.start()

    print("MainProcess End")
