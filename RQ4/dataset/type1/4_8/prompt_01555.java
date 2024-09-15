/**
 * This reader will read from octaveReader until a single line equal() spacer is read, after that this reader will
 * return eof. When this reader is closed it will update the state of octave to NONE.
 * 
 * @param octaveReader
 * @param spacer
 */
public OctaveExecuteReader(final BufferedReader octaveReader, final String spacer) 
{
    this.octaveReader = octaveReader;
    this.spacer = spacer;
}   