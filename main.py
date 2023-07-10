from wonderwords import RandomSentence
import random
import time
import tkinter
import ttkthemes
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title('Type Speed Test')

window.geometry('700x700')

window.option_add("*Label.Font", "consolas 30")
window.option_add("*Button.Font", "consolas 30")

sent_list = []
sent_paragraph = ""

for i in range(5):
    sent = RandomSentence()
    random_sent = sent.sentence()
    sent_list.append(random_sent)
    sent_paragraph += random_sent + " "

def error_rate(sent_paragraph, typed_paragraph):
    error_count = 0
    length = len(sent_paragraph)

    for i, char in enumerate(sent_paragraph):
        try:
            if char != typed_paragraph[i]:
                error_count += 1
        except:
            error_count += 1

    error_percent = error_count / length * 100
    return error_percent

def main():
    print("Type the below paragraph as quickly as possible with as few mistakes to get a high score: \n")
    print(sent_paragraph)
    print("\n")

    start_time = time.time()
    typed_paragraph = input()
    end_time = time.time()

    time_taken = end_time - start_time

    error_percent = error_rate(sent_paragraph, typed_paragraph)
    print("\n")

    if error_percent >= 50:
        print(f"Your error rate {error_percent} was quite high and hence your accurate speed could not be computed.")
    else:
        speed = len(typed_paragraph) / time_taken
        print("***** YOUR SCORE REPORT *****")
        print(f"Your speed is {speed} words/sec")
        print(f"The error rate is {error_percent}")

if __name__ == '__main__':
    main()
