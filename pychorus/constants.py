# Denoising size in seconds
SMOOTHING_SIZE_SEC = 5.0

# Number of samples to consider in one chunk.
# Smaller values take more time, but are more accurate
N_FFT = 2**13

# For line detection
LINE_THRESHOLD = 0.08
MIN_LINES = 6
NUM_ITERATIONS = 6

# We allow an error proportional to the length of the clip
OVERLAP_PERCENT_MARGIN = 0.2
