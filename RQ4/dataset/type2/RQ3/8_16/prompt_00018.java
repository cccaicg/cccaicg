/**
 * Gets the document URL.
 *
	 * @return      a "file:" URL for the current directory
 */

public URL getDocumentBase() 
{
    try
    {
        return new URL("file:" + System.getProperty("user.dir") + "/");
    }
    catch (MalformedURLException e)
    {
        return null;
    }
}	