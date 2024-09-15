/**
 * Gets the value of the message property.
 * 
 * <p>
 * This accessor method returns a reference to the live list,
 * not a snapshot. Therefore any modification you make to the
 * returned list will be present inside the JAXB object.
 * This is why there is not a <CODE>set</CODE> method for the message property.
 * 
 * <p>
 * For example, to add a new item, do as follows:
 * <pre>
 *    getMessage().add(newItem);
 * </pre>
 * 
 * 
 * <p>
 * Objects of the following type(s) are allowed in the list
 * {@link Message }
 * 
 * 
 */
import java.util.ArrayList;
public List<Message> getMessage() 
{
    if (message == null)
    {
        message = new ArrayList<Message>();
    }
    return this.message;
}   