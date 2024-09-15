/**
 * SortFunction to animate the ViewGroup
 *
 * @param function subclass of SortFunction to be applied to the ViewGroup
 * @return SpruceBuilder object
 */
public SpruceBuilder sortWith(SortFunction function) 
{
    this.sortFunction = function;
    return this;
}   