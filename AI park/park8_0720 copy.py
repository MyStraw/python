from multiprocessing import Pool
import time

def work(x):
    #print(x)
    for _ in range(10):
        y = x**2


if __name__ == "__main__":
    pool = Pool(4) #일꾼 4개를 만들고
    data = range(1, 100000) #일꾼들이 사용할 데이터 준비
    t0 = time.time_ns()
    pool.map(work, data) #던져줘. 4명 일꾼이 있는 pool에 던져줘
    t1 = time.time_ns()
    
    print(f'Time:{t1-t0} (ns)')