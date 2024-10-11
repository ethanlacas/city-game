import tkinter as tk
from tkinter import messagebox
import random
import pickle  # For saving/loading game state

# Constants
CITY_WIDTH = 10
CITY_HEIGHT = 10
INITIAL_MONEY = 1000
INITIAL_POWER = 100
INITIAL_WATER = 100
INITIAL_FOOD = 100

# Class to manage city generation and layout
class ProceduralCity:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.city_layout = [[0] * width for _ in range(height)]  # 0: empty, 1: residential, 2: commercial, 3: industrial
        self.buildings = []  # Track buildings added to the city

    def generate_random_city(self):
        # Generate a random city layout for demonstration
        for i in range(self.height):
            for j in range(self.width):
                self.city_layout[i][j] = random.choice([0, 1, 2, 3])  # Randomly assign zones
        print("City layout generated.")

    def display_city(self):
        # Print the city layout to the console
        for row in self.city_layout:
            print(" ".join(str(cell) for cell in row))

    def reset_city(self):
        self.city_layout = [[0] * self.width for _ in range(self.height)]
        print("City reset to initial state.")

    def add_building(self, x, y, building_type):
        # Add a building to the city
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.city_layout[y][x] == 0:  # Check if the space is empty
                self.city_layout[y][x] = building_type
                self.buildings.append((x, y, building_type))
                print(f"Building added at ({x}, {y}): Type {building_type}")
            else:
                print("Space is already occupied.")
        else:
            print("Invalid coordinates.")

# Class to manage resources in the game
class AdvancedResourceManager:
    def __init__(self):
        self.resources = {
            'money': INITIAL_MONEY,
            'power': INITIAL_POWER,
            'water': INITIAL_WATER,
            'food': INITIAL_FOOD,
        }
        self.resource_capacity = {
            'money': 5000,
            'power': 500,
            'water': 500,
            'food': 500,
        }

    def collect_resources(self):
        # Simulate resource collection
        self.resources['money'] += random.randint(50, 150)
        self.resources['power'] += random.randint(5, 15)
        self.resources['water'] += random.randint(10, 30)
        self.resources['food'] += random.randint(15, 25)
        print("Resources collected.")

    def check_resources(self):
        # Check resource levels
        for resource, amount in self.resources.items():
            if amount < 0:
                print(f"Warning: {resource} is running low!")

    def print_resources(self):
        print("Current Resources:")
        for resource, amount in self.resources.items():
            print(f"{resource.capitalize()}: {amount}")

# Class to manage the economy of the city
class EconomyManager:
    def __init__(self):
        self.income = 100
        self.expenses = 50
        self.total_income = 0
        self.total_expenses = 0

    def calculate_income(self):
        # Simulate income calculation
        self.total_income += self.income
        print(f"Total income updated: {self.total_income}")

    def calculate_expenses(self):
        # Simulate expense calculation
        self.total_expenses += self.expenses
        print(f"Total expenses updated: {self.total_expenses}")

    def balance_budget(self):
        balance = self.total_income - self.total_expenses
        print(f"Budget balance: {balance}")
        return balance

# Class to manage happiness in the city
class HappinessManager:
    def __init__(self):
        self.happiness = 100
        self.happiness_events = []

    def increase_happiness(self, amount):
        self.happiness += amount
        print(f"Happiness increased by {amount}. Current happiness: {self.happiness}")

    def decrease_happiness(self, amount):
        self.happiness -= amount
        print(f"Happiness decreased by {amount}. Current happiness: {self.happiness}")

    def check_happiness(self):
        if self.happiness < 50:
            print("Warning: Happiness is low!")

    def print_happiness(self):
        print(f"Current Happiness Level: {self.happiness}")

# Class to manage crisis events
class CrisisEvent:
    def __init__(self):
        self.events = ["Natural Disaster", "Economic Downturn", "Public Protest"]
        self.current_event = None

    def trigger_event(self):
        self.current_event = random.choice(self.events)
        print(f"Crisis event triggered: {self.current_event}")

    def resolve_event(self):
        print(f"Crisis event resolved: {self.current_event}")
        self.current_event = None

# Class for city customization options
class CityCustomization:
    def __init__(self):
        self.customizations = {
            'parks': 0,
            'public_transport': 0,
            'education': 0,
        }

    def add_park(self):
        self.customizations['parks'] += 1
        print(f"Park added. Total parks: {self.customizations['parks']}")

    def improve_transport(self):
        self.customizations['public_transport'] += 1
        print(f"Public transport improved. Total improvements: {self.customizations['public_transport']}")

    def enhance_education(self):
        self.customizations['education'] += 1
        print(f"Education enhanced. Total enhancements: {self.customizations['education']}")

# Class for managing city transportation
class TransportationManager:
    def __init__(self):
        self.routes = []

    def add_route(self, route_name):
        self.routes.append(route_name)
        print(f"Route added: {route_name}")

    def remove_route(self, route_name):
        if route_name in self.routes:
            self.routes.remove(route_name)
            print(f"Route removed: {route_name}")

    def print_routes(self):
        print("Current Routes:")
        for route in self.routes:
            print(f"- {route}")

