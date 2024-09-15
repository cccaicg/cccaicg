/**
 * Remove the specified photo from the group.
 *
 * @param photoId The photo ID
 * @param groupId The group ID
 * @throws IOException
 * @throws SAXException
 * @throws FlickrException
 */

public void remove(String photoId, String groupId) throws IOException, SAXException,
        FlickrException 
{
    Map<String, Object> parameters = new HashMap<String, Object>();
    parameters.put("method", METHOD_REMOVE);
    parameters.put("photo_id", photoId);
    parameters.put("group_id", groupId);

    Response response = callMethod(parameters);
    checkError(response);
}       