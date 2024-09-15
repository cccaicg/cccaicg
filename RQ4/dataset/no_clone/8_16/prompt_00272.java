/**
 * Initializes the successor list.
 */

private void initSuccessorList() 
{
    successorList = new ArrayList<>();
    for (int i = 0; i < 4; i++)
    {
        successorList.add(new ArrayList<>());
    }
}   