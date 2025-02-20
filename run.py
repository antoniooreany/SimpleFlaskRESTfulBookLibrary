# import logging
# from app import create_app, db
# import keyboard
# import threading
#
# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# app = create_app()
#
# with app.app_context():
#     db.create_all()
#
# def run_server():
#     app.run()
#
# def confirm_shutdown():
#     response = input("Are you sure you want to shut down the server? (y/n): ")
#     if response.lower() == 'y':
#         logging.info("Server is shutting down...")
#         print("\nShutting down gracefully...")
#         app.do_teardown_appcontext()
#         exit(0)
#
# def listen_for_quit():
#     keyboard.add_hotkey('ctrl+q', confirm_shutdown)
#     keyboard.wait('ctrl+q')
#
# if __name__ == '__main__':
#     server_thread = threading.Thread(target=run_server)
#     server_thread.start()
#     listen_for_quit()


import logging
from app import create_app, db
import keyboard
import threading

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = create_app()

with app.app_context():
    db.create_all()

def run_server():
    app.run()

def confirm_shutdown():
    response = input("Are you sure you want to shut down the server? (y/n): ")
    if response.lower() == 'y':
        logging.info("Server is shutting down...")
        print("\nShutting down gracefully...")
        app.do_teardown_appcontext()
        exit(0)

def listen_for_quit():
    keyboard.add_hotkey('ctrl+q', confirm_shutdown)
    keyboard.wait('ctrl+q')

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    listen_for_quit()

