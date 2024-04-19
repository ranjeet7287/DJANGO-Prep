# Event Management Example
# Assume you have two sets representing attendees for two different events.

event1_attendees = {'Alice', 'Bob', 'Charlie', 'David'}
event2_attendees = {'Charlie', 'Eva', 'Frank', 'David'}

# Check for common attendees using set intersection
common_attendees = event1_attendees & event2_attendees
print("Common Attendees:", common_attendees)

# Add a new attendee to one event
event1_attendees.add('Grace')

# Remove an attendee from the other event
event2_attendees.remove('Eva')

# Union of attendees from both events
all_attendees = event1_attendees | event2_attendees
print("All Attendees:", all_attendees)
