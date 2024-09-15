/**
 * This function aids loading of pending tickets from an array of tickets.
 */
public void LoadPendingTickets() 
{
    // Iterate through the array of pending tickets
    for (int i = 0; i < pendingTickets.length; i++)
    {
        // Check if the current ticket is not null
        if (pendingTickets[i] != null)
        {
            // Load the ticket into the system
            LoadTicket(pendingTickets[i]);
        }
    }
}   