import re
import string
import json


def clean_transcript(transcript):
    """
    Cleans a given transcript for easy searching in the 20k most common words in the Google Trillion Words Corpus
    ...

    Parameters
    ----------
    transcript : str
        The transcript to be cleaned

    Output : str
        The cleaned transcript
    """
    transcript = re.sub("[\(\[].*?[\)\]]", "", transcript)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    no_punc = transcript.translate(table)
    return no_punc.lower()


def PD_bag_of_words(transcripts):
    """
    Processes a list of transcripts and returns a list of
    corresponding pronunciation difficulties (PD) according to
    a simple bag of words
    ...

    Parameters
    ----------
    transcripts : [str]
        List of transcripts passed as strings

    Output : [float]
        List of difficulties for corresponding transcripts passed as floats
    """

    # build dict from 20k.txt
    f = open("20k.txt", "r")
    word_dict = {}
    for i in range(20000):
        line = f.readline().strip()
        word_dict[line] = i
    f.close()

    out = []
    for x in transcripts:
        x = clean_transcript(x)
        split_x = x.split()
        PD = 0
        for word in split_x:
            if word_dict.get(word, -1) == -1:
                PD += 1
        out.append(PD)
    return out


if __name__ == "__main__":
    with open("sample_transcripts.txt", "r") as transcripts:
        lines = transcripts.read().split('\n')
        difficulties = PD_bag_of_words(lines)
        matched = list(zip(difficulties, lines))
        matched.sort()
        for x in matched:
            print(x)
        # for x in lines:
        #     print(clean_transcript(x))
