/**
 * Main processing method for the Log object
 */
public void run() 
{
    while (true)
    {
        try
        {
            // Get the next message from the queue
            Message message = messageQueue.take();

            // Process the message
            processMessage(message);
        }
        catch (InterruptedException e)
        {
            // Handle the exception
            e.printStackTrace();
        }
    }
}   