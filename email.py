'''
An Email Simulation:
Populates an inbox list where it takes in the contents and email address from the received email to make a new Email object.
Displays the inbox with the message truncated to the user.
The user can open one email which then gives the option to mark as spam or delete.
When opening the email, it changes the status to read.
Opening unread folder shows the messages marked as unread
Opening spam folder shows the messages marked as spam.
Also allows the user to compose an email and places it in the outbox, which the use can view.
'''

#=====classes=====#
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


# displays inbox and perform actions on email
def get_email():
    # iterate through "inbox" using the "enumerate" function, which adds a counter for the current email number
    for email_num, email in enumerate(inbox, 1):
        # for each email, a truncated version of the email contents is made by taking the first 20 characters and adding "..." to the end
        truncated_message = email.email_contents[:20] + "..."
        # display the contents of the inbox in decorative manner
        output = f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ Email number: {email_num} ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
        output += f"From:\t\t{email.from_address}\n"
        output += f"Message:\t{truncated_message}\n"
        output += f"Read:\t\t{email.has_been_read}\n"
        output += f"Spam:\t\t{email.is_spam}\n"
        output += f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"

        print(output)
    
    # while loop allows action to be taken on a particular email
    while True:
        # try block negates any non integers entered
        try:
            # ask the user for which email to perform actions on (-1 added to compensate for enumerating from 1)
            email_choice = int(input("\nSelect the email number that you would like to open (-1 to go back to main menu): "))-1

            # if 0 or -2 and below picked give error
            if email_choice == -1 or email_choice <= -3:
                print("Invalid email number, please try again.\n")
                continue

            # if choice more than total emails give error
            elif email_choice > len(inbox)-1:
                print("Invalid email number, please try again.\n")
                continue
            
            # goes back to main menu when -1 picked
            elif email_choice == -2:
                break
            
            # when correct email number picked
            else:
                # Mark the email as read calling mark_as_read() method from Email class
                email = inbox[email_choice]
                email.mark_as_read()
                # Display/open the full selected email.
                output = f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ Email {email_choice+1} ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
                output += f"From:\t{inbox[email_choice].from_address}\n"
                output += f"Read:\t{inbox[email_choice].has_been_read}\n"
                output += f"Spam:\t{inbox[email_choice].is_spam}\n"
                output += f"Message:\n{inbox[email_choice].email_contents}\n"
                output += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"

                print(output)

                # while loop allows actions to be taked on selected email
                while True:
                    # try block negates any non integers entered
                    try:
                        # choose an action to take on the email, the user's input is converted to an integer
                        email_action = int(input("Would you like to do\n1. Delete email\n2. Mark as spam\n3. Exit\n: "))
                        
                        # calls delete() functions and displays confirmation of deletion
                        if email_action == 1:
                            delete(email_choice)
                            print("Email is deleted.\n")
                            break
                        
                        # calls mark_as_spam() method from Email class
                        elif email_action == 2:
                            Email.mark_as_spam(inbox[email_choice])
                            print("Email marked as spam.\n")
                            break
                        
                        # goes back to main menu
                        elif email_action == 3:
                            break

                        # incorrect integer entry gives error
                        else:
                            print("Invaid entry. Please type options 1, 2 or 3.\n")

                    # when non integer entered (ValueError) give error
                    except ValueError:
                        return print("Invalid input. Returning to main menu.\n")
                break

        # when non integer entered (ValueError) give error
        except ValueError:
            return print("Invalid input. Returning to main menu.\n")


# shows the user emails that have been unread
def get_unread_emails():
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ Unread Emails ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")
    # for each email in the inbox, check if the email's has_been_read property is equal to False and display those only
    for email in inbox:
        if email.has_been_read == False:
            output = "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            output += f"From:\t\t{email.from_address}\n"
            output += f"Message:\t{email.email_contents}\n"
            output += f"Spam:\t\t{email.is_spam}\n"
            output += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"

            print(output)


# shows the user emails that have been marked as spam
def get_spam_emails():
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ Spam Emails ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")
    # for each email in the inbox, check if the email's is_spam property is equal to True and display those only
    for email in inbox:
        if email.is_spam == True:
            output = "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            output += f"From:\t\t{email.from_address}\n"
            output += f"Message:\t{email.email_contents}\n"
            output += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"

            print(output)


# deletes an email from inbox list
def delete(email_choice):
    inbox.pop(email_choice)


# Call add_email() function and populate the inbox list.
add_email("max@gmail.com", "Are you going to Lunch on Wednesday?")
add_email("steve@gmail.com", "Thank you for your response, will respond shortly.")
add_email("prince@yahoo.com", "Hello I am a Nigerian prince, give me £1000 and I'll pay you back 10x over after I win back my throne.")
add_email("bob@outlook.com", "Are you going to golf on Wednesday?")

user_choice = ""

while user_choice != "quit":

    user_choice = input('''
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ Email Simulator ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
What would you like to do:
Inbox   - Read whole inbox (read/unread/spam) and perform actions
Unread  - Return a list of unread emails
Spam    - Return a list of spam emails
Send    - Send an email
Outbox  - Show sent emails
Quit    - Exit program
\n''').lower()

    if user_choice == "inbox":
        print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ Inbox ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        # call function to show user the number of emails 
        print(f"You have {get_count()} emails in your Inbox.\n")
        # call function to display emails
        get_email()

    elif user_choice == "unread":
        # call function to display unread emails
        get_unread_emails()

    elif user_choice == "spam":
        # call function to display spam emails
        get_spam_emails()

    elif user_choice == "send":
        # Prompt user to input 'email_address' and 'email_message' to send.
        email_address = input("\nEnter the email address: \n")
        email_contents = input("\nWrite your email message: \n")

        # Email is appended to 'sent' list.
        send_email= (email_address, email_contents)
        # email to appended to outbox
        outbox.append(send_email)
        print("Message sent to outbox.\n")

    elif user_choice == "outbox":
        print("\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ Outbox ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")
        # Loop through outbox list and display email address and message.
        for emails in outbox:
            print(f"From:\t{emails[0]} \nEmail:\t{emails[1]}\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")

    elif user_choice == "quit":
        print("Goodbye")

    else:
        print("Oops - incorrect input")
