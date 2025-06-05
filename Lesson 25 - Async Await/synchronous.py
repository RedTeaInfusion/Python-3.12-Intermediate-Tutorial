import time
from tqdm import tqdm

def run_task(name, steps, delay):
    with tqdm(total=steps, desc=name, position=int(name[-1])-1, leave=False) as pbar:
        for _ in range(steps):
            time.sleep(delay)
            pbar.update(1)

def run_tasks(delays, steps_per_task):
    task_1 = run_task('Task 1', steps_per_task, delays[0])
    task_2 = run_task('Task 2', steps_per_task, delays[1])
    task_3 = run_task('Task 3', steps_per_task, delays[2])

def run_sync_pipeline(shared_delays, steps_per_task):
    print('\n=== Synchronous Execution ===')
    print(f'Delays: {shared_delays[0]}, \
                    {shared_delays[1]}, \
                    {shared_delays[2]},')
    start = time.time()
    run_tasks(shared_delays, steps_per_task)
    end = time.time()
    print(f'\n\n\nSync executed in {end - start:.2f} seconds')