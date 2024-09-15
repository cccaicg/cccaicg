/**
 * wait for msgs
 *
 */
public void run() 
{
    while (true)
    {
        try
        {
            String msg = (String) in.readObject();
            System.out.println(msg);
        }
        catch (IOException | ClassNotFoundException e)
        {
            e.printStackTrace();
        }
    }
}   