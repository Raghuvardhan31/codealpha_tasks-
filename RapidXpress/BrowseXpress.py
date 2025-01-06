from googlesearch import search

def internet_search(query, num_results=10):
    try:
        # Perform the search
        results = search(query, num_results=num_results)
        return list(results)
    except Exception as e:
        return [f"Error: {str(e)}"]
if __name__ == "__main__":
    query = input("Enter your search query: ")
    print(f"Searching for: {query}\n")
    
    results = internet_search(query)
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result}")
