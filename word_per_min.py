import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("🚀 Welcome to the Speed Typing Test!\n")
    stdscr.addstr("Type the given paragraph as fast and accurately as you can.\n")
    stdscr.addstr("You must complete at least 50 words.\n")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0, accuracy=0, elapsed=0, words_typed=0):
    stdscr.addstr(0, 0, target, curses.color_pair(3))
    stdscr.addstr(3, 0, f"WPM: {wpm} | Accuracy: {accuracy:.2f}% | Time: {int(elapsed)}s | Words Typed: {words_typed}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def load_paragraph():
    paragraphs = [
        "Python is a versatile and powerful programming language that has become one of the most popular choices for developers worldwide. It is known for its simplicity, readability, and vast ecosystem of libraries. Whether you are building web applications, working with data science, or exploring artificial intelligence, Python provides tools and frameworks to make development easier and faster.",
        
        "The importance of consistent practice cannot be overstated when it comes to learning new skills. Typing is no different. By practicing every day, you not only improve your speed but also increase your accuracy and confidence. Many professional programmers and writers recommend setting aside dedicated time daily to focus solely on typing and writing exercises.",
        
        "Technology is evolving at an incredible pace, shaping the way we live, work, and interact with one another. Artificial intelligence, blockchain, and cloud computing are no longer futuristic concepts; they are part of our everyday lives. To stay relevant in today’s fast-changing world, continuous learning and skill development have become more important than ever."
    ]
    return random.choice(paragraphs)


def wpm_test(stdscr):
    target_text = load_paragraph()
    current_text = []
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        elapsed_time = max(time.time() - start_time, 1)
        words_typed = len("".join(current_text).split())
        wpm = round((words_typed / (elapsed_time / 60)))

        correct_chars = sum(1 for i, c in enumerate(current_text) if i < len(target_text) and c == target_text[i])
        accuracy = (correct_chars / len(current_text) * 100) if current_text else 0

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, accuracy, elapsed_time, words_typed)
        stdscr.refresh()

        if "".join(current_text) == target_text and words_typed >= 50:
            stdscr.nodelay(False)
            return wpm, accuracy, int(elapsed_time)

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC to quit
            return None, None, None

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # correct
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # incorrect
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # default

    start_screen(stdscr)

    while True:
        wpm, accuracy, elapsed = wpm_test(stdscr)

        if wpm is None:
            break  # quit with ESC

        stdscr.clear()
        stdscr.addstr("✅ Test Completed!\n\n")
        stdscr.addstr(f"Final WPM: {wpm}\n")
        stdscr.addstr(f"Accuracy: {accuracy:.2f}%\n")
        stdscr.addstr(f"Time Taken: {elapsed} seconds\n")
        stdscr.addstr("\n(You typed at least 50 words!)\n")
        stdscr.addstr("\nPress any key to try again or ESC to quit...")
        stdscr.refresh()

        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)
