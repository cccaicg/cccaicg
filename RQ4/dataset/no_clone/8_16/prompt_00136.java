/** Add an index to a table. */
public void addIndex(final byte[] baseTableName, final IndexSpecification indexSpec) throws IOException 
{
    if (indexSpec.isUnique())
    {
        // create a unique index
        createUniqueIndex(baseTableName, indexSpec);
    }
    else
    {
        // create a non-unique index
        createIndex(baseTableName, indexSpec);
    }
}   