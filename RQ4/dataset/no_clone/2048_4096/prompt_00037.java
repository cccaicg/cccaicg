/**
 * This assumes that all children have been fetched
 */
protected boolean matches(ExecutionTree tree) 
{
    if (tree == null)
    {
        return false;
    }
    if (tree instanceof ExecutionTree)
    {
        return matches((ExecutionTree) tree);
    }
    return false;
}   