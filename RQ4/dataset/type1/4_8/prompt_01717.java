/**
 * Gets the value of the attributeName property.
 * 
 * <p>
 * This accessor method returns a reference to the live list,
 * not a snapshot. Therefore any modification you make to the
 * returned list will be present inside the JAXB object.
 * This is why there is not a <CODE>set</CODE> method for the attributeName property.
 * 
 * <p>
 * For example, to add a new item, do as follows:
 * <pre>
 *    getAttributeName().add(newItem);
 * </pre>
 * 
 * 
 * <p>
 * Objects of the following type(s) are allowed in the list
 * {@link String }
 * 
 * 
 */
import java.util.ArrayList;
public List<String> getAttributeName() 
{
    if (attributeName == null)
    {
        attributeName = new ArrayList<String>();
    }
    return this.attributeName;
}   