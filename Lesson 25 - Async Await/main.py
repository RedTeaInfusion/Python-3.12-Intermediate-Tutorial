'''
Lesson 25 - Async Await
async
await
tqdm
asyncio
'''
import random
import synchronous
import asynchronous

NUM_TASKS = 3
STEPS_PER_TASK = 50

def generate_delays():
    return [random.randint(1, 100) / 1000 for _ in range(NUM_TASKS)]

def main():
    shared_delays = generate_delays()
    synchronous.run_sync_pipeline(shared_delays, STEPS_PER_TASK)
    asynchronous.run_async_pipeline(shared_delays, STEPS_PER_TASK)

if __name__ == '__main__':
    main()