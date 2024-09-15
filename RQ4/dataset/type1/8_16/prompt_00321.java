/**
 * Gets the value of the entityOrViewEntityOrExtendEntity property.
 * 
 * <p>
 * This accessor method returns a reference to the live list,
 * not a snapshot. Therefore any modification you make to the
 * returned list will be present inside the JAXB object.
 * This is why there is not a <CODE>set</CODE> method for the entityOrViewEntityOrExtendEntity property.
 * 
 * <p>
 * For example, to add a new item, do as follows:
 * <pre>
 *    getEntityOrViewEntityOrExtendEntity().add(newItem);
 * </pre>
 * 
 * 
 * <p>
 * Objects of the following type(s) are allowed in the list
 * {@link Entity }
 * {@link ExtendEntity }
 * {@link ViewEntity }
 * 
 * 
 */
import java.util.ArrayList;
public List<Object> getEntityOrViewEntityOrExtendEntity() 
{
    if (entityOrViewEntityOrExtendEntity == null)
    {
        entityOrViewEntityOrExtendEntity = new ArrayList<Object>();
    }
    return this.entityOrViewEntityOrExtendEntity;
}   