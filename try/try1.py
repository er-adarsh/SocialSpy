import tkinter as tk
import threading
import queue

def background_task(q):
    # Perform a background task
    result = "some result"
    q.put(result)  # Put result in queue for main thread to process

def process_queue():
    try:
        result = q.get_nowait()  # Check for result without blocking
        label.config(text=result)
    except queue.Empty:
        pass
    root.after(100, process_queue)  # Check again after 100 ms

root = tk.Tk()
label = tk.Label(root, text="Waiting for result...")
label.pack()

# Set up a queue for thread-safe communication
q = queue.Queue()

# Start background thread
threading.Thread(target=background_task, args=(q,), daemon=True).start()

# Start queue processing loop
root.after(100, process_queue)

root.mainloop()