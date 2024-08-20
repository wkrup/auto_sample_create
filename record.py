import subprocess
import threading
import signal
import os

def start_recording(output_file):
    monitor_source = "alsa_output.pci-0000_00_1b.0.analog-stereo.monitor"  # Replace with your monitor source name
    command = [
        "ffmpeg",
        "-f", "pulse",
        "-i", monitor_source,
        output_file
    ]


    # Start recording
    process = subprocess.Popen(command)
    return process

def stop_recording(process):
    # Send a SIGINT signal to gracefully stop ffmpeg
    process.send_signal(signal.SIGINT)
    process.wait()  # Wait for the process to terminate
    print("Recording stopped.")



