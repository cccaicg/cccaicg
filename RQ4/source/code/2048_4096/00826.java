/**
 * Set the input stream of the serialized bytes data of this record set.
 *
 * @param in
 *          input stream
 * @return builder
 */
public Builder setInputStream(InputStream in){
    this.in = in;
    return this;
}