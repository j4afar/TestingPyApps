blogs  = dict()

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit:'
def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit
    selection = input(MENU_PROMPT)
    print_blogs()



def print_blogs():
    # Print the available blogs
    for key,blog in blogs.items():
        print('- {}'.format(blog))