import threading
import time  


class ThreadLifecycle:
   
    @staticmethod
    def worker_thread(name):
       
        print(f"Thread {name}: Running")

        
        print(f"Thread {name}: Sleeping")
        time.sleep(2)

    
        print(f"Thread {name}: Done")


    @staticmethod
    def demonstrate():
       
        print("1. NEW: Creating thread object")
        thread = threading.Thread(
            target=ThreadLifecycle.worker_thread,
            args=("Worker-1",)
        )


        
        print("2. READY: Starting thread")
        thread.start()


        
        print("3. RUNNING: Thread is executing")


    
        print("4. BLOCKED: Thread may be sleeping or waiting")
        time.sleep(1)  # Main thread sleeps briefly


        
        print("5. Check if thread is alive")
        print(f"Thread is alive: {thread.is_alive()}")


        
        print("6. TERMINATED: Wait for thread to finish")
        thread.join()
        print(f"Thread is alive: {thread.is_alive()}")


ThreadLifecycle.demonstrate()