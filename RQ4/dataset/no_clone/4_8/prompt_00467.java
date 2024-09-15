/**
 * Store a file on the server, including metadata
 * 
 * @param container   The name of the container
 * @param obj         The File containing the file to copy over
 * @param contentType The MIME type of the file
 * @param name        The name of the file on the server
 * @param metadata    A map with the metadata as key names and values as the metadata values
 * @param callback    The object to which any callbacks will be sent (null if you don't want callbacks)
 * @throws IOException   There was an IO error doing network communication
 * @throws HttpException There was an error with the http protocol
 * @throws FilesException 
 */
public boolean storeObject(String container, byte obj[], String contentType, String name, Map<String,String> metadata, IFilesTransferCallback callback) throws IOException, HttpException, FilesException 
{
    if (obj == null)
    {
        throw new FilesException("Object to store was null");
    }

    if (name == null || name.length() == 0)
    {
        throw new FilesException("Name to store was null or empty");
    }

    if (contentType == null || contentType.length() == 0)
    {
        throw new FilesException("Content type to store was null or empty");
    }

    String path = container + "/" + name;
    return this.storeObject(path, obj, contentType, metadata, callback);
}   