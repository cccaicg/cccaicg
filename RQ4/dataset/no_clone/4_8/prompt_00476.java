/**
 * Deletes a container
 * 
 * @param name  The name of the container
 * @throws IOException   There was an IO error doing network communication
 * @throws HttpException There was an error with the http protocol
 * @throws FilesAuthorizationException The user is not Logged in
 * @throws FilesInvalidNameException   The container name is invalid
 * @throws FilesNotFoundException      The container doesn't exist
 * @throws FilesContainerNotEmptyException The container was not empty
 */
public boolean deleteContainer(String name) throws IOException, HttpException, FilesAuthorizationException, FilesInvalidNameException, FilesNotFoundException, FilesContainerNotEmptyException 
{
    if (!isValidName(name)) {
        throw new FilesInvalidNameException();
    }

    String path = "/v1/containers/" + name;

    return delete(path);
}   