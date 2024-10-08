/**
 * Thransforms string to float
 * 
 * @param value
 *            value that will be transformed
 * @param field
 *            value will be assigned to this field
 * @return Float that represents value
 * @throws TransformationException
 *             if something went wrong
 */
@Override
public Float transform(String value, Field field) throws TransformationException{
	try
	{
		return Float.parseFloat(value);
	}
	catch(Exception e)
	{
		throw new TransformationException(e);
	}
}