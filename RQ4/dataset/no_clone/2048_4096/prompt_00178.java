/**
 * persist empty Optional of Date
 */





@Test
public void nullDate() 
{
    Optional<Date> nullDate = Optional.ofNullable(null);
    entityManager.persist(nullDate);
}   