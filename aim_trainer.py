import math
import random
import time
import pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer 🎯")

# Colors
BG_COLOR = (0, 25, 40)
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game constants
TARGET_PADDING = 30
TOP_BAR_HEIGHT = 50
LIVES = 3
LABEL_FONT = pygame.font.SysFont("comicsans", 28)

# Load sounds safely
try:
    HIT_SOUND = pygame.mixer.Sound("hit.wav")
    MISS_SOUND = pygame.mixer.Sound("miss.wav")
except:
    HIT_SOUND = None
    MISS_SOUND = None


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = RED
    SECOND_COLOR = WHITE

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        self.size += self.GROWTH_RATE if self.grow else -self.GROWTH_RATE

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        return math.hypot(x - self.x, y - self.y) <= self.size


def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)
    return f"{minutes:02d}:{seconds:02d}.{milli}"


def draw_top_bar(win, elapsed_time, hits, misses):
    pygame.draw.rect(win, GREY, (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", True, "black")
    speed = round(hits / elapsed_time, 1) if elapsed_time > 0 else 0
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", True, "black")
    hits_label = LABEL_FONT.render(f"Hits: {hits}", True, "black")
    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", True, "black")

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (220, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))


def get_middle(surface):
    return WIDTH / 2 - surface.get_width() / 2


def start_menu():
    run = True
    while run:
        WIN.fill(BG_COLOR)
        title = LABEL_FONT.render("🎯 Aim Trainer", True, WHITE)
        start = LABEL_FONT.render("Press [SPACE] to Start", True, WHITE)
        quit_label = LABEL_FONT.render("Press [Q] to Quit", True, WHITE)

        WIN.blit(title, (get_middle(title), 200))
        WIN.blit(start, (get_middle(start), 300))
        WIN.blit(quit_label, (get_middle(quit_label), 400))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_q:
                    return False


def end_screen(win, elapsed_time, hits, clicks):
    run = True
    accuracy = round((hits / clicks) * 100, 1) if clicks > 0 else 0

    while run:
        win.fill(BG_COLOR)
        labels = [
            f"Time: {format_time(elapsed_time)}",
            f"Speed: {round(hits / elapsed_time, 1) if elapsed_time > 0 else 0} t/s",
            f"Hits: {hits}",
            f"Accuracy: {accuracy}%",
            "Press [R] to Restart or [Q] to Quit"
        ]

        for i, text in enumerate(labels):
            label = LABEL_FONT.render(text, True, WHITE)
            win.blit(label, (get_middle(label), 150 + i * 60))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False


def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    hits, clicks, misses = 0, 0, 0
    start_time = time.time()
    target_timer = 1000  # ms between spawns
    pygame.time.set_timer(pygame.USEREVENT, target_timer)

    while run:
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.USEREVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                targets.append(Target(x, y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets[:]:
            target.update()
            if target.size <= 0:
                targets.remove(target)
                misses += 1
                if MISS_SOUND:
                    MISS_SOUND.play()
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                hits += 1
                if HIT_SOUND:
                    HIT_SOUND.play()

        if misses >= LIVES:
            return end_screen(WIN, elapsed_time, hits, clicks)

        WIN.fill(BG_COLOR)
        for t in targets:
            t.draw(WIN)
        draw_top_bar(WIN, elapsed_time, hits, misses)
        pygame.display.update()


if __name__ == "__main__":
    while True:
        if not start_menu():
            break
        if not main():
            break
