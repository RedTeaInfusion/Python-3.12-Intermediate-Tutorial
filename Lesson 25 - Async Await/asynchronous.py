import time
import asyncio
from tqdm import tqdm

async def run_task(name, steps, delay):
    with tqdm(total=steps, desc=name, position=int(name[-1])-1, leave=False) as pbar:
        for _ in range(steps):
            await asyncio.sleep(delay)
            pbar.update(1)

async def run_tasks(delays, steps_per_task):
    task_1 = run_task('Task 1', steps_per_task, delays[0])
    task_2 = run_task('Task 2', steps_per_task, delays[1])
    task_3 = run_task('Task 3', steps_per_task, delays[2])
    await asyncio.gather(task_1, task_2, task_3)

def run_async_pipeline(shared_delays, steps_per_task):
    print('\n=== Asynchronous Execution ===')
    print(f'Delays: {shared_delays[0]}, \
                    {shared_delays[1]}, \
                    {shared_delays[2]},')
    start = time.time()
    asyncio.run(run_tasks(shared_delays, steps_per_task))
    end = time.time()
    print(f'\n\n\nAsync executed in {end - start:.2f} seconds')