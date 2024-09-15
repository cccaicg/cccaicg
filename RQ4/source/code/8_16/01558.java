/**
 * Retrieves a serialized <code>Automaton</code> from a stream.
 * @param stream input stream with serialized automaton
 * @exception IOException if input/output related exception occurs
 * @exception OptionalDataException if the data is not a serialized object
 * @exception InvalidClassException if the class serial number does not match
 * @exception ClassCastException if the data is not a serialized <code>Automaton</code>
 * @exception ClassNotFoundException if the class of the serialized object cannot be found
 */
public static Automaton load(InputStream stream) throws IOException, OptionalDataException, ClassCastException, 
                                                        ClassNotFoundException, InvalidClassException{
	ObjectInputStream s = new ObjectInputStream(stream);
	return (Automaton)s.readObject();
}