class BrowsingHistory:
    def __init__(self):
        """Initialize an empty stack for browsing history."""
        self.history = []

    def add_page(self, url):
        """Add a new page to the browsing history stack."""
        self.history.append(url)
        print(f"Added page: {url}")

    def remove_page(self):
        """Remove the most recently added page from the stack."""
        if self.history:
            removed_page = self.history.pop()
            print(f"Removed page: {removed_page}")
            return removed_page
        else:
            print("No pages to remove.")
            return None

    def get_page_count(self):
        """Return the number of pages in the browsing history."""
        count = len(self.history)
        print(f"Number of pages viewed: {count}")
        return count

    def is_empty(self):
        """Check if the browsing history stack is empty."""
        empty = len(self.history) == 0
        print(f"Browsing history is empty: {empty}")
        return empty

# Testing the BrowsingHistory class
if __name__ == "__main__":
    history_manager = BrowsingHistory()
    
    # Add some pages
    history_manager.add_page("https://example.com")
    history_manager.add_page("https://python.org")
    history_manager.add_page("https://github.com")
    
    # Check the number of pages
    history_manager.get_page_count()
    
    # Remove some pages
    history_manager.remove_page()
    history_manager.remove_page()
    
    # Check if history is empty
    history_manager.is_empty()
    
    # Remove remaining pages
    history_manager.remove_page()
    
    # Check if history is empty after removing all pages
    history_manager.is_empty()
    
    # Try to remove a page from an empty history
    history_manager.remove_page()

