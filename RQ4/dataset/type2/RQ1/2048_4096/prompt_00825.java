/**
 * Namespace Location.
 *
 * @param uri
 *          namespace location uri.
 * @see DistributedLogNamespace
 * @return namespace builder.
 */
public DistributedLogNamespaceBuilder uri(URI uri) 
{
    this.uri = uri;
    return this;
}   