import sys
from datetime import timedelta
from pydub import AudioSegment
import questionary

def loop_audio(audio_file, file_name, number_of_hours):
    if number_of_hours > 5:
        print("The limit for looping is 5 hours")
        return

    target_time = timedelta(hours=number_of_hours)

    final_audio = AudioSegment.empty()

    while timedelta(seconds=final_audio.duration_seconds) < target_time:
        final_audio += audio_file

    file_type = get_file_type()

    export_format = ""
    if file_type == "m4a":
        export_format = "ipod"
    else:
        export_format = file_type

    final_audio.export(
        file_name + f"_looped_{number_of_hours}h." + str(file_type),
        format=export_format
    )

def get_file_name(file_path):
    file_length = len(file_path)
    file_name = ""

    for i in range(1, file_length + 1):
        if file_path[-i] == "/":
            break
        else:
            file_name += file_path[-i]

    return (file_name[::-1])[:-4]

def get_file_path():
    file = questionary.path(
        "What audio file would you like to loop?"
    ).ask()

    if file.lower().endswith(".mp3") or file.lower().endswith(".wav") or file.lower().endswith(".m4a"):
        return file
    else:
        print("File type not supported.")
        sys.exit()

def get_number_of_hours():
    number_of_hours = questionary.select(
        "How many hours do you want to loop for?",
        choices=["1", "2", "3", "4", "5"]
    ).ask()

    return number_of_hours

def get_file_type():
    choice = questionary.select(
        "What file type would you like to save your audio as?",
        choices=["wav", "mp3", "m4a"]
    ).ask()

    return choice

def main():
    # Getting the audio file
    file = get_file_path()
    file_name = get_file_name(file)
    user_audio = AudioSegment.from_file(file, format=file[-3:].lower())

    # Getting the number of hours to loop
    loop_duration = int(get_number_of_hours())
    print("Looping audio...")

    # Looping audio
    loop_audio(user_audio, file_name, loop_duration)

if __name__ == "__main__":
    main()