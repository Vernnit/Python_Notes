# JUST EXPERIMENTING-->


import concurrent.futures as cf
import time

t1 = time.perf_counter()


def func():
    print('process started')
    time.sleep(1)
    print('process terminated')


if __name__ == '__main__':
    with cf.ProcessPoolExecutor() as executor:
        for _ in range(13):
            executor.submit(func)

        # for _ in range(12):
        #     executor.submit(func)

    t2 = time.perf_counter()

    print(f'time taken {t2-t1:.2f}')


# THIS MACHINE HAS 12 LOGICAL CORES SO 12 PROCESSES CAN RUN AT A TIME PARALLELLY SO IT TAKES APPROX. 1 SEC . BUT FOR EVEN 1 MORE PROCESS LIKE 13 IT IS ASSIGNED AGAIN TO SAY 1ST CORE , SO ALL 12 CORES RUNS 12 PROCESSES AND TAKES 1 SEC AND THEN 1 CORE PROCESSES 13TH PROCESS WHICH TAKES 1 SEC MORE SO ~ 2SEC ARE TAKEN .