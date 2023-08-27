import multiprocessing
import time
import glob
import concurrent.futures
from joblib import Parallel, delayed

print("Number of cpu : ", multiprocessing.cpu_count())

def someProcess(inDir):
    fileLst = []
    jpgFiles = glob.glob(inDir + '/*.jpg', recursive=True)
    fileLst.append(jpgFiles)
    return(fileLst)

def someTask():
    files = someProcess(r'D:\Projects\WORKING\ML\imagery\CO_Water_Wildland\wildland')
    print(files)

def task():
    print('Sleeping for 0.5 seconds')
    time.sleep(0.5)
    print('Finished sleeping')

def cube(x):
    return x**3

if __name__ == "__main__":

    ### Part 1

    # # Start a time tracker
    # start_time = time.perf_counter()
    #
    # # Create a list for storing the process that will be run
    # processes = []
    #
    # # Creates 10 processes then starts them
    # for i in range(10):
    #     p = multiprocessing.Process(target=task)
    #     #p = multiprocessing.Process(target=someTask)
    #     p.start()
    #     processes.append(p)
    #
    # # Joins all the processes
    # for p in processes:
    #     p.join()
    #
    # finish_time = time.perf_counter()
    #
    # print(f"Program finished in {finish_time - start_time} seconds")

    ### Part 2

    # # Define the number of processes to pool i.e. the number of cores that will be used
    # pool = multiprocessing.Pool(3)
    #
    # # Start time tracking
    # start_time = time.perf_counter()
    #
    # # Define the process to run a function with list comprehension
    # # This uses “async” (asynchronous) because we don't want wait for the task to finish, and
    # # the main process may continue to run.
    # processes = [pool.apply_async(cube, args=(x,)) for x in range(1, 1000)]
    #
    # # The apply_async() function does not return the result but the object
    # # get(), to retrieve the result as the task to finishes
    # result = [p.get() for p in processes]
    #
    # finish_time = time.perf_counter()
    #
    # print(f"Program finished in {finish_time-start_time} seconds")
    # print(result)

    ### Part 3 map()

    # # Define the number of processes to pool i.e. the number of cores that will be used
    # pool = multiprocessing.Pool(3)
    #
    # # Start time tracking
    # start_time = time.perf_counter()
    #
    # # The start and join are hidden behind the pool.map() function. This splits the iterable range(1,1000)
    # # into chunks and runs each chunk in the pool. The map function is a parallel version of the
    # # list comprehension.
    # result = pool.map(cube, range(1,1000))
    #
    # finish_time = time.perf_counter()
    #
    # print(f"Program finished in {finish_time-start_time} seconds")
    # print(result)

    ### Part 4 Executor()

    # Use equivalent of using pool
    with concurrent.futures.ProcessPoolExecutor(3) as executor:

        start_time = time.perf_counter()

        # Running the multiprocessing module under the hood.
        result = list(executor.map(cube, range(1, 1000)))

        finish_time = time.perf_counter()

    print(f"Program finished in {finish_time - start_time} seconds")
    print(result)


    ### Part 5 joblib

    # start_time = time.perf_counter()
    #
    # # The Parallel n_jobs defines the number of processes to pool i.e. cores. The delayed()
    # # function is a wrapper to another function to make a “delayed” version of the function call.
    # # Which means it will not execute the function immediately when it is called.
    # result = Parallel(n_jobs=3)(delayed(cube)(i) for i in range(1, 1000))
    #
    # finish_time = time.perf_counter()
    #
    # print(f"Program finished in {finish_time - start_time} seconds")
    # print(result)
