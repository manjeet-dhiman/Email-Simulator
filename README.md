# Email-Simulator
A Python program that simulates an email messaging system.

## Description
This program simulates a basic email client by populating an inbox list with emails.<br />
*It takes the contents and email address from the received email to create a new Email object.<br />
*The inbox can be displayed with the message truncated to the user.<br />
*The user can open one email and then has the option to mark it as spam or delete it. When an email is opened, its status changes to "read".<br />
*Additionally, the program has a feature that allows the user to compose an email, which is placed in the outbox.

## Programming principles
This program practices the programming concept of classes in Object Oriented Programming. Furthermore it employs programming functions such as enumerate, .pop(), append() and a good amount of conditional logic.

## Running the program
Run the email.py file in any Python IDE, such as Visual Studio Code.

## Code preview
```
class Email():
    # constructor takes in four arguments, with has_been_read and is_spam set to False by default
    def __init__(self, from_address, email_contents, has_been_read = False, is_spam = False):
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = has_been_read
        self.is_spam = is_spam
    
    # method is used to change the value of the has_been_read property from False to True.
    def mark_as_read(self):
        self.has_been_read = True
        return self.has_been_read

    # method is used to change the value of the is_spam property from False to True.
    def mark_as_spam(self):
        self.is_spam = True
        return self.is_spam


# empty lists that will be populated after functions and methods
inbox = []
outbox = []

#=====functions=====#
# populates inbox list with emails
def add_email(from_address, email_contents):
    email_object = Email(from_address, email_contents)
    inbox.append(email_object)


# returns the number of emails in the inbox
def get_count():
    return len(inbox)

```
