/**
 * @param entity
 *            The entity which the error detail is about.
 * @param dateTime
 *            The datetime of the error detail.
 * @param message
 *            The message of the error detail.
 * @param rc
 *            The return code of the error detail (nullable).
 */
protected EntityErrorDetail(T entity, DateTime dateTime, String message, Integer rc) 
{
    this.entity = entity;
    this.dateTime = dateTime;
    this.message = message;
    this.rc = rc;
}   