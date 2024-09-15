/**
 * Gets the value of the interfaceRef property.
 * 
 * <p>
 * This accessor method returns a reference to the live list,
 * not a snapshot. Therefore any modification you make to the
 * returned list will be present inside the JAXB object.
 * This is why there is not a <CODE>set</CODE> method for the interfaceRef property.
 * 
 * <p>
 * For example, to add a new item, do as follows:
 * <pre>
 *    getInterfaceRef().add(newItem);
 * </pre>
 * 
 * 
 * <p>
 * Objects of the following type(s) are allowed in the list
 * {@link QName }
 * 
 * 
 */
import java.util.ArrayList;
public List<QName> getInterfaceRef() 
{
    if (interfaceRef == null)
    {
        interfaceRef = new ArrayList<QName>();
    }
    return this.interfaceRef;
}   