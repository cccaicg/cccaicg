/**
 * @see ExecutionEntity#ensureExecutionTreeInitialized
 */
protected void ensureCaseExecutionTreeInitialized() 
{
    if (!caseExecutionTreeInitialized)
    {
        initializeCaseExecutionTree();
    }
}   