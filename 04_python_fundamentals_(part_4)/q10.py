'''
Concept: OOP
Q10. Mini Project – OOP Chat System
Let’s create a Chat System using OOPs concepts. We have to create classes:
•
User
•
Message
•
ChatRoom
And we have to implement functions:
• sending messages
• viewing chat history
• user joining and leaving the chatroom
'''

# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1  # simple counter for unique message IDs

    def __init__(self, sender, content):
        self.sender = sender          # User object
        self.content = content        # text of the message
        self.id = Message.message_counter
        Message.message_counter += 1  # increment for next message

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None  # will hold a ChatRoom object

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []      # list of User objects
        self.messages = []   # list of Message objects

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)  # simulate sending to all users

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()


# ---------------------------------------
# Example Usage
# ---------------------------------------
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
