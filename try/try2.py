import threading

def task():
    print("Thread is running...")
    for i in range(5):
        print(f"Task step {i}")
        
# Create a thread
thread = threading.Thread(target=task)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread has finished.")