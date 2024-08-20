import subprocess
import threading
import signal
import os


def start_recording(output_file):
    # Define the output file and duration
    duration = 1  # Duration in seconds

    # Define the monitor source name (replace with your specific monitor name)
    monitor_source = "auto_null.monitor"  # Example monitor source name

    # Create the ffmpeg command
    command = [
        "ffmpeg",
        "-f", "pulse",
        "-i", monitor_source,
        "-t", str(duration),
        output_file
    ]

    # Run the command
    print("Recording started...")
    subprocess.run(command)
    print("Recording finished.")




