/**
 * Replaces the TypeAccess list element at index {@code i} with the new node {@code node}.
 * @param node The new node to replace the old list element.
 * @param i The list index of the node to be replaced.
 * @apilevel high-level
 * @ast method 
 * 
 */
import java.util.List;
public void setTypeAccess(Access node, int i) 
{
    List<Access> list = getTypeAccessList();
    list.setChild(node, i);
}   