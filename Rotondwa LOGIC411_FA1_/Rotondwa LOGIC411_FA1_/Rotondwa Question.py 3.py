#Question 3

import time 
import random

def typing_speed_test():
   print("Try Again!")

print("\nWelcome to the Typing Speed Test!")
input("\nPress Enter when you are ready to start...")

sentences = ["It is with great pleasure to welcome you. ", "The future is bright for those who do not fear change. ",
             "I can do all things through Christ who strenghtens me. ",
               "The ladies were out in numbers, praising and worshiping. ", "The Gentle men were out working hard to provide"]

sentence = ''.join(random.sample(sentences,2))

print(f"\nType the following sentence as fast as you can:\n{sentence}\n")

start_time = time.time()

user_input = input("Type Here: ")

end_time = time.time()

time_taken = end_time-start_time

words_typed = len(user_input.split())
expected_words = sentence.split()
words_per_minute = (words_typed/time_taken) * 60

errors = sum(1 for w1, w2 in zip(expected_words, user_input) 
             if w1 != w2)

print("\nNumber of words typed:{}".format(words_typed))
print("Time Taken: {:.2f} seconds".format(time_taken))
print("Typing speed: {:.2f} words/minute".format(words_per_minute))

if __name__ == "__main__":
    typing_speed_test()
