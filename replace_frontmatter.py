import os
import re

def search_and_replace(directory):
    while True:
        # Prompt user for word or phrase to find
        search_term = input("Enter word or phrase to find (case-sensitive): ")

        # If search term is empty, continue to next iteration
        if not search_term.strip():
            continue

        # Prompt user for replacement word or phrase
        replace_term = input("Enter replacement word or phrase: ")

        # Recursively search through the directory
        for root, _, files in os.walk(directory):
            for file in files:
                # Check if file is a Markdown file
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        content = f.read()

                    # Extract frontmatter content
                    frontmatter_pattern = r'^---\n(.*?\n)---'
                    updated_content = re.sub(frontmatter_pattern, lambda match: match.group(0).replace(search_term, replace_term), content, flags=re.DOTALL)

                    # Write updated content back to the file
                    with open(file_path, "w") as f:
                        f.write(updated_content)
                        print(f"Replaced '{search_term}' with '{replace_term}' in '{file_path}'")

        # Prompt user to continue or exit
        choice = input("Press Enter to search again or type 'exit' to quit: ").lower()
        if choice == "exit":
            break

def main():
    # Prompt user for directory path
    directory = input("Enter directory path: ")
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    search_and_replace(directory)
    print("Search and replace operation completed.")

if __name__ == "__main__":
    main()

