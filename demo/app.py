# DevCore Learning Log - Showcase Program
# Highlights concepts from the DevCore School Python for Beginners Course

import datetime # Module 6: For using dates and times
import json     # Module 6: For saving and loading data in a structured way (like dictionaries and lists)
import os       # Module 6: For checking if a file exists

LOG_FILE = "devcore_learning_log.json"

# --- Functions (Module 5: Functions) ---

def display_welcome():
    """Displays a welcome message.""" # Docstrings are good practice (Module 8 hint)
    print("=" * 40)
    print("🎉 Welcome to DevCore Learning Log! 🎉") # Module 1 & 2: print(), Strings
    print("=" * 40)
    print("Showcasing what you'll learn at DevCore School!")
    print("-" * 40)

def display_menu():
    """Displays the main menu options."""
    print("\nChoose an action:")
    print("1. Add New Learning Entry")
    print("2. View All Entries")
    print("3. Save Log")
    print("4. Load Log (Automatic on start)")
    print("5. Exit")

def load_log_from_file():
    """Loads learning entries from a JSON file."""
    # Module 7: File Handling & Module 6: Error Handling
    if not os.path.exists(LOG_FILE): # Check if file exists
        return [] # Return an empty list if no file

    try:
        with open(LOG_FILE, 'r') as f: # 'r' for read
            entries = json.load(f) # Converts JSON data from file to Python list of dictionaries
            print("\n✅ Log loaded successfully!")
            return entries
    except FileNotFoundError:
        print(f"\nℹ️ No existing log file ('{LOG_FILE}') found. Starting fresh.")
        return [] # Module 4: Lists
    except json.JSONDecodeError:
        print(f"\n⚠️ Error decoding '{LOG_FILE}'. File might be corrupted. Starting fresh.")
        return []
    except Exception as e: # Catch other potential errors
        print(f"\n⚠️ An unexpected error occurred while loading: {e}")
        return []

def save_log_to_file(entries):
    """Saves learning entries to a JSON file."""
    # Module 7: File Handling
    try:
        with open(LOG_FILE, 'w') as f: # 'w' for write (overwrites existing file)
            json.dump(entries, f, indent=4) # Saves Python list of dicts to file as JSON, indent for readability
        print(f"\n✅ Log saved successfully to '{LOG_FILE}'!")
    except Exception as e: # Module 6: Error Handling
        print(f"\n⚠️ Error saving log: {e}")

def add_learning_entry(current_entries):
    """Adds a new learning entry."""
    print("\n--- Add New Learning Entry ---")
    # Module 1 & 2: Variables, input(), Strings
    topic = input("Enter the topic you learned: ")
    notes = input("Enter key notes/takeaways: ")
    category = input("Enter a category (e.g., Python Basics, RHEL9 Commands): ")
    
    # Module 6: datetime module
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    # Module 4: Dictionaries
    entry = {
        "timestamp": timestamp,
        "topic": topic,
        "notes": notes,
        "category": category
    }
    current_entries.append(entry) # Module 4: Appending to a list
    print(f"\n✨ Entry for '{topic}' added!")
    return current_entries

def view_learning_entries(entries):
    """Displays all learning entries."""
    print("\n--- Your Learning Entries ---")
    if not entries: # Module 2: Conditional logic
        print("ℹ️ Your learning log is currently empty.")
        return

    # Module 3: for loop & Module 4: Iterating through list of dictionaries
    for index, entry in enumerate(entries, start=1): # enumerate for numbering
        print(f"\nEntry #{index}:")
        # Module 1 & 2: String formatting (f-strings), accessing dictionary values
        print(f"  Timestamp: {entry['timestamp']}")
        print(f"  Topic    : {entry['topic']}")
        print(f"  Notes    : {entry['notes']}")
        print(f"  Category : {entry['category']}")
    print("-" * 27)

# --- Main Program Logic (Module 2 & 3: Control Flow - if/elif/else, while loop) ---
def main():
    """Main function to run the Learning Log program."""
    display_welcome()
    learning_entries = load_log_from_file() # Load existing entries at the start

    # Module 3: while loop for the main menu
    while True: 
        display_menu()
        # Module 1 & 2: input(), variable assignment
        choice = input("Enter your choice (1-5): ")

        # Module 2: if/elif/else for menu choices
        if choice == '1':
            learning_entries = add_learning_entry(learning_entries)
        elif choice == '2':
            view_learning_entries(learning_entries)
        elif choice == '3':
            save_log_to_file(learning_entries)
        elif choice == '4': # Re-load, though it loads at start too
            learning_entries = load_log_from_file()
        elif choice == '5':
            print("\n💡 Saving your progress before exiting...")
            save_log_to_file(learning_entries)
            print("👋 Happy Learning with DevCore School! Goodbye!")
            break # Module 3: break to exit the loop
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 5.")

# --- Standard Python entry point (Module 0: Implied - Running a Python script) ---
if __name__ == "__main__":
    # This ensures main() runs only when the script is executed directly
    main()