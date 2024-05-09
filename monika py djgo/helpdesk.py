class HelpDeskTicket:
    def __init__(self, ticket_id, user, issue, status='Open'):
        self.ticket_id = ticket_id
        self.user = user
        self.issue = issue
        self.status = status

class HelpDeskSystem:
    def __init__(self):
        self.tickets = []

    def submit_ticket(self, user, issue):
        ticket_id = len(self.tickets) + 1
        ticket = HelpDeskTicket(ticket_id, user, issue)
        self.tickets.append(ticket)
        print(f"Ticket {ticket_id} submitted successfully.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets to display.")
            return
        print("Current Tickets:")
        for ticket in self.tickets:
            print(f"Ticket ID: {ticket.ticket_id}, User: {ticket.user}, Issue: {ticket.issue}, Status: {ticket.status}")

    def close_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.status = 'Closed'
                print(f"Ticket {ticket_id} closed successfully.")
                return
        print("Ticket not found.")

# Example usage
help_desk = HelpDeskSystem()

while True:
    print("\nHelp Desk Management System")
    print("1. Submit Ticket")
    print("2. View Tickets")
    print("3. Close Ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user = input("Enter your name: ")
        issue = input("Enter the issue: ")
        help_desk.submit_ticket(user, issue)
    elif choice == '2':
        help_desk.view_tickets()
    elif choice == '3':
        ticket_id = int(input("Enter the ticket ID to close: "))
        help_desk.close_ticket(ticket_id)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")