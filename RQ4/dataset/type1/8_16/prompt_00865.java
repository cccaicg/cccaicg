/**
	 * Returns the '<em><b>Book Category</b></em>' literal with the specified literal value.
	 * <!-- begin-user-doc -->
 * <!-- end-user-doc -->
	 * @generated
	 */
public static BookCategory get(String literal) 
{
		for (int i = 0; i < VALUES_ARRAY.length; ++i)
		{
			BookCategory result = VALUES_ARRAY[i];
			if (result.toString().equals(literal))
			{
				return result;
			}
		}
		return null;
	}	