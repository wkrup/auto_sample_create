import subprocess
import threading
import signal
import os


def start_recording(output_file="output.wav"):
    monitor_source = "auto_null.monitor"  # Replace with your monitor source name
    command = [
        "ffmpeg",
        "-f", "pulse",
        "-i", monitor_source,
        output_file
    ]

def stop_recording(process):
    # Send a SIGINT signal to gracefully stop ffmpeg
    process.send_signal(signal.SIGINT)
    process.wait()  # Wait for the process to terminate
    print("Recording stopped.")




