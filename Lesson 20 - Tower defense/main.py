import pygame
import configparser
from button import Button
from enemy import Enemy
from tower import Tower
from message_box import MessageBox
from constants import (
    WIDTH, HEIGHT, GRID, CELL_SIZE, WHITE, BLACK, GRAY, BROWN, DARK_GREEN, DARK_RED)


def get_tower(grid_x, grid_y, type_towers, index):
    return Tower(
        x=grid_x * CELL_SIZE,
        y=grid_y * CELL_SIZE,
        level=type_towers[index][0],
        damage=type_towers[index][1],
        fire_range=type_towers[index][2],
        fire_rate=type_towers[index][3],
        cost=type_towers[index][4],
        upgrade_cost=type_towers[index][5],
        image_path=type_towers[index][6],
    )

def draw_tower_stats(surface, selected_tower, level, damage, fire_range, fire_rate, cost, upgrade_cost, max_tower_level):
    font = pygame.font.SysFont('Arial', 20)
    stats_text = [
        f'Damge: {damage}',
        f"Range: {fire_range}",
        f"Fire rate: {fire_rate}",
        f'Level: {level}',
        f'Sell cost: {round(int(cost) * 0.9)}' if isinstance(selected_tower, Tower) else f'Cost: {cost}',
        f'Upgrade cost: {int(upgrade_cost)}' if int(level) < max_tower_level else '',
    ]
    for i, line in enumerate(stats_text):
        text = font.render(line, True, BLACK)
        surface.blit(text, (WIDTH - 350, 460 + i * 20))

def draw_grid_elements(screen, towers, enemies, projectiles):
    screen.fill(WHITE)
    for y, row in enumerate(GRID):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell in [0, 4]:
                pygame.draw.rect(screen, DARK_GREEN, rect)
            elif cell in [1, 2, 3]:
                pygame.draw.rect(screen, BROWN, rect)
    for x in range(len(GRID[0]) + 1):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, len(GRID) * CELL_SIZE), 1)
    for y in range(len(GRID) + 1):
        pygame.draw.line(screen, BLACK, (0, y * CELL_SIZE), (len(GRID[0]) * CELL_SIZE, y * CELL_SIZE), 1)
    towers.draw(screen)
    enemies.draw(screen)
    projectiles.draw(screen)
    for enemy in enemies:
        enemy.draw_health_bar(screen)

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    result = []
    for section in config.sections():
        section_values = []
        for key, value in config.items(section):
            try:
                section_values.append(int(value))
            except ValueError:
                section_values.append(value)
        result.append(section_values)
    return result

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)

    towers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    
    game_running = True
    level_running = False
    selected_tower = None
    current_level = 1

    # Enemies
    total_enemies_spawned = 0
    spawn_counter = 0

    # Game
    score = 0
    lives = 20
    money = 300

    # Towers
    type_towers = read_config_file('towers.ini')
    levels = read_config_file('levels.ini')
    max_tower_level = 5

    # Create the buttons with the images
    button_tower1 = Button(WIDTH * 0.06, HEIGHT * 0.75, 32, 32, '', '', '', image_path="./images/tower1.png")
    button_tower2 = Button(WIDTH * 0.12, HEIGHT * 0.75, 32, 32, '', '', '', image_path="./images/tower2.png")
    button_tower3 = Button(WIDTH * 0.18, HEIGHT * 0.75, 32, 32, '', '', '', image_path="./images/tower3.png")

    # Buttons
    button_start = Button(WIDTH * 0.05, HEIGHT * 0.85, 190, 50, BROWN, "Start Level 1", WHITE, '')
    button_sell = Button(WIDTH - 180, HEIGHT * 0.73, 170, 40, DARK_RED, "Sell Tower", WHITE, '')
    button_upgrade = Button(WIDTH - 180, HEIGHT * 0.8, 170, 40, DARK_GREEN, "Upgrade", WHITE, '')

    # Main Loop
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running == False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.is_clicked(event) and not level_running:
                    level_running = True
                    total_enemies_spawned = 0
                    enemies.empty()
                    spawn_fire_rate, enemy_healt, speed, value, enemy_image, num_enemies = levels[current_level-1]
                elif button_tower1.is_clicked(event):
                    selected_tower = 'Tower 1'
                elif button_tower2.is_clicked(event):
                    selected_tower = 'Tower 2'
                elif button_tower3.is_clicked(event):
                    selected_tower = 'Tower 3'
                elif button_sell.is_clicked(event) and selected_tower and isinstance(selected_tower, Tower):
                    money += int(round(selected_tower.cost * 0.9))
                    GRID[selected_tower.rect.y // CELL_SIZE][selected_tower.rect.x // CELL_SIZE] = 0
                    towers.remove(selected_tower)
                    selected_tower = None
                elif button_upgrade.is_clicked(event) and selected_tower and isinstance(selected_tower, Tower):
                    if money >= selected_tower.upgrade_cost and selected_tower.level < max_tower_level:
                        money -= selected_tower.upgrade_cost
                        selected_tower.level += 1
                        selected_tower.damage = int(round(selected_tower.damage * (100 + selected_tower.level * 3) / 100))
                        selected_tower.fire_range = int(round(selected_tower.fire_range * (100 + selected_tower.level * 3) / 100))
                        selected_tower.fire_rate = int(round(selected_tower.fire_rate * (100 + selected_tower.level * 3) / 100))
                        selected_tower.upgrade_cost = int(round(selected_tower.upgrade_cost * (100 + selected_tower.level * 3) / 100))
                        selected_tower.cost = int(round(selected_tower.cost * (100 + selected_tower.level * 3) / 100))
                elif event.button == 1:
                    pass

        if level_running:
            for tower in towers:
                projectile = tower.update(enemies)
                if projectile:
                    projectiles.add(projectile)
            for enemy in enemies:
                if enemy.progress_path(enemy.find_path(GRID)):
                    lives -= 1
                    enemy.kill()
                if enemy.health <= 0:
                    enemy.kill()
                    score += 10
                    money += value
            projectiles.update()
            if total_enemies_spawned < num_enemies:
                spawn_counter += 1
                if spawn_counter >= spawn_fire_rate:
                    spawn_counter = 0
                    enemies.add(Enemy(enemy_healt, speed, value, enemy_image))
                    total_enemies_spawned += 1
        

            
    pygame.quit()

if __name__ == '__main__':
    main()
