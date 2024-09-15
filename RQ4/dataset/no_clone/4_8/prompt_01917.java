/**
 * Takes the given stream and makes a String out of whatever data it has. Be
 * really careful with this, as it will just attempt to read whatever's in
 * the stream until it stops, meaning it'll spin endlessly if this isn't the
 * sort of stream that ends.
 * 
 * @param stream
 *            InputStream to read from
 * @return a String consisting of the data from the stream
 */
protected static String getStringFromStream(InputStream stream)
        throws IOException 
{
    StringBuilder builder = new StringBuilder();
    byte[] buffer = new byte[1024];
    int bytesRead;
    while ((bytesRead = stream.read(buffer)) != -1)
    {
        builder.append(new String(buffer, 0, bytesRead));
    }
    return builder.toString();
}       