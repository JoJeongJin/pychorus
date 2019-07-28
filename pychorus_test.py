from os import listdir
from os.path import isfile, join
from pychorus import find_and_output_chorus
from pychorus import create_chroma
from pychorus.similarity_matrix import TimeTimeSimilarityMatrix, TimeLagSimilarityMatrix

music_file_path = "./music/"

files = [f for f in listdir(music_file_path) if isfile(join(music_file_path, f)) ]

for file_name in files:
    print(file_name)
    name = file_name.split(".")[0]
    chorus_start_sec = find_and_output_chorus(music_file_path+name+".mp3", "./output/"+ name+".wav" , 10)

    chroma, _, sr, _ = create_chroma(music_file_path+name+".mp3")
    # time_time_similarity = TimeTimeSimilarityMatrix(chroma, sr)
    time_lag_similarity = TimeLagSimilarityMatrix(chroma, sr)

    # # Visualize the results
    # time_time_similarity.display()
    time_lag_similarity.display()
