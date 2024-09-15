/**
 * <code>string ref_id = 1;</code>
 * @param value The bytes for refId to set.
 * @return This builder for chaining.
 */
public Builder setRefIdBytes(
    com.google.protobuf.ByteString value) 
{
  if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);

  refId_ = value;
  onChanged();
  return this;
}   