# Main game class to orchestrate the game mechanics
class CityGame:
    def __init__(self):
        self.city = None
        self.resources = None
        self.economy = None
        self.happiness = None
        self.crisis_event = None
        self.customization = None
        self.transportation_manager = None
        self.game_data_file = "game_data.pkl"

    def start_new_game(self):
        # Initialize all game components for a new game
        self.city = ProceduralCity(CITY_WIDTH, CITY_HEIGHT)
        self.city.generate_random_city()
        self.resources = AdvancedResourceManager()
        self.economy = EconomyManager()
        self.happiness = HappinessManager()
        self.crisis_event = CrisisEvent()
        self.customization = CityCustomization()
        self.transportation_manager = TransportationManager()
        self.display_status("New game started!")

    def load_game(self):
        try:
            with open(self.game_data_file, 'rb') as f:
                game_data = pickle.load(f)
                self.city = game_data['city']
                self.resources = game_data['resources']
                self.economy = game_data['economy']
                self.happiness = game_data['happiness']
                self.crisis_event = game_data['crisis_event']
                self.customization = game_data['customization']
                self.transportation_manager = game_data['transportation_manager']
                self.display_status("Game loaded successfully!")
        except (FileNotFoundError, EOFError):
            self.display_status("No saved game found!")

    def save_game(self):
        game_data = {
            'city': self.city,
            'resources': self.resources,
            'economy': self.economy,
            'happiness': self.happiness,
            'crisis_event': self.crisis_event,
            'customization': self.customization,
            'transportation_manager': self.transportation_manager,
        }
        with open(self.game_data_file, 'wb') as f:
            pickle.dump(game_data, f)
        self.display_status("Game saved successfully!")

    def display_status(self, message):
        print(message)  # For console output

# Class to handle the user interface
class CityGameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("City Simulation Game")
        self.game = CityGame()
        self.bg_color = "#2196F3"
        self.master.configure(bg=self.bg_color)

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.master, text="City Simulation Game", font=("Arial", 24), bg=self.bg_color, fg="white")
        self.title_label.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(self.master, text="", font=("Arial", 14), bg=self.bg_color, fg="white")
        self.status_label.pack(pady=10)

        # New Game Button
        self.new_game_button = tk.Button(self.master, text="Start New Game", command=self.start_new_game, bg="#4CAF50", fg="white")
        self.new_game_button.pack(pady=10)

        # Load Game Button
        self.load_game_button = tk.Button(self.master, text="Load Game", command=self.load_game, bg="#4CAF50", fg="white")
        self.load_game_button.pack(pady=10)

        # Save Game Button
        self.save_game_button = tk.Button(self.master, text="Save Game", command=self.save_game, bg="#4CAF50", fg="white")
        self.save_game_button.pack(pady=10)

        # Action Entry
        self.action_entry = tk.Entry(self.master, width=30, font=("Arial", 14))
        self.action_entry.pack(pady=10)

        # Action Button
        self.action_button = tk.Button(self.master, text="Execute Action", command=self.handle_action, bg="#2196F3", fg="white")
        self.action_button.pack(pady=10)

        # Additional Game Actions
        self.extra_actions_frame = tk.Frame(self.master, bg=self.bg_color)
        self.extra_actions_frame.pack(pady=10)

        self.add_park_button = tk.Button(self.extra_actions_frame, text="Add Park", command=self.add_park, bg="#4CAF50", fg="white")
        self.add_park_button.grid(row=0, column=0)

        self.improve_transport_button = tk.Button(self.extra_actions_frame, text="Improve Transport", command=self.improve_transport, bg="#4CAF50", fg="white")
        self.improve_transport_button.grid(row=0, column=1)

        self.enhance_education_button = tk.Button(self.extra_actions_frame, text="Enhance Education", command=self.enhance_education, bg="#4CAF50", fg="white")
        self.enhance_education_button.grid(row=0, column=2)

        self.view_resources_button = tk.Button(self.extra_actions_frame, text="View Resources", command=self.view_resources, bg="#4CAF50", fg="white")
        self.view_resources_button.grid(row=1, column=0)

        self.view_happiness_button = tk.Button(self.extra_actions_frame, text="View Happiness", command=self.view_happiness, bg="#4CAF50", fg="white")
        self.view_happiness_button.grid(row=1, column=1)

        self.trigger_crisis_button = tk.Button(self.extra_actions_frame, text="Trigger Crisis", command=self.trigger_crisis, bg="#FF5722", fg="white")
        self.trigger_crisis_button.grid(row=1, column=2)

    def start_new_game(self):
        self.game.start_new_game()
        self.update_status("Game has started. You can begin taking actions.")

    def load_game(self):
        self.game.load_game()
        self.update_status("Game loaded. You can resume playing.")

    def save_game(self):
        self.game.save_game()
        self.update_status("Game saved.")

    def handle_action(self):
        action = self.action_entry.get()
        self.action_entry.delete(0, tk.END)  # Clear input after submission
        self.process_action(action)

    def process_action(self, action):
        # Example processing logic
        responses = {
            'p': "You placed a new tile.",
            'z': "You zoned a new area.",
            's': "You specialized your city.",
            'r': "You conducted research.",
            'c': "You customized your city.",
            'q': "Quitting the game. Goodbye!"
        }

        response = responses.get(action.lower(), "Invalid action. Try again.")
        self.update_status(response)

    def add_park(self):
        self.game.customization.add_park()
        self.update_status("Park added to the city.")

    def improve_transport(self):
        self.game.customization.improve_transport()
        self.update_status("Public transport improved.")

    def enhance_education(self):
        self.game.customization.enhance_education()
        self.update_status("Education enhanced.")

    def view_resources(self):
        self.game.resources.print_resources()

    def view_happiness(self):
        self.game.happiness.print_happiness()

    def trigger_crisis(self):
        self.game.crisis_event.trigger_event()
        self.update_status("Crisis event triggered!")

    def update_status(self, message):
        self.status_label.config(text=message)
        print(message)  # Output to console for debugging

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    game_ui = CityGameUI(root)
    root.mainloop()
