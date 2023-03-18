# import google news #one news at a time 

from GoogleNews import GoogleNews

# Create a GoogleNews object
googlenews = GoogleNews()

# Set the search query
googlenews.search('breaking news')

# Fetch the news
googlenews.get_page(1)

# Extract the news articles and store them in a list
news_items = googlenews.results()

# Initialize the news index to 0
news_index = 0

# Display the first news article
while news_index < len(news_items):
    if any(word.lower() in news_items[news_index]['desc'].lower() for word in ['english', 'news', 'breaking']):
        print(news_items[news_index]['title'])
        print(news_items[news_index]['link'])
        break
    else:
        news_index += 1

# Wait for user input to display the next news
while True:
    user_input = input("Enter 'next news' to display the next news or 'exit' to quit: ")
    if user_input.lower() == 'next news':
        # Move to the next news article if there are more articles to display
        if news_index < len(news_items) - 1:
            news_index += 1
            # Display the next news article
            while news_index < len(news_items):
                if any(word.lower() in news_items[news_index]['desc'].lower() for word in ['english', 'news', 'breaking']):
                    print(news_items[news_index]['title'])
                    print(news_items[news_index]['link'])
                    break
                else:
                    news_index += 1
        else:
            print("No more news to display.")
            break
    elif user_input.lower() == 'exit':
        break
    else:
        print("Invalid input. Please enter 'next news' or 'exit'.")
