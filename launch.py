from modules import launch_utils
import torch
import torch_directml
import sys
import argparse

# Function to parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Launch Web UI with DirectML support.")
    # Add argument to choose DirectML
    parser.add_argument("--use-directml", action="store_true", help="Use DirectML instead of CUDA/CPU")
    # Add other arguments as needed (for example, skipping torch CUDA test)
    parser.add_argument("--skip-torch-cuda-test", action="store_true", help="Skip the torch CUDA test")
    parser.add_argument("--no-half", action="store_true", help="Disable half precision")
    # Add any other arguments that are already part of your web UI setup
    return parser.parse_args()

# Function to handle device selection
def get_device(args):
    if args.use_directml:
        print("Using DirectML device")
        return torch_directml.device()  # Use DirectML device
    # Fallback to default CUDA or CPU
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Main function
def main():
    # Parse command line arguments
    args = parse_args()

    # Remove the check for args.test_server, since it's not defined
    # if args.test_server:
    #     launch_utils.configure_for_tests()

    # Record the initial startup time
    launch_utils.startup_timer.record("initial startup")

    # Prepare environment
    with launch_utils.startup_timer.subcategory("prepare environment"):
        launch_utils.prepare_environment()

    # Get the selected device (DirectML, CUDA, or CPU)
    device = get_device(args)
    print(f"Using device: {device}")

    # Call start() to launch the Web UI
    launch_utils.start()

if __name__ == "__main__":
    main()
