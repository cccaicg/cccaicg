/**
 * Gets the value of the relation property.
 * 
 * <p>
 * This accessor method returns a reference to the live list,
 * not a snapshot. Therefore any modification you make to the
 * returned list will be present inside the JAXB object.
 * This is why there is not a <CODE>set</CODE> method for the relation property.
 * 
 * <p>
 * For example, to add a new item, do as follows:
 * <pre>
 *    getRelation().add(newItem);
 * </pre>
 * 
 * 
 * <p>
 * Objects of the following type(s) are allowed in the list
 * {@link Relation }
 * 
 * 
 */
import java.util.ArrayList;
public List<Relation> getRelation() 
{
    if (relation == null)
    {
        relation = new ArrayList<Relation>();
    }
    return this.relation;
}   