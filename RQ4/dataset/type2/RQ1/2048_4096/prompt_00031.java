// parent ////////////////////////////////////////////////////////////////////
public CaseExecutionEntity getParent() 
{
    ensureParentLoaded();
    return parent;
}   