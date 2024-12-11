import whisper
import os

# Settings
language = 'fr'


def main():
    # transcribe every file in input directory
    for filename in os.listdir('input'):
        # allowed formats are mp3 and wav
        if filename.split('.')[-1] not in ['mp3', 'wav']:
            continue

        # audio/transcription title
        title = os.path.basename(filename).split('.')[0]

        # create model and transcribe file with it
        model = whisper.load_model('tiny')
        trans_result = model.transcribe(f'input/{filename}', language=language)
        transcription_txt = trans_result['text']

        # save transcription
        with open(f'output/{title}.txt', 'w') as f:
            f.write(transcription_txt)


if __name__=="__main__":
    main